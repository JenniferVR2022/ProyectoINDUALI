# Generated by Django 4.1.1 on 2023-03-19 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receta', '0005_remove_receta_estandar'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='estandar',
            field=models.CharField(default=1, max_length=50, verbose_name='Estandar'),
            preserve_default=False,
        ),
    ]
