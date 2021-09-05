"""mon_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from product import views as product_views
from scraper import views as scraper_views
from user import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('new/',scraper_views.scraper,name='new'),
    path('login/',user_views.log,name='login'),
    path('products/',product_views.show_products,name='products'),
    path('details/',product_views.show_details,name='details'),
    path('', user_views.log,name=''),
]