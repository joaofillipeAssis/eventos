from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #transfora html em arquivo para ser executado
    return render(request, 'home.html') 