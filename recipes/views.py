from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/home.html', context= {
        'name': 'Luiz Otavio',
    })


def sobre(request):
    return HttpResponse('Sobre')

def contato(request):
    return render(request, 'me-apague/temp.html')
