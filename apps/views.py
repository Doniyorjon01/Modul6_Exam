from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class RegisterTemplateView(TemplateView):
    template_name = 'register.html'