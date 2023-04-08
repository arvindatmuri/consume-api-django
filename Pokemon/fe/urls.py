from django.urls import path
from .views import pokemon_list, pokemon

urlpatterns = [
    path('pokemon/<int:pokemon_id>/', pokemon, name='pokemon'),
    path('', pokemon_list, name='pokemon_list'),
]