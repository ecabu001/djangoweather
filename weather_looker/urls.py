from django.urls import path
from . import views

#insert new URLS here
urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name="about")
]
