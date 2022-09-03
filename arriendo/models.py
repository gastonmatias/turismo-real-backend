from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    id = models.BigAutoField('Id usuario',primary_key=True)
    email = models.CharField('Email',max_length=100,unique=True)
    rut = models.CharField('Rut',max_length=100)
    name = models.CharField('Nombre',max_length=100)
    last_name = models.CharField('Apellido',max_length=100)
    password = models.CharField(max_length=100)
    regular_customer = models.BooleanField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email','name','last_name','rut']

    def __str__(self):
        return f'{self.name}, {self.last_name}'
    
    # para determinar si puede acceder o no al admin de django
    def has_perm(self,perm,obj = None):
        return True
    
    def has_module_perms(self,app_label):
        return True




