from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView,LoginView
urlpatterns = [
    path('add/',views.add,name='flat_add'),


]
