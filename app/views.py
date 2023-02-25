from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,TemplateView,DetailView
from app.models import *

class Home(TemplateView):
    template_name='app/home.html'

class SchoolList(ListView):
    model=School
    context_object_name='schools'
    template_name='app/SchoolList.html'
    #queryset=School.objects.filter(name='jsp')
    ordering=['location']

class SchoolDetail(DetailView):
    model=School
    context_object_name='i'

