from django.shortcuts import render
from django.contrib.auth.decorators import login_required,user_passes_test
from . import models
# Create your views here.
@login_required(login_url='login')
def add(request,**kwargs):
    if request.POST:

        member = models.Member(name=request.POST.get('name'),
                               email=request.POST.get('email'),
                               mobile=request.POST.get('mobile'),
                               parmanent_address=request.POST.get('parmenent_address'),
                               nid=request.POST.get('nid')
                               )
        member.save()

    return render(request, 'member/add.html')