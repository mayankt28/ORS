from django.db import models
from django.utils import timezone
from mgmt_sys.models import Patient

# Create your models here.

class Avaliable(models.Model):
    date = models.DateField()
    seats = models.IntegerField()


    def __str__(self):
        return str(self.seats)

class Appointment(models.Model):

    # app_id = models.AutoField()
    patient = models.ForeignKey(Patient , on_delete=models.CASCADE  ,null=True , blank=True)
    
    booking_id = models.IntegerField(primary_key=True)

    state = models.CharField(max_length=50 , null=False  )
    hospital = models.CharField(max_length=50,null=False )
    department = models.CharField(max_length=50,null=True)
    # hospital = models.ForeignKey(Hospital , on_delete=models.CASCADE ,null=True)
    # dep = models.ForeignKey (Department , on_delete=models.CASCADE , null=True)
    appointment_date = models.DateField(null=True,default=timezone.now())

    booking_date=models.DateTimeField( default=timezone.now())

    queue = models.IntegerField(null=True , blank=True)

    def __str__(self):
        return str(self.booking_id)

class Doctor(models.Model):


    doctorName              = models.CharField(max_length=100 ,blank=False)
    doctor_department       = models.CharField(max_length=100,blank=False)
    doctor_email            = models.CharField(max_length=100,blank=False)
    doctor_mobile           = models.CharField(max_length=200,blank=False)
    doctor_status           = models.CharField(max_length=100,blank=False,default='On')

    doctor_password         = models.CharField(max_length=100,blank=False)


    # department = models.ForeignKey(Department , on_delete=models.CASCADE , null=True)
    def __str__(self):
        return self.doctorName

class Department(models.Model):
    # hospital_name
    seats_available         = models.ForeignKey(Avaliable , on_delete=models.CASCADE , null=True)
    dep_name                = models.CharField(max_length=50 , null=False , blank=False)
    doctors                 = models.ForeignKey(Doctor , on_delete=models.CASCADE  ,null=True , blank=True)
    # available = models.IntegerField(null=True)

    def __str__(self):
        return self.dep_name


class Hospital(models.Model):


    hospitalName            = models.CharField(max_length=100 ,blank=False)
    hospital_type           = models.CharField(max_length=100,blank=False)
    under_govt              = models.CharField(max_length=100,blank=False)
    hospital_address        = models.CharField(max_length=200,blank=False)
    hospital_state          = models.CharField(max_length=100,blank=False)

    hospital_district       = models.CharField(max_length=100,blank=False)
    hospital_website        = models.URLField(max_length=255,blank=True)
    hmis                    = models.CharField(max_length=10,blank=False)

    hospital_doctor_num     = models.IntegerField(blank=True,null=True,default="5")

    nodal_officer_name      = models.CharField(max_length=100,blank=False)
    nodal_officer_email     = models.CharField(max_length=100,blank=False)
    nodal_officer_password  = models.CharField(max_length=100,blank=False)

    hmis_name               = models.CharField(max_length=100,blank=True)
    hmis_deploy_org_name    = models.CharField(max_length=100,blank=True)
    department              = models.ManyToManyField(Department)




    # department = models.ForeignKey(Department , on_delete=models.CASCADE , null=True)
    def __str__(self):
        return self.hospitalName



