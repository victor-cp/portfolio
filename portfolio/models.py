from django.db import models
# data types
from django.db.models.fields import CharField
# viene de otro conjunto de paquetes de django
from django.db.models.fields.files import ImageField

# Create your models here.


class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
