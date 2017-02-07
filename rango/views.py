from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says go eat a dick! <br/> <a href='/rango/about/'>About</a>")
def about(request):
    return HttpResponse("memes")