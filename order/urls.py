from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:service_id>/', views.history, name='history'),
    path('addservice/', views.addservice, name='addservice'),
    path('great/', views.great, name='great'),

    
]