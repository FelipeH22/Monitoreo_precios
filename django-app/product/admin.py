from django.contrib import admin

# Register your models here.
from .models import Productos
from .models import Precios
from .models import Precios_producto

admin.site.register(Productos) 
admin.site.register(Precios)
admin.site.register(Precios_producto)