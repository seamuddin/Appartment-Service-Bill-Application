from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView,LoginView
urlpatterns = [
    path('',views.index,name='index'),
    path('dashboard/',views.index,name='dashboard'),
    path('login/', LoginView.as_view(template_name='login/login.html'), name='login'),


]
