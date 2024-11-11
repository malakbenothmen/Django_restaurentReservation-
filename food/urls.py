from django.urls import path
from django.urls.conf import include
from food import views

urlpatterns=[
    path('food', views.foods),
    
]