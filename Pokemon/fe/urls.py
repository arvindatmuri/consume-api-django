from django.urls import path
from .views import pokemon_list, moves_list, pokemon, pokemon_move, home

urlpatterns = [
    path('pokemon/move/<int:move_id>/', pokemon_move, name='move'),
    path('pokemon/<int:pokemon_id>/', pokemon, name='pokemon'),
    path('pokemon/list/', pokemon_list, name='pokemon_list'),
    path('move/list/', moves_list, name='move_list'),
    path('', home, name='home'),
]