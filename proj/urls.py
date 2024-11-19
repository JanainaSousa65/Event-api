from . import views
from django.urls import path

urlpatterns = [
    path('event/', views.evento_create, name='evento_create'),
    path('events/', views.event_list, name='event_list'),
]

