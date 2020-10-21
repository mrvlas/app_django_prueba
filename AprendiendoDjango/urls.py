"""AprendiendoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

# importamos miapp con las vistas
from miapp import views

# Para pasar paremetros por la URL se utiliza /<str:atributo>

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    path('inicio/',views.index, name="index"),
    path('hola-mundo/',views.hola_mundo, name="hola_mundo"),
    path('contacto/', views.contacto, name="contacto"),
    path('quienes_somos/',views.quienes_somos, name='quienes_somos'),
    path('crear-articulo/<str:title>/<str:content>/<str:public>/',views.crear_articulo, name='crear_articulo'),
    path('articulo/',views.articulo, name='articulo'),
    path('editar-articulo/<str:id>/',views.editar_articulo, name='editar_articulo'),
    path('listado-articulos/',views.listar_articulos, name='listado_articulos'),
    path('borrar-articulo/<int:id>/',views.borrar_articulos, name='borrar_articulo'),
    path('create-article/',views.create_article, name='create_article'),
    path('save-article/',views.save_article, name='save_article'),
    path('creacion-full-articulo/', views.creacion_full_articulo, name ='creacion_full_articulo')
]
