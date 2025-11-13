from django.urls import path
from . import views
urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('markAsDone/<int:pk>/', views.markAsDone, name='markAsDone'),
    path('markAsUndone/<int:pk>/', views.markAsUndone, name='markAsUndone'),
    path('editTask/<int:pk>/', views.editTask, name='editTask'),
    path('deleteTask/<int:pk>/', views.deleteTask, name='deleteTask')]