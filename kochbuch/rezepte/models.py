from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):   # Kategorieklasse für Rezepte
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name  # Echter name statt "Objekt"


class Recipe(models.Model):
    title = models.CharField('Titel', max_length=300)
    image = models.ImageField('Bild')
    ingr = models.TextField('Zutaten', max_length=600)
    instr = models.TextField('Zubereitung', max_length=20000)
    category = models.ManyToManyField(Category)
