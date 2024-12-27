# from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# podempos enviar archivos html

def hello(request):
    return HttpResponse("<h1>Hello world</h1>")