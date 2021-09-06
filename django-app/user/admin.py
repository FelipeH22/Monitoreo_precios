from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin


# Register your models here.

#from .models import Personas
from .models import PerPro
from .models import precios_productos_cliente

#admin.site.register(Personas)
admin.site.register(PerPro)
admin.site.register(precios_productos_cliente)
