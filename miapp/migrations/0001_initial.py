# Generated by Django 3.0.5 on 2020-09-08 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('contenido', models.TextField()),
                ('publicado', models.BooleanField()),
                ('fecha_creacion_articulo', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion_articulo', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=250)),
                ('fecha_creacion_categoria', models.DateTimeField()),
            ],
        ),
    ]
