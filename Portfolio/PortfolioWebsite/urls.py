from .views import HomePage, AboutPage, ProfilePage
from django.urls import path
from . import views


urlpatterns = [
    path('profile', ProfilePage.as_view()),
    path('about', AboutPage.as_view()),
    path('home', HomePage.as_view()),
    path('', HomePage.as_view()),

] 
