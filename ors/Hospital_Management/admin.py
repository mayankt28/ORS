from django.contrib import admin
from .models import Appointment , Avaliable , Hospital , Department,Doctor

# Register your models here.

admin.site.register(Appointment)
admin.site.register(Avaliable)
admin.site.register(Hospital)
admin.site.register(Department)
admin.site.register(Doctor)

