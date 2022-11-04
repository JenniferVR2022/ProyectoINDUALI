from django.db import models
from django.utils.translation import gettext_lazy as _


class Componente (models.Model):
   codComponente=models.TextField(max_length=50, verbose_name="Código Componente")
   nomComponente=models.TextField(max_length=50, verbose_name="Nombre Componente")
