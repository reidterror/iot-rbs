from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('all_events/', views.all_events, name='all_events'),
    path('book/', views.book, name="book"),
]
