from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView,LoginView
urlpatterns = [
    path('add/',views.add,name='flat_add'),
    path('',views.index,name='flat_list'),
    path('flats/',views.flat_data,name='flat_data'),
    path('delete/<int:flat_id>',views.delete,name='member_delete'),
    path('edit/<int:flat_id>',views.edit,name='member_edit')
]
