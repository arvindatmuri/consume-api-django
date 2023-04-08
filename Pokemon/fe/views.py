import requests
from django.core.paginator import Paginator
from django.shortcuts import render


def pokemon(request, pokemon_id):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}')
    pokemon_data = response.json()
    return render(request, 'pokemon.html', {'pokemon': pokemon_data})


def pokemon_list(request):
    # Get the page number from the request query parameters
    page_number = request.GET.get('page', 1)

    # Make a request to the PokeAPI to get the list of Pokemon
    response = requests.get('https://pokeapi.co/api/v2/pokemon?offset=0&limit=1300')
    pl = response.json()['results']
    # data = response.json()

    # Create a Paginator object to handle the pagination
    paginator = Paginator(pl, 20)
    page = paginator.get_page(page_number)
    # print(page.object_list)
    # print(paginator)
    # Render the template with the data and pagination information
    return render(request, 'pokemon_list.html', {
        'pokemon_list': page.object_list,
        'page': page,
    })
