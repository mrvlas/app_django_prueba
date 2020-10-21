from django.db import models

# Aca se crean los modelos 

# para crear el archivo de migracion (antes de cerarlo en la bbdd)
# py manage.py makemigrations

# Para crear las tablas y la estructura de la bbdd
# py manage.py sqlmigrate miapp (y el nombre de la migracion) 0001

# Para ejecutar y que se guarde en la bbdd 
# py manage.py migrate  


class Articulo(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.TextField()
    imagen = models.ImageField(default='null')
    publicado = models.BooleanField()
    fecha_creacion_articulo = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion_articulo = models.DateTimeField(auto_now=True)


class Categoria(models.Model):
    nombre =models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    fecha_creacion_categoria =  models.DateTimeField()
