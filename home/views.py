from django.shortcuts import render
from django.views import View
from django.views.generic import *
from django.db import connection
from .models import *

class home(TemplateView):
    template_name='faradars-in-mobile-4.html'

class p_list(ListView):
    model= prodacts
    template_name="p_list.html"
    context_object_name="p_list"

class p_detale(DetailView):
    model= prodacts
    template_name= 'p_detale.html'
    pk_url_kwarg='id'



