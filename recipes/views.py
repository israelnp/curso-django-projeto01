from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html', {'nome':'Israel'})


def contato(request):
    return render(request, 'meapague/temp.html')


def sobre(request):
    return HttpResponse('Sobre')
