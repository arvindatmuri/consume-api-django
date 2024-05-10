import requests
from django.core.paginator import Paginator
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})


def pokemon(request, pokemon_id):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}')
    pokemon_data = response.json()
    return render(request, 'pokemon.html', {'pokemon': pokemon_data})


def pokemon_move(request, move_id):
    response = requests.get(f'https://pokeapi.co/api/v2/move/{move_id}')
    move_data = response.json()
    return render(request, 'pokemon_moves.html', {'move': move_data})


def pokemon_list(request):
    # Get the page number from the request query parameters
    page_number = request.GET.get('page', 1)

    # Make a request to the PokeAPI to get the list of Pokemon
    response = requests.get('https://pokeapi.co/api/v2/pokemon?offset=0&limit=1300')
    pl = response.json()['results']
    # data = response.json()
    search_query = request.GET.get('search', '')
    if search_query:
        pl = [pk for pk in pl if search_query.lower() in pk['name'].lower()]
    # Create a Paginator object to handle the pagination
    paginator = Paginator(pl, 10)
    page = paginator.get_page(page_number)

    # Render the template with the data and pagination information
    return render(request, 'pokemon_list.html', {
        'pokemon_list': page.object_list,
        'page': page,
    })


def moves_list(request):
    # Get the page number from the request query parameters
    page_number = request.GET.get('page', 1)

    # Make a request to the PokeAPI to get the list of Pokemon
    response = requests.get('https://pokeapi.co/api/v2/move?offset=0&limit=1000')
    ml = response.json()['results']
    # data = response.json()
    search_query = request.GET.get('move_search', '')
    if search_query:
        ml = [mv for mv in ml if search_query.lower() in mv['name'].lower()]
    # Create a Paginator object to handle the pagination
    paginator = Paginator(ml, 10)
    page = paginator.get_page(page_number)

    # Render the template with the data and pagination information
    return render(request, 'moves_list.html', {
        'move_list': page.object_list,
        'page': page,
    })
