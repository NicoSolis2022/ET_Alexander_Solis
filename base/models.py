from django.db import models
from distutils.command.upload import upload
# Create your models here.


class cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=9)
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    clave = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to="imagenes", null=True)


    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.email)
