from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from app.models import *
class SchoolList(ListView):
    model=School
    context_object_name='schools'
    template_name='app/SchoolList.html'
    #queryset=School.objects.filter(name='jsp')
    ordering=['location']
