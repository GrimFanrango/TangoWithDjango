from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "I want to die!"}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("rango says here is the about page <br/> <a href='/rango/'>Back to where you came from</a>")