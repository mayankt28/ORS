from django.shortcuts import render , redirect , HttpResponse
from .forms import PatientForm , AppointForm , AppointDate #, Hospital_choiceForm
from Hospital_Management.models import Appointment,Avaliable, Department,Hospital
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .utils import get_booking_id , get_password
from mgmt_sys.models import Patient
from twilio.rest import Client
from patient_ors import settings

from django.db.models import Q



import datetime
from django.utils import timezone


# Create your views here.
def login_view(request):
    if request.method == 'POST':

        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username)
        print(password)
        user = authenticate(username = username,password = password)
        print(user.username + " "+user.password)

        if user is not None:
            login(request,user)
            print('hey')
            return redirect(get_patient_user_panel)
        else:
            error = 1
            return render(request,'mgmt_sys/loginp.html',{'error':error})
    else:
        return render(request,'mgmt_sys/loginp.html')


@login_required(login_url = login_view)
def logout_view(request):
    logout(request)
    return redirect(login_view)


def index(request):
    return render(request , 'mgmt_sys/HomePage.html')


# def login(request):
#     return render(request , 'mgmt_sys/login.html')

def choice(request):
    return render(request , "mgmt_sys/choice.html")




def patient_register(request):

    form = PatientForm(request.POST or None )

    if request.method=='POST':
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():

            email = form.cleaned_data['email']
            username = email
            password = get_password()
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print(password)
            
            request.session['user'] = [username , email , password ]
            
            obj=form.save(commit=False)
            request.session['patient'] = [obj.first_name,obj.middle_name , obj.last_name , obj.gender ,str(obj.dob), obj.son_daughter_of , obj.mother_name , obj.email , obj.mobile , obj.address , obj.state , obj.country , obj.pincode]
        
            return redirect(confirmation)


    return render(request , 'mgmt_sys/patient-register.html' ,{'form':form})

def patient_forgotpassword(request):
    return redirect(login_view)


def appointment(request):
    form = AppointForm(request.POST or None )

    print(request.method)

    if request.method == 'POST':
        print(form.is_valid())
        if form.is_valid():

            state = form.cleaned_data['state']


            hospital = form.cleaned_data['hospital']
            department = form.cleaned_data['department']


            obj=form.save(commit=False)
            obj.booking_id = get_booking_id()
            request.session['id'] = [obj.booking_id , state,hospital,department]
            print(request.session['id'])


            return redirect(calander)

    return render(request , 'mgmt_sys/appointment.html' ,{'form':form})





def calander(request):

    id = request.session['id']


    appointment_obj = Appointment()
    if request.method == 'POST':
        appointment_date = request.POST.get('appointment_date')
        id.append(appointment_date)
        
        request.session['id'] = id

        return redirect(patient_register)

    return render(request , 'mgmt_sys/calander.html',{})


def confirmation(request):

    # obj = Appointment.objects.filter(pk=pk)
    # print(obj.hospital)
    obj = request.session['id']
    b_id=obj[0]
    p_name = request.session['patient'][1]
    hospital = obj[2]
    department =obj [3]
    appointment_date = obj[4]

    print('come back@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

    return render(request,'mgmt_sys/confirm.html' , {'bid':b_id , 'pname':p_name , 'hospital':hospital , 'department':department , 'appointment_date':appointment_date } )




def save_data(request):
    u_list = request.session['user']
    p_list = request.session['patient']
    a_list = request.session['id']
    

    user= User.objects.create_user(u_list[0],u_list[1],u_list[2])
    print(user.username+" "+u_list[2]+",,"+u_list[1]+",,"+u_list[0])
    pat = Patient.objects.create(
        first_name = p_list[0],
        middle_name = p_list[1],
        last_name = p_list[2],
        gender = p_list[3],
        dob = p_list[4],
        son_daughter_of = p_list[5],
        mother_name = p_list[6],
        email = p_list[7],
        mobile = p_list[8],
        address = p_list[9],
        state = p_list[10] ,
        country = p_list[11],
        pincode = p_list[12],
        )
    pat.save()

    app = Appointment.objects.create(
        patient = pat,
        booking_id = a_list[0],
        state = a_list[1],
        hospital = a_list[2],
        department = a_list[3],
        appointment_date = a_list[4],


        )
    app.save()


    send_mail("Booking confirmed.","Password for login is ->"+u_list[2],'thathonkingwizard@gmail.com',[u_list[1]])
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(to='+917733920429', from_='+14062154272', body='Your booking has been confirmed.Thank you for using online portal')


    return render(request , 'mgmt_sys/confirmed.html',{'bid':app.booking_id , 'state':app.state , 'hospital':app.hospital ,'department':app.department , 'appointment_date':app.appointment_date , 'name':pat.first_name})




@login_required(login_url = login_view)
def get_patient_user_panel(request):

    username = request.user
    patient = Patient.objects.get(email=username)

    appointment_list = Appointment.objects.filter(patient_id=patient.pk)

    past_appointment = []
    upcoming_appointment = []

    for appointment in appointment_list:
        if appointment.appointment_date <= datetime.date.today():
            past_appointment.append(appointment)
        else:
            upcoming_appointment.append(appointment)

    context = {
        'patient': patient,
        'past_appointments': past_appointment,
        'upcoming_appointments': upcoming_appointment,   
    }
    
    return render(request,'mgmt_sys/Patient-UserPanel.html', context)

@login_required(login_url = login_view)
def patient_appointment_reschedule(request,booking_id=None):


    if request.method == 'POST':

        booking_id=request.session['booking_id']
        appointment_date = request.POST.get("appointment_date")
        
        booking = Appointment.objects.get(booking_id=booking_id)
        booking.appointment_date=appointment_date
        booking.save()

        hospital = Hospital.objects.filter(hospitalName=booking.hospital)
        department = Department.objects.filter(hospital=hospital)

        seatsAvailable = Avaliable.objects.filter(department=department)

        return redirect(get_patient_user_panel)

    request.session['booking_id']=booking_id
    booking = Appointment.objects.filter(booking_id=booking_id)
    context = {
        'appointment_date': booking[0].appointment_date,
    }
    return render(request,'mgmt_sys/reschedule-cal.html', context)



@login_required(login_url = login_view)
def patient_appointment_cancel(request,booking_id=None):
    booking = Appointment.objects.get(booking_id=booking_id)
    booking.delete()
    return redirect(get_patient_user_panel)

@login_required(login_url = login_view)
def patient_appointment_print(request):
    return redirect(get_patient_user_panel)

@login_required(login_url = login_view)
def booknew_appointment(request):

    if request.method == 'POST':


        booking_id=request.session['booking_id']

        hospitalName = request.POST.get("hospital")
        hospitalDepartment = request.POST.get("department")
        hospitalState = request.POST.get("state")
        
        appointment_date = request.POST.get("appointment_date")

        appointment = Appointment()
        appointment.patient = Patient.objects.filter(email=request.user).first()
        appointment.state=hospitalState
        appointment.department=hospitalDepartment
        appointment.hospital=hospitalName
        appointment.appointment_date=appointment_date

        appointment.save()
        return redirect(get_patient_user_panel)
    context = { }
    return render(request,'mgmt_sys/register-newAppointment.html', context)