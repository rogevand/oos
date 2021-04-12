from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Service, Musician
from django.template import context
from .forms import NameForm


def index(request):
    recent_services_list = Service.objects.order_by('date')[:5]
    context = {
        'recent_services_list': recent_services_list,
    }
    return render(request, 'order/index.html', context)

def history(request, service_id):
    return  HttpResponse("you are looking at the %s service " % service_id)

def addservice(request):
    #service = get_object_or_404(Service, pk=service_id)
    data = Musician()
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            #this is the data returned by the post request
            Musician.objects.create(name=str(form.cleaned_data['post']), instrument1='', instrument2='', vocalYN=True)
            #data.name = 
            #data.save()
            
            print(data)
    else:
        form = NameForm()

    context = {'form': form, 'data': data}
    return render(request, 'order/addservice.html', context)


def great(request):
    context = {great: "great"}
    return render(request, 'order/great.html', context)
