from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Landing_page,name="Landing_page"),
    path('home',views.home,name="home"),
    path('home2',views.home2,name="home2"),
    path('index',views.index,name="index"),
    path('recommend',views.recommend,name="recommend"),
    path('recommend2',views.recommend2,name="recommend2"),
    path('contacts',views.contacts,name="contacts"),
    path('about_us',views.about_us,name="about_us"),
    path('login',views.login,name="login"),
    path('registration',views.registration,name="registration"),
    path('novels',views.novels,name="novels"),
    path('maps',views.maps,name="maps"),
]
