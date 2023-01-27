from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
import random
from . import models
from django.conf import settings
from django.db.models.signals import post_save
from .models import Recipe, Category
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect # get_object_or_404 hinzugefügt
from django import forms
from django.urls import reverse_lazy
from string import ascii_uppercase
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.

class RecipeForm(forms.ModelForm):
    """Klasse zur Formularerstellung."""
    class Meta:
        model = models.Recipe
        exclude = []

class Recipe(DetailView):      # Rezept darstellen
    model = Recipe
    template_name = 'recipedetail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Recipe, self).get_context_data(*args, **kwargs)
        return context

#@login_required()
def upload(request):

    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():  # Formular überprüfen
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return HttpResponseRedirect('/')  # Umleitung
        else:
            print(form.errors)
    else:
        form = RecipeForm()  # leeres Formular
    return render(request, 'upload.html', dict(form=form))

def overview(request):      # Startseite
    all_recipes= models.Recipe.objects.all()
    return render(request, 'index.html', dict(recipes=all_recipes))


def category(request, category_name):
    category = models.Category.objects.get(name=category_name)    # ähnlich recipe, aber verknüpft mit rezept über manytomany, s. models
    return render(request, 'categories.html', dict(category=category))  # dict übergeben, wird anders abgefragt, s. category.html l.41


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        recipes = models.Recipe.objects.filter(title__icontains=searched)
        return render(request, 'search.html', dict(searched=searched, recipes=recipes))
    else:
        return render(request, 'search.html', {})


def recipe_a_z(request):
    for i in ascii_uppercase:
        letter = i
    all_recipes = models.Recipe.objects.order_by('title')
    return render(request, 'rezepte_a_z.html', dict(letter=letter, recipes=all_recipes))



def about(request):
    return render(request, 'about.html')


