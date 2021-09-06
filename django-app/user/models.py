from django.db import models
from django.db.models.deletion import CASCADE
from product.models import Productos
#from django.contrib.auth.models import User
#from django.contrib.auth.models import BaseUserManager
#from django.contrib.auth.models import AbstractUser
#from django.contrib.auth.models import AbstractBaseUser
#from django.db.models.base import Model
#from django.contrib.auth.models import UserManager
# Create your models here.

class Personas(models.Model):

    email = models.CharField(db_column='correo', unique=True, max_length=400)
    password = models.CharField(db_column='pass', max_length=400)# Field renamed because it was a Python reserved word.
    
    class Meta:
        managed = True
        db_table = 'personas'
        

"""class Personas(AbstractBaseUser):

    email = models.CharField(db_column='correo', unique=True, max_length=400,primary_key=True)
    password = models.CharField(db_column='pass', max_length=400)# Field renamed because it was a Python reserved word.
    last_login = models.DateTimeField(db_column='last_login',blank=True, null=True)
    is_active = models.BooleanField(db_column='is_active',blank=True,null=True)
    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        managed = True
        db_table = 'personas'

"""

class PerPro(models.Model):

    id_persona = models.OneToOneField(Personas, db_column='id_persona', primary_key=True, on_delete=CASCADE)
    id_producto = models.ForeignKey(Productos, db_column='id_producto',on_delete=CASCADE)

    class Meta:
        managed = True
        db_table = 'per_pro'
        unique_together = (('id_persona', 'id_producto'),)

#map from view 
class precios_productos_cliente(models.Model):

    id_persona = models.OneToOneField(Personas,db_column='id_persona',primary_key=True,on_delete=CASCADE)
    correo =  models.CharField(db_column='correo', max_length=400)
    nombre =  models.CharField(db_column='nombre', max_length=400)
    precio = models.BigIntegerField(db_column='precio')

    class Meta:
        managed = False
        db_table = 'precios_productos_cliente'