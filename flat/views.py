from django.shortcuts import render, redirect
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import HttpResponse
import json

@login_required(login_url='login')
def add(request,**kwargs):
    if request.POST:
        try:
            flat = Flat()
            flat.flat_no = request.POST.get('flat_no')
            flat.size = request.POST.get('size')
            flat.owner = Member.objects.get(id=request.POST.get('owner'))
            flat.full_clean()
            flat.save()
            return redirect('/flat')

        except ValidationError as e:
            context = {}
            request.POST._mutable = True
            context['flat'] = request.POST
            context['error'] = str(e.message_dict)
            return render(request, 'flat/add.html', context)
    context = {'owner': Member.objects.all()}
    return render(request, 'flat/add.html', context=context)


@login_required(login_url='login')
def index(request, **kwargs):
    return render(request, 'flat/index.html')


@login_required(login_url='login')
def flat_data(request, **kwargs):
    context = {}
    context['flat'] = Flat.objects.all()
    return render(request, 'flat/table_data.html',context=context)



@login_required(login_url='login')
def delete(request, flat_id, **kwargs):

    flat = Flat.objects.get(id=flat_id)
    flat.delete()
    response_data = {}
    response_data['result'] = 'done'
    response_data['message'] = 'Member Deleted SuccessFully'
    response_data['status'] = True
    return HttpResponse(json.dumps(response_data), content_type="application/json")


@login_required(login_url='login')
def edit(request,flat_id, **kwargs):
    if request.POST:
        try:
            flat = Flat.objects.get(id=flat_id)
            flat.flat_no = request.POST.get('flat_no')
            flat.size = request.POST.get('size')
            flat.owner = Member.objects.get(id=request.POST.get('owner'))
            flat.full_clean()
            flat.save()
            context = {}
            context['flat'] = flat
            context['owner'] = Member.objects.all()
            return render(request, 'flat/edit.html', context=context)

        except ValidationError as e:
            context = {}
            request.POST._mutable = True
            request.POST['id'] = flat_id
            context['flat'] = request.POST
            context['error'] = str(e.message)
            print(e.message)
            context['owner'] = Member.objects.all()
            return render(request, 'flat/edit.html', context)


    flat = Flat.objects.get(id=flat_id)
    context = {}
    context['flat'] = flat
    context['owner'] = Member.objects.all()
    return render(request, 'flat/edit.html',context=context)