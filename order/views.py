from django.shortcuts import render
from django.http import HttpResponse
from .models import Service
from django.template import context


def index(request):
    recent_services_list = Service.objects.order_by('date')[:5]
    context = {
        'recent_services_list': recent_services_list,
    }
    return render(request, 'order/index.html', context)

def history(request, service_id):
    return  HttpResponse("you are looking at the %s service " % service_id)

