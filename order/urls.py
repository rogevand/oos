from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:service_id>/', views.history, name='history')
]