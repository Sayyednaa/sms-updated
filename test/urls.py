from django.urls import path
from . import views

app_name = 'test'
urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='home'),
    path('update/<int:pk>/', views.update, name='home'),
    path('delete/<int:pk>/', views.delete, name='home'),
   
]


