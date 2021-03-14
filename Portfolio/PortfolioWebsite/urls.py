from .views import HomePage, AboutPage, ProjectsPage, ContactsPage
from django.urls import path
from . import views


urlpatterns = [
    path('projects', ProjectsPage.as_view()),
    path('contact', ContactsPage.as_view()),
    path('about', AboutPage.as_view()),
    path('home', HomePage.as_view()),
    path('', HomePage.as_view()),

] 
