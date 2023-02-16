from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('',views.index,name='index'),
    path('dashboard/',views.index,name='dashboard'),
    path('login/', LoginView.as_view(template_name='login/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('generate_bill/', views.generate_bill, name='generate_bill'),
    path('pdf/', views.GeneratePdf.as_view()),

]
