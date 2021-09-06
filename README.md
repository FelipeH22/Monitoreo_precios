# Monitoreo_precios

### _Proyecto desarrollado para obtener análisis de los precios en los productos ingresados por el usuario (WEB)_

#### Descripción
_Haciendo uso de web scraping en Python se llevará un historial de precios que tomarán los productos ingresados por el usuario a lo largo del tiempo que dure en observación. Este obtendrá gráficos y análisis sobre la variación y se mostrará también que tan oportuna sería una compra en ese momento_

#### Instalar librerías
```
~$ pip install -r requirements.txt
```

##### Ejecutar por consola un archivo en específico
```
~$ python nombre_archivo.py
```

#### Estructura del proyecto
+ Monitoreo_precios/
    + bd/
        + conecta.py
        + pers_prod.py
        + persona.py
        + precio.py
        + producto.py
    + django-app/
        + mon_django/
            + \_\_init__.py
            + asgi.py
            + settings.py
            + urls.py
            + wsgi.py   
        + product/
            + migrations/
            + \_\_init__.py
            + admin.py
            + apps.py
            + models.py
            + tests.py
            + views.py
        + scraper/
            + migrations/
            + \_\_init__.py
            + admin.py
            + apps.py
            + models.py
            + tests.py
            + views.py
        + static/
            + resources/
            + styles/
        + templates/
            + detail_product.html
            + login.html
            + my_products.html
            + new.html
        + user/
            + migrations/
            + \_\_init__.py
            + admin.py
            + apps.py
            + models.py
            + tests.py
            + views.py
        + manage.py
        + requirements.txt 
    + structure
        + \_\_init__.py
        + bst.py
        + data_structure.py
        + hash_table.py
        + heap.py
        + node.py
        + node_bst.py
        + node_hash.py
        + precio_estructuras.py
        + stack.py   
    + ws/
        + ws.py  
    + README.md
    + requirements.txt
