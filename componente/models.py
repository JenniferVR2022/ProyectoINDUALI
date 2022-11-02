from enum import unique
from msilib.schema import Control
from tkinter import ACTIVE
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
 
class Componente (models.Model):
    codComponente=models.BigIntegerField(max_length=50, verbose_name="Cod Componente")
    nomComponente=models.BigIntegerField(max_length=50, verbose_name="Nom Componente")
