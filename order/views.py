from django.db.models.fields import DateField
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Service, Musician
from django.template import context
from .forms import NameForm, ServiceForm

def base(request):

    return render(request, 'order/base.html')


    
def history(request):
    recent_services_list = Service.objects.order_by('date')[:5]
    context = {
        'recent_services_list': recent_services_list,
    }
    return render(request, 'order/history.html', context)

def addmusician(request):
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
    return render(request, 'order/addmusician.html', context)

def addservice(request):
    data = ServiceForm()
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            #this is the data returned by the post request
            #Musician.objects.create(name=str(form.cleaned_data['post']), instrument1='', instrument2='', vocalYN=True)
            Service.date  = form.cleaned_data['date']
            Service.leader = form.cleaned_data['leader']
            Service.theme =  form.cleaned_data['theme']
            Service.prelude_time = form.cleaned_data['prelude_time']
            Service.sermon = form.cleaned_data['sermon']
            Service.announcements = form.cleaned_data['announcements']
            # musicians need to be a dropdown selection
            Service.musicians = form.cleaned_data['musician1']
            Service.musicians = form.cleaned_data['musician2']
            Service.save()

            #Service.objects.create(date, leader, theme, prelude_time, sermon, announcements, musician1, musician2)
            
            print(data)
    else:
        form = ServiceForm()

    context = {'form': form, 'data': data}
    return render(request, 'order/addservice.html', context)


def great(request):
    context = {great: "great"}
    return render(request, 'order/great.html', context)

