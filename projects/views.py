from django.shortcuts import render
from django.http import HttpResponse

from .models import Project

# Create your views here.
def home(request):
    projects = Project.objects.all()
    projects = Project.objects.filter(is_visible=True)
    projects = Project.objects.order_by("-rank", "title")

    return render(request, "home.html", {
     "projects":projects
    })

 
def about(request):
    return render(request, "about.html")

def availability(request):
    return render(request, "availability.html")
