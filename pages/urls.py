from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns=[
    path('home', views.index, name='index'),
    path('menu', views.menu),
    path('about', views.about),
    path('reservation', views.reservation),
    path('login', views.login),
]