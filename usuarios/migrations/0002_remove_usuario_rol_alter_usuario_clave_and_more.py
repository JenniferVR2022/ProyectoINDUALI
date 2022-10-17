# Generated by Django 4.1.2 on 2022-10-16 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='rol',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='clave',
            field=models.CharField(max_length=20, verbose_name='Contraseña'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='estado',
            field=models.CharField(max_length=50, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='numeroDocumento',
            field=models.CharField(max_length=50, unique=True, verbose_name='Nùmero de documento'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipoDocumento',
            field=models.CharField(choices=[('C.C', 'Cédula de Ciudadanía'), ('C.E', 'Cédula de Extranjería'), ('P.A', 'Otro Tipo de Documento')], default='C.C', max_length=4, verbose_name='Tipo de Documento'),
        ),
    ]
