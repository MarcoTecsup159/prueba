from django.db import models

class Mensaje(models.Model):
    contenido = models.CharField(max_length=200)
