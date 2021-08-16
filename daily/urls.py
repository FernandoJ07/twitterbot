from django.contrib.auth import logout
from django.urls import path
from . import views

urlpatterns = [
    path('', views.credential, name='credential'),
    path('home', views.home, name='home'),
    path('register', views.register, name='register'),
    path('logout', views.logout_view, name='logout'),
    path('login', views.login_view, name='login')
]