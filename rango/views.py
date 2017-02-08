from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("rango says hello! <br/> <a href='/rango/about/'>About</a>")
def about(request):
    return HttpResponse("rango says here is the about page <br/> <a href='/rango/'>Back to where you came from</a>")