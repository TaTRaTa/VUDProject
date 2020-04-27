
from django.urls import path
from . import views

app_name = 'vud'

urlpatterns = [
    path('', views.HomeView.as_view() , name="home"),
    path('<int:pk>/detail', views.DetailView.as_view(), name="detail"),
    path('<int:pk>/edit', views.EditView.as_view(), name="edit"),
]