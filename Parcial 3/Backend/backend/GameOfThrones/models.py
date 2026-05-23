from django.db import models

# Create your models here.

class personajes(models.Model):
    nombre = models.CharField(max_length=100)  
    casa = models.CharField(max_length=100)  
    titulo = models.CharField(max_length=200, blank=True)
    estado = models.CharField(max_length=50, choices=[
        ('vivo', 'Vivo'),
        ('muerto', 'Muerto'),
        ('desconocido', 'Desconocido')
    ], default='vivo')
    imagen = models.ImageField(upload_to='got_imegen/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} de la Casa {self.casa}"