from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    return HttpResponse("This is a home.")


def welcome(request):
    template = loader.get_template('home/welcome.html')
    return HttpResponse(template.render())
