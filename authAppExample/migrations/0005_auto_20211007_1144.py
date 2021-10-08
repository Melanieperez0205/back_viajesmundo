# Generated by Django 3.2.8 on 2021-10-07 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authAppExample', '0004_auto_20211007_1051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='isActive',
            new_name='alimentacion',
        ),
        migrations.RenameField(
            model_name='account',
            old_name='balance',
            new_name='banios',
        ),
        migrations.AddField(
            model_name='account',
            name='descripcion',
            field=models.CharField(default='', max_length=50, verbose_name='Descripcion inmueble'),
        ),
        migrations.AddField(
            model_name='account',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='account',
            name='habitaciones',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='account',
            name='precio',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='account',
            name='ubicacion',
            field=models.CharField(default='', max_length=50, verbose_name='Ubicacion inmueble'),
        ),
        migrations.AddField(
            model_name='account',
            name='valoracion',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=1),
        ),
    ]
