
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('donor/', views.Home , name="home"),
    path('needy/', views.Home , name="home"),
    path('login/', views.Home , name="home"),
]