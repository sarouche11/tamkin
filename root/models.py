from django.db import models
import random
from . import data as data_register
from django.contrib.auth.models import User

# Create your models here.



class SettingApp(models.Model):
    home_page = models.BooleanField(default=False)  
    registration = models.BooleanField(default=True)  
    email_notif = models.BooleanField(default=False)
    update_in = models.DateTimeField(auto_now=True)
    
    


def generate_code():
    return ''.join(random.choices('AZERTYUIOPQSDFGHJKLMWXCVBN123456789', k=10))


def generate_code_int():
    return str(random.randint(10000, 99999))


class Compagnion(models.Model):
    code = models.CharField(max_length=200, blank=False, null=False, unique=True, default=generate_code_int)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    nin = models.CharField(max_length=200, blank=True, null=True)
    genre = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        choices=data_register.genre.choices,
        default=data_register.genre.m
    )
    
    birthday = models.DateField(blank=True, null=True, default=None)
    phone = models.CharField(max_length=500, blank=True, null=True)
  


    active = models.BooleanField(default=True)
    insert_in = models.DateTimeField(auto_now_add=True)
    updated_in = models.DateTimeField(auto_now=True)

    def __str__(self):
         return self.code


class Wilaya(models.Model):
    code = models.CharField(max_length=200, blank=False, null=False, unique=True)
    name_fr = models.CharField(max_length=200, blank=True, null=True)
    name_ar = models.CharField(max_length=200, blank=True, null=True)
    
        
    active = models.BooleanField(default=True)
    insert_in = models.DateTimeField(auto_now_add=True)
    updated_in = models.DateTimeField(auto_now=True)

    def __str__(self):
         return self.name_fr or self.code
    

class Commune(models.Model):
    code = models.CharField(max_length=200, blank=False, null=False, unique=True)
    name_fr = models.CharField(max_length=200, blank=True, null=True)
    name_ar = models.CharField(max_length=200, blank=True, null=True)

    wilaya = models.ForeignKey(
          Wilaya,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name='wilayas'
    )
        
    active = models.BooleanField(default=True)
    insert_in = models.DateTimeField(auto_now_add=True)
    updated_in = models.DateTimeField(auto_now=True)

    def __str__(self):
         return self.name_fr or self.code    
    

class Registered (models.Model):

    code = models.CharField(max_length=20, unique=True, default=generate_code)
    nin = models.CharField(max_length=18, blank=True, null=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    genre = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        choices=data_register.genre.choices,
        default=data_register.genre.m
    )
    
    birthday = models.DateField(blank=True, null=True, default=None)
    phone = models.CharField(max_length=500, blank=True, null=True)
    wilaya= models.ForeignKey(
        Wilaya,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name='registered_people'
    )

    status = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        choices=data_register.registration.choices,
        default=data_register.registration.CHECK_NIN
    )

    attestation_file = models.FileField(upload_to='attestations/', blank=True, null=True)

    miclat = models.BooleanField(default=False)
    compagnion = models.ForeignKey(
    Compagnion,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="registrations"
)

    active = models.BooleanField(default=True)
    insert_in = models.DateTimeField(auto_now_add=True)
    updated_in = models.DateTimeField(auto_now=True)



    def __str__(self):
       return f"{self.first_name} {self.last_name} ({self.code})"
    

    
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, blank=False, null=False)
    subject = models.CharField(max_length=200, blank=False, null=False)
    message = models.TextField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_in = models.DateTimeField(auto_now=True)

    def __str__(self):
            return f'{self.name} - {self.subject}'


    
