from django.shortcuts import render

from django.views.generic import TemplateView, DetailView, ListView


class AboutPage(TemplateView):
    template_name = 'about.html'

class HomePage(TemplateView):
    template_name = 'home.html'

class ProfilePage(TemplateView):
    template_name = 'profile.html'
