from django.urls import path

from . import views

urlpatterns = [
     path('what-is-my-availability', views.availability, name='availability'),
     path('about', views.about, name='about'),
    path('', views.home, name='home'),
]