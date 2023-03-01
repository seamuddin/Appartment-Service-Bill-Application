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
    context['member'] = Member.objects.all()
    return render(request, 'member/index.html',context=context)


@login_required(login_url='login')
def delete(request, member_id, **kwargs):

    member = Member.objects.get(id=member_id)
    member.delete()
    response_data = {}
    response_data['result'] = 'done'
    response_data['message'] = 'Member Deleted SuccessFully'
    response_data['status'] = True
    return HttpResponse(json.dumps(response_data), content_type="application/json")


@login_required(login_url='login')
def edit(request,member_id, **kwargs):
    if request.POST:
        try:
            member = Member.objects.get(id=member_id)
            member.email = request.POST.get('email')
            member.name = request.POST.get('name')
            member.mobile = request.POST.get('mobile')
            member.parmanent_address = request.POST.get('parmanent_address')
            member.nid = request.POST.get('nid')
            member.plot_no = request.POST.get('plot_no')
            member.profession = request.POST.get('profession')
            member.save()
            context = {}
            context['member'] = member
            return render(request, 'member/edit.html', context=context)

        except ValidationError as e:
            context = {}
            request.POST._mutable = True
            request.POST['id'] = member_id
            context['member'] = request.POST
            context['error'] = str(e.message)
            print(e.message)
            return render(request, 'member/edit.html', context)


    member = Member.objects.get(id=member_id)
    context = {}
    context['member'] = member
    return render(request, 'member/edit.html',context=context)

# Create your views here.
@login_required(login_url='login')
def members_data(request, **kwargs):
    context = {}
    context['member'] = Member.objects.all()
    return render(request, 'member/table_data.html',context=context)



@login_required(login_url='login')
def add(request,**kwargs):
    if request.POST:
        try:
            member = Member()
            member.email = request.POST.get('email')
            member.name = request.POST.get('name')
            member.mobile = request.POST.get('mobile')
            member.parmanent_address = request.POST.get('parmanent_address')
            member.nid = request.POST.get('nid')
            member.plot_no = request.POST.get('plot_no')
            member.profession = request.POST.get('profession')
            member.full_clean()
            member.save()
            return redirect('/member')

        except ValidationError as e:
            context = {}
            request.POST._mutable = True
            context['member'] = request.POST
            context['error'] = str(e.message_dict)
            return render(request, 'member/add.html', context)
    return render(request, 'member/add.html')




