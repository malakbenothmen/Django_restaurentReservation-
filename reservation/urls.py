from django.urls import path
from django.urls.conf import include
from . import views


app_name = 'reservation'
urlpatterns=[
    path('validation', views.validation),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>/', views.update , name='update'),
    path('delete/<int:id>/', views.delete , name='delete'),
    path('search', views.search, name='search'),

   
]