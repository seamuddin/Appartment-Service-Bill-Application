from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required,user_passes_test
from django.views.generic import View
from servicebill import settings
from . import html_to_pdf
# Create your views here.
from tanent.models import Tanent
from .models import BillHistory
from flat.models import Flat
import calendar
from datetime import datetime

from django.http import HttpResponse
from django.views.generic import View


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        # getting the template
        pdf = html_to_pdf('bill/invoice.html')

        # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')


@login_required(login_url='login')
def index(request,**kwargs):
    return render(request,'dashboard/dashboard.html')


def login(request,**kwargs):
    return render(request,'login/login.html')

def loginview(request,**kwargs):
    return render(request, 'dashboard/index.html')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/login')



@login_required(login_url='login')
def generate_bill(request,**kwargs):
    import random
    if request.POST:
        bill_history = BillHistory()
        bill_history.month = request.POST.get('month')
        bill_history.year = request.POST.get('year')
        bill_history.amount = request.POST.get('amount') if request.POST.get('amount') else 400
        bill_history.status = 0
        bill_history.invoice_number = 'BL'+str(BillHistory.objects.last().id+1 if BillHistory.objects.last() else 0) + str(random.randint(0,1000))
        bill_history.tanent = Tanent.objects.get(id = request.POST.get('tanent'))
        bill_history.date = datetime.now()
        bill_history.clean()
        bill_history.save()


        bill_info = {}
        bill_info['tanent'] = bill_history.tanent.name
        bill_info['month'] = calendar.month_name[int(bill_history.month)]
        bill_info['year'] = bill_history.year
        bill_info['amount'] = bill_history.amount
        bill_info['status'] = bill_history.status
        bill_info['flat_no'] = bill_history.tanent.flat.flat_no
        bill_info['size'] = bill_history.tanent.flat.size
        bill_info['amount'] = bill_history.amount
        bill_info['id'] = bill_history.id
        return render(request,'bill/bill_info.html',context=bill_info)


    context = {
        'tanents': Tanent.objects.all(),
        'years': year_list(2020,2100),
        'month': month_list(),
        'flats': Flat.objects.all()
    }
    return render(request,'bill/add.html', context=context)


def year_list(start,end):
    year = []
    for i in range(start,end):
        year.append(i)

    return year


def month_list():
    import calendar
    month = []
    for i in range(1,13):

        month.append({'name' : calendar.month_name[i], 'number' : i})


    return month

class GeneratePdfForBill(View):
    def get(self, request, bill_id, *args, **kwargs):
        data = {}

        # getting the template
        pdf = html_to_pdf('bill/invoice.html')

        # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')