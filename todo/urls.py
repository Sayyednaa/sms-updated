# in todo/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('<int:pk>/update/', views.task_update, name='task_update'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('syallbuss/', views.syalfun, name='syallbuss'),
    path('syallbuss/add/', views.syal_add, name='syallbuss'),
    path('syallbuss/update/<int:pk>', views.syal_update, name='syallbuss'),
    path('syallbuss/delete/<int:pk>', views.syal_delete, name='syallbuss'),
]
