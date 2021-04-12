from django.urls import path

from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('base/', views.base, name='base'),
    path('history/', views.history, name='history'),
    path('addservice/', views.addservice, name='addservice'),
    path('great/', views.great, name='great'),

    
]