# Generated by Django 4.1 on 2023-03-09 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('numero_productos', models.PositiveIntegerField(default=0)),
                ('categoria_popular', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['nombre_categoria'],
            },
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('autor', models.CharField(max_length=100)),
                ('cuerpo', models.TextField()),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('numero_visitas', models.PositiveIntegerField(default=0)),
                ('destacada', models.BooleanField(default=False)),
                ('duracion_lectura_promedio', models.PositiveIntegerField(blank=True, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.categoria')),
            ],
            options={
                'ordering': ['-fecha_publicacion'],
            },
        ),
    ]