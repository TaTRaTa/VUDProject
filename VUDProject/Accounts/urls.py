
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    # path('donor/', views.Home , name="donor"),
    # path('needy/', views.Home , name="needy"),
    # path('base/', views.Home , name="base"),
    # path('home/', views.Home , name="home"),
    path('register', views.register, name="register")


]