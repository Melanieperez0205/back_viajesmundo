# Generated by Django 3.2.7 on 2021-10-21 03:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('habitaciones', models.IntegerField(default=0)),
                ('banios', models.IntegerField(default=0)),
                ('alimentacion', models.BooleanField(default=True)),
                ('valoracion', models.IntegerField(default=0.0)),
                ('precio', models.IntegerField(default=0)),
                ('descripcion', models.CharField(default='', max_length=50, verbose_name='Descripcion inmueble')),
                ('ubicacion', models.CharField(default='', max_length=50, verbose_name='Ubicacion inmueble')),
                ('lastChangeDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('isAvailable', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
            ],
        ),
    ]