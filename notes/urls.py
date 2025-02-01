from django.urls import path
from . import views

app_name = 'notes'
urlpatterns = [
    path('', views.home, name='home'),
    path('upload_note/', views.note_upload, name='upload_note'),
    path('delete_note/<int:note_id>/', views.delete_note, name='delete_note'),
    path('view_notes/<int:note_id>/', views.view_notes, name='view_notes'),
]


