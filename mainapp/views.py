from django.shortcuts import render
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.
@login_required(login_url='login')
def index(request,**kwargs):
    return render(request,'dashboard/dashboard.html')


def login(request,**kwargs):
    return render(request,'login/login.html')

def loginview(request,**kwargs):
    return render(request, 'dashboard/index.html')
