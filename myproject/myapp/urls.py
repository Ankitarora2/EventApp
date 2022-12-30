from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('events/', views.event_list, name='event_list'),
    path('interest/', views.show_interest, name='show_interest'),
    path('rating/', views.rate_event, name='rate_event'),
]
