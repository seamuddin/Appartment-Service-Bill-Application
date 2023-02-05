from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView,LoginView
urlpatterns = [
    path('',views.index,name='tanent'),
    path('tanents/',views.tanent_data,name='tanents'),
    path('add/',views.add,name='tanent_add'),
    path('delete/<int:tanent_id>',views.delete,name='tanent_delete'),
    path('edit/<int:tanent_id>',views.edit,name='tanent_edit'),
]
