from django.db import models

# Create your models here.

class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.titulo

class Libro(Publicacion):
    autor = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)

class Revista(Publicacion):
    numero = models.IntegerField()
    editorial = models.CharField(max_length=100)

class Periodico(Publicacion):
    seccion = models.CharField(max_length=100)
    editor = models.CharField(max_length=100)
