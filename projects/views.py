from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("This is the homepage.")

def about(request):
    return HttpResponse("This is the aboutpage.")

def availability(request):
    return HttpResponse("I have no availability right now")
