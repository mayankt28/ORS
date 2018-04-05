from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [

	path('register-hospital/' , views.registerForm , name='register_hospital'),
 	path('hospital-login/' , views.hospital_login_view , name='hospital_login_Page'),
 	path('hospital-user-panel/' , views.HospitalUserPanel , name='hospital_dashboard'),
 	path('hospital-forgotpassword/',views.Hospital_forgotpassword,name='hospital-forgotpassword'),
	path('hospital-logout/', views.hospital_logout_view ,name = 'hospital-logout'),
	path('register-new-doctor/', views.register_new_doctor ,name = 'register_new_doctor'),
	url(r'^doctor/changeStatus/(?P<doctor_pk>\d+)/$' , views.changeStatus , name='patient_appointment_reschedule'),
    
]	