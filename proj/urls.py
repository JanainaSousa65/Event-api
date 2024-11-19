'''from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.home),
    path('event/', view=views.event_list),
    #path('evento/', view=views.evento_create)
    from django.urls import path'''
from . import views
from django.urls import path

urlpatterns = [
    path('event/', views.evento_create, name='evento_create'),
    path('events/', views.event_list, name='event_list'),
]

