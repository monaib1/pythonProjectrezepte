from django.urls import path, include
from .views import *

urlpatterns = [
    path('', overview, name='index'),
    path('upload', upload, name='upload'),
    path('recipe/<int:pk>', Recipe.as_view(), name='recipe'),
    path('search', search, name='search'),
    path('recipe_a_z', recipe_a_z, name='recipe_a_z'),
    path('about/', about, name='about'),
    path('category/', category, name='category'),
]
