from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required,user_passes_test
from django.views.generic import View
from servicebill import settings
# Create your views here.
from tanent.models import Tanent


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
    context = {
        'tanents': Tanent.objects.all(),
        'years': year_list(2020,2100),
        'month': month_list()
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

