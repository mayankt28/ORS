from django import forms
from .models import Patient
from Hospital_Management.models import Appointment

class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        # fields = "__all__"
        exclude = ('hospital','uhid','aadhar')


# class Hospital_choiceForm(forms.Form):
#     state = forms.CharField(max_length=100)
#     hospital = forms.CharField(max_length=100)
#     department = forms.CharField(max_length=100)



class AppointForm(forms.ModelForm):


    class Meta:
        model = Appointment
        exclude = ('queue','appointment_date','booking_date' , 'booking_id' ,  )


class AppointDate(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ('appointment_date',)
