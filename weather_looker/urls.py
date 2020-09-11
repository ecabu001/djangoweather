from django.urls import path
from . import views

#insert new URLS here
#This is a new comment
urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name="about")
]
