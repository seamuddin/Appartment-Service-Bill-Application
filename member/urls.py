from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView,LoginView
urlpatterns = [
    path('',views.index,name='member'),
    path('add/',views.add,name='member_add'),


]
