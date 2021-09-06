from django.db import models

# Create your models here.

class Productos(models.Model):

    id = models.BigAutoField(unique=True,primary_key=True)
    nombre = models.CharField (max_length=500)
    tienda = models.CharField(max_length=20)
    url = models.CharField(unique=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'productos'


class Precios(models.Model):

    id = models.BigAutoField(unique=True,primary_key=True)
    precio = models.IntegerField()
    fecha = models.DateTimeField()
    id_producto = models.ForeignKey(

        'Productos',
        models.DO_NOTHING,
        db_column='id_producto',
        blank=True,
        null=True
        )

    class Meta:
        managed = False
        db_table = 'precios'
        

#map from view 
class Precios_producto(models.Model):

    precio = models.BigIntegerField(db_column='precio')
    fecha = models.DateTimeField(db_column='fecha')
    id_producto = models.IntegerField(db_column='id_producto')
    nombre = models.CharField(primary_key=True,blank=True,db_column='nombre',max_length=400)
    tienda = models.CharField(db_column='tienda',max_length=400)
    url = models.CharField(db_column='url',max_length=1000)    

    class Meta:
        managed = False
        db_table = 'precios_producto'