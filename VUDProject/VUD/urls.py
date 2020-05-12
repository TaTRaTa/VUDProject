
from django.urls import path, re_path
from . import views

app_name = 'vud'

urlpatterns = [
    path('', views.HomeView.as_view() , name="home"),
    path('create/', views.create_req_view, name="create_req"),
    path('<int:pk>/detail', views.detail_req_view, name="detail"),
    path('<int:pk>/edit', views.edit_req_view, name="edit"),
    path('<int:pk>/isopen', views.switch_req_isopen_view, name="isopen_req"),
]