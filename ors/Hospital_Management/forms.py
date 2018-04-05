from django import forms
from .models import Appointment,Hospital,Doctor

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

class HospitalForm(forms.ModelForm):


    class Meta:
        model = Hospital
        exclude = {'department','hmis_deploy_org_name','hmis_name','hmis','hospital_doctor_num'}


class AppointForm(forms.ModelForm):


    class Meta:
        model = Appointment
        exclude = ('patient','queue','appointment_date','booking_date' , 'booking_id')


class AppointDate(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ('appointment_date',)

class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        exclude = ('doctor_status',)