from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView,LoginView
urlpatterns = [
    path('',views.index,name='tanent'),
    path('tanents/',views.tanent_data,name='tanents'),
    path('add/',views.add,name='tanent_add'),
    path('delete/<int:tanent_id>',views.delete,name='tanent_delete'),
    path('edit/<int:tanent_id>',views.edit,name='tanent_edit'),
    path('payment_info/<int:tanent_id>',views.payment_info,name='tanent_payment_info'),
    path('payment_data/<int:tanent_id>',views.payment_data,name='tanent_payment_data'),
    path('get_flat_charge/<int:tanent_id>',views.get_flat_charge,name='get_flat_charge'),
    path('pdf_data/<int:bill_id>',views.pdf_data,name='pdf_data'),
    path('change_tanent_flat/', views.change_tanent_flat, name='change_tanent_flat'),
]
