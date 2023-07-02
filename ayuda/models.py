from django.db import models

class Archivo(models.Model):
    archivo = models.FileField(upload_to='archivos/')

    def __str__(self):
        return self.archivo.name