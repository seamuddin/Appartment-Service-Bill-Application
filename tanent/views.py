from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import *
from django.core.exceptions import ValidationError
from django.http import HttpResponse
import json

# Create your views here.
@login_required(login_url='login')
def index(request,**kwargs):
    context = {}
    context['tanent'] = Tanent.objects.all()
    return render(request, 'tanent/index.html',context=context)


@login_required(login_url='login')
def delete(request, tanent_id, **kwargs):

    tanent = Tanent.objects.get(id=tanent_id)
    tanent.delete()
    response_data = {}
    response_data['result'] = 'done'
    response_data['message'] = 'Tanent Deleted SuccessFully'
    response_data['status'] = True
    return HttpResponse(json.dumps(response_data), content_type="application/json")


@login_required(login_url='login')
def edit(request,tanent_id, **kwargs):
    if request.POST:
        try:
            tanent = Tanent.objects.get(id=tanent_id)
            tanent.email = request.POST.get('email')
            tanent.name = request.POST.get('name')
            tanent.mobile = request.POST.get('mobile')
            tanent.parmanent_address = request.POST.get('parmanent_address')
            tanent.nid = request.POST.get('nid')
            tanent.date = request.POST.get('date')
            tanent.flat = Flat.objects.get(id=request.POST.get('flat'))
            tanent.save()
            context = {}
            context['tanent'] = tanent
            context['flat'] = Flat.objects.all()
            return render(request, 'tanent/edit.html', context=context)

        except ValidationError as e:
            context = {}
            request.POST._mutable = True
            request.POST['id'] = tanent_id
            context['tanent'] = request.POST
            context['error'] = str(e.message)
            print(e.message)
            return render(request, 'tanent/edit.html', context)


    tanent = Tanent.objects.get(id=tanent_id)
    context = {}
    context['tanent'] = tanent
    context ['flat'] = Flat.objects.all()
    return render(request, 'tanent/edit.html',context=context)

# Create your views here.
@login_required(login_url='login')
def tanent_data(request, **kwargs):
    context = {}
    if request.GET.get('name'):
        tanent = Tanent.objects.filter(name__contains = request.GET.get('name'))
        # print(tanent.query.__str__())
    else:
        tanent = Tanent.objects.all()
    context['tanent'] = tanent
    return render(request, 'tanent/table_data.html',context=context)



@login_required(login_url='login')
def add(request,**kwargs):
    if request.POST:
        try:
            tanent = Tanent()
            tanent.email = request.POST.get('email')
            tanent.name = request.POST.get('name')
            tanent.mobile = request.POST.get('mobile')
            tanent.parmanent_address = request.POST.get('parmanent_address')
            tanent.nid = request.POST.get('nid')
            tanent.date = request.POST.get('date')
            tanent.flat = Flat.objects.get(id=request.POST.get('flat'))
            tanent.full_clean()
            tanent.save()
            return redirect('/tanent')

        except ValidationError as e:
            context = {}
            request.POST._mutable = True
            context['tanent'] = request.POST
            context['flat'] = Flat.objects.all()
            context['error'] = str(e.message_dict)
            return render(request, 'tanent/add.html', context)
    context = {'flat': Flat.objects.all()}
    return render(request, 'tanent/add.html',context=context)




@login_required(login_url='login')
def payment_info(request,tanent_id, **kwargs):
    return render(request,'tanent/index.html')