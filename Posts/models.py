from datetime import date
from django.db import models

class Post(models.Model):
    """CATEGORIES = [
       ('Dulce', 'Dulce'),
       ('Salado', 'Salado'),
       ('Vegetariano', 'Vegetariano'),
       ('Desayunos', 'Desayunos'),
       ('Sopas', 'Sopas'),
   ]"""

    titulo = models.CharField(max_length=20)
    ##categoria = models.CharField(max_length=512, choices=CATEGORIES)
    ingredientes = models.TextField(max_length=2000)
    texto = models.TextField(max_length=2000)
    autor = models.CharField(max_length=50)
    tiempo = models.CharField(max_length=50)
    porciones = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='imagenes_posts', null=True, blank=True)
    fecha = models.DateField(default=date.today)
    

    def __str__(self):
        return self.titulo


