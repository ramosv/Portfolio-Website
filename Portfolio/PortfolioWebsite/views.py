from django.shortcuts import render

from django.views.generic import TemplateView, DetailView, ListView


class AboutPage(TemplateView):
    template_name = 'about.html'

class HomePage(TemplateView):
    template_name = 'home.html'

class ProjectsPage(TemplateView):
    template_name = 'projects.html'

class ContactsPage(TemplateView):
    template_name = 'contact.html'
