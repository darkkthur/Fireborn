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
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
                ('duracion', models.PositiveIntegerField()),
                ('numero_reservas', models.PositiveIntegerField(default=0)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.categoria')),
            ],
            options={
                'ordering': ['-numero_reservas'],
            },
        ),
    ]
