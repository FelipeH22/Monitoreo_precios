# Monitoreo_precios

### _Proyecto desarrollado para obtener análisis de los precios en los productos ingresados por el usuario (WEB)_

#### Descripción
_Haciendo uso de web scraping en Python se llevará un historial de precios que tomarán los productos ingresados por el usuario a lo largo del tiempo que dure en observación. Este obtendrá gráficos y análisis sobre la variación y se mostrará también que tan oportuna sería una compra en ese momento_


#### Ejecutar proyecto
Creando un entorno virtual dentro del proyecto.
```
~$ pip install virtualenv
~$ virtualenv envProlog
```
##Instalar librerías
```
~$ pip install -r requirements.txt
```
##Ejecutar proyecto
```
~$ python manage.py runserver
```

#### Ejecutar por consola un archivo en específico
```
~$ python nombre_archivo.py

```

#### Estructura del proyecto
+ Monitoreo_precios/
    + Monitoreo_precios/
      + __init__.py
      + asgi.py
      + settings.py
      + urls.py
      + wsgi.py
    + templates/
    + creacion.sql/
    + manage.py
    + README.md
    + requirements.txt
    + WS.py
