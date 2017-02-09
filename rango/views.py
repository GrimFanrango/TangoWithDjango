from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page


def index(request):

    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html')

def show_category(request, category_name_slug):
    #Create a context dictionary which we can pass
    #to the template rendering engine
    context_dict = {}

    try:
        #try to find a category with the slug with the given name?
        category = Category.objects.get(slug=category_name_slug)

        #Get all the associated pages.
        pages = Page.objects.filter(category=category)

        #add our results to the template context under name pages.
        context_dict['pages'] = pages

        #Also take the category object from the database
        #and add it to the context dictionary.
        #and use it to verify that the category exists
        context_dict['category'] = category

    except Category.DoesNotExist:
        #If we didn't find the specified category we don't do anything
        #The template will display a zero category error for us
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context_dict)

