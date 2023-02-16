from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required,user_passes_test

from tanent import obj
from .models import *
from django.core.exceptions import ValidationError
from django.http import HttpResponse
import json
from mainapp.models import BillHistory
import calendar

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
    context['my_date'] = str(tanent.date)
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
    tanent = Tanent.objects.get(id=tanent_id)
    context = {}
    context['tanent'] = tanent
    return render(request,'tanent/payment_info.html', context=context)


@login_required(login_url='login')
def payment_data(request,tanent_id, **kwargs):
    date = Tanent.objects.get(id=tanent_id)
    date = date.date
    from datetime import datetime, timedelta
    from collections import OrderedDict
    dates = [str(date), str(datetime.today().date())]
    start, end = [datetime.strptime(_, "%Y-%m-%d") for _ in dates]
    month_list = list(
        OrderedDict(((start + timedelta(_)).strftime(r"%b %Y"), None) for _ in range((end - start).days)).keys())
    data_list=[]
    tanent = Tanent.objects.get(id=tanent_id)
    for month in month_list:
        data_list.append({'month': month,
                          'amount':calculate_service_charge(tanent.flat.size)

                          })
    context = {}
    context['bill'] = data_list
    context['tanent'] = tanent
    return render(request, 'tanent/payment_data.html', context=context)


def calculate_service_charge(flat_size):
    if int(flat_size) < 800:
        return 500
    elif int(flat_size) < 1200:
        return 800
    elif int(flat_size) >= 1200:
        return 1500



def get_flat_charge(request, tanent_id,**kwargs):
    flat_size = Tanent.objects.get(id=tanent_id).flat.size
    response_date = {'charge' : calculate_service_charge(flat_size)}
    return HttpResponse(json.dumps(response_date), content_type="application/json")


def pdf_data(request, bill_id,**kwargs):
    bill = BillHistory.objects.get(id=bill_id)

    bill_info = {
        'year' : bill.year,
        'month' : calendar.month_name[int(bill.month)],
        'tanent' : bill.tanent.name,
        'tanent_mobile' : bill.tanent.mobile,
        'tanent_email' : bill.tanent.email,
        'tanent_add' : bill.tanent.parmanent_address,
        'flat' : bill.tanent.flat.flat_no,
        'amount' : bill.amount,
        'status' : 'Paid' if bill.status == 1 else 'Unpaid',
        'invoice_no' : bill.invoice_number,
        'invoice_date' : bill.date.strftime("%Y-%m-%d %H:%M %p")
    }

    return render(request, 'bill/invoice.html', context=bill_info)