from django.contrib import admin
from django.urls import include, path
from order import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('order/', include('order.urls')),
    path('', views.base, name='base'),
]
