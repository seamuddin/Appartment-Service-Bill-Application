from django.shortcuts import render

# Create your views here.
def add(request,**kwargs):
    return render(request, 'flat/add.html')