
from django.urls import path
from . import views

app_name = 'vud'

urlpatterns = [
    path('', views.Home , name="home"),
]