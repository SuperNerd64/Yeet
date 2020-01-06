from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class acuvisionView(TemplateView):
    template_name = 'index.html'
    
class appointmentView(TemplateView):
    template_name = 'yeetyeet.html'    