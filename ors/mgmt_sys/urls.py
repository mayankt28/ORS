from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('appointment/fill_details' , views.patient_register , name='patient_register_details'),
    path('patient-login/' , views.login_view, name='patient_login_Page'),
    path('patient-logout/' , views.logout_view, name='patient_logout_page'),
    path('choice/' , views.choice , name='choice'),
    path('appointment/',views.appointment , name = 'appointment'),
    path('register-patient/',views.appointment , name = 'register-patient'),
    path('patient-forgotpassword/',views.patient_forgotpassword , name = 'patient-forgotpassword'),
    path('cal',views.calander , name='cal'),
    path('save',views.save_data , name = 'save_data'), ########
    path('patient-panel/' , views.get_patient_user_panel , name='patient_user_panel'),
    url(r'^appointment/reschedule/(?P<booking_id>\d+)/$' , views.patient_appointment_reschedule , name='patient_appointment_reschedule'),
    url(r'^appointment/cancel/(?P<booking_id>\d+)/$' , views.patient_appointment_cancel , name='patient_appointment_cancel'),
    url(r'^appointment/print/(?P<booking_id>\d+)/$' , views.patient_appointment_print , name='patient_appointment_print'),
    
    path('appointment/booknew/' , views.booknew_appointment , name='booknew_appointment'),
    path('confirm/',views.confirmation , name='confirm'),
    path('' , views.index , name = 'index'),
]
