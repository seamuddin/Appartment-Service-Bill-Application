from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView,LoginView
urlpatterns = [
    path('',views.index,name='member'),
    path('members/',views.members_data,name='members'),
    path('add/',views.add,name='member_add'),
    path('delete/<int:member_id>',views.delete,name='member_add'),


]
