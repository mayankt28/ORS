"""patient_ors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include ,re_path

from mgmt_sys.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patient/' , include("mgmt_sys.urls")),
 	path('hospital/' , include("Hospital_Management.urls")),
 	path('', index ,name='choices'),

 	re_path(r'^paypal/',include('paypal.standard.ipn.urls')),
    re_path(r'^payment/',include('payment.urls',namespace='payment')),
]