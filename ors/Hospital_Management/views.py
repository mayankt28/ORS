from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import HospitalForm,DoctorForm
from .models import Hospital,Department,Doctor,Appointment

# Create your views here.

def registerForm(request):

    form = HospitalForm(request.POST or None )

    if form.is_valid():
        username = form.cleaned_data['nodal_officer_email']
        email = username
        password = form.cleaned_data['nodal_officer_password']
        user = User.objects.create_user(username,email,password)
        user.first_name = form.cleaned_data['nodal_officer_name']
        user.save()
        form.save()
        login(request,user)
        return redirect(HospitalUserPanel)

    

    return render(request , 'management/registerHospital.html' ,{'form':form})


def hospital_login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect(HospitalUserPanel)
        else:
            error = 1
            return render(request,'management/loginh.html',{'error':error})
    else:
	    return render(request,'management/loginh.html',{})


@login_required(login_url= hospital_login_view)
def HospitalUserPanel(request):

    print(request.user)
    hospital = Hospital.objects.get(nodal_officer_email=request.user.username)
    print(hospital)
    departments = Department.objects.filter(hospital=hospital)
    doctorList = []

    print(len(departments))

    for department in departments:
        doctors = Doctor.objects.filter(department=department)
        print(len(doctors))
        for doctor in doctors:
            doctorList.append(doctor)

    booking = Appointment.objects.filter(hospital=hospital.hospitalName)

    context = {
    
        'hospital':hospital,
        'department':departments,
        'doctorList':doctorList,
        'booking':booking,
    }
    return render(request,'management/hospitalPanel.html',context)

@login_required(login_url= hospital_login_view)
def hospital_logout_view(request):
    logout(request)
    return redirect(hospital_login_view)

@login_required(login_url= hospital_login_view)
def register_new_doctor(request):

    form = DoctorForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            hospital = Hospital.objects.get(nodal_officer_email=request.user.username)
            departments = Department.objects.filter(hospital=hospital)
            form.save()
            return redirect(HospitalUserPanel)
        return redirect(HospitalUserPanel)
    context = {
        'form':form,
    }
    return render(request,'management/register-new-doctor.html',context)



def Hospital_forgotpassword(request):
    return redirect(hospital_login_view)


@login_required(login_url= hospital_login_view)
def changeStatus(request,doctor_pk=None):


    doctor = Doctor.objects.get(pk=doctor_pk)

    if(doctor.doctor_status == 'On'):
        doctor.doctor_status = 'Off'
    else:
        doctor.doctor_status = 'On'

    doctor.save()


    return redirect(HospitalUserPanel)

