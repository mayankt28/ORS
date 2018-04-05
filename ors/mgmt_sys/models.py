from django.db import models
from django.utils import timezone
# from Hospital_Management.models import Avaliable,


# Create your models here.
Initial_choices = (
    ('mr' , 'MR'),
    ('ms' , 'MS'),
    ('mrs','MRS'),
    )

Gender_choices = (
    ('male' , 'MALE'),
    ('female' , 'FEMALE'),
    ('other','OTHER')
    )





class Patient(models.Model):
    
    first_name = models.CharField(max_length=50, blank = False)
    middle_name = models.CharField(max_length=20 ,  blank=True)
    last_name = models.CharField(max_length=20  , blank=True)

    # appointment_list = models.ForeignKey(Appointment , on_delete=models.CASCADE ,null=True )
    aadhar = models.CharField(max_length=12 , unique=True , null=True , blank=True)
    # hospital = models.CharField(max_length=50,null=True)
    # hospital = models.ForeignKey(Hospital , on_delete = models.CASCADE , null=True)
    uhid = models.IntegerField(null=True,blank=True)
    gender = models.CharField(max_length=10,blank=False)
    dob = models.DateField()
    
    son_daughter_of = models.CharField(max_length=50 ,blank=True,null=True)
    mother_name = models.CharField(max_length=50 ,blank=False,null=True)

    email = models.EmailField(max_length=50 ,  blank = True , default='None')
    mobile = models.IntegerField(blank = False)
    address = models.CharField(max_length=100 , blank=False)
    state = models.CharField(max_length=20 , blank=False)
    country = models.CharField(max_length=50 , blank = False)
    pincode = models.IntegerField(blank=False)


    def __str__(self):
        return self.first_name
