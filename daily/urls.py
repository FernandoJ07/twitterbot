from django.contrib.auth import logout
from django.urls import path
from . import views

urlpatterns = [
    path('', views.credential, name='credential'),
    path('home', views.home, name='home'),
    path('tweets', views.tweets, name='tweets'),
    path('newEntry', views.newEntry, name='newEntry'),
    path('delete/<int:entry_id>', views.delEntry, name = 'delete'),
    path('edit/<int:entry_id>', views.editEntry, name='edit'),
    path('register', views.register, name='register'),
    path('logout', views.logout_view, name='logout'),
    path('login', views.login_view, name='login')
]