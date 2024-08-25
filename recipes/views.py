from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('home 1')

def sobre(request):
    return HttpResponse('Sobre')

def contato(request):
    return HttpResponse('Contato')