from django.shortcuts import render
from django.http import HttpResponse
import requests


def home(request):
    return render(request, "home.html", {})


def users(request):
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    # convert response data into json
    user = response.json()
    # print(user)
    return render(request, "users.html", {'users': user})
