from django.db import models

# Create your models here.
class ListaPrecio (models.Model):
    codListaPrecio=models.CharField(max_length=50, verbose_name="Cod Lista Precio")
    nomListaPrecio=models.CharField(max_length=50, verbose_name="Nom Lista Precio")
    tipoLista=models.CharField(max_length=50, verbose_name="Tipo Lista")
