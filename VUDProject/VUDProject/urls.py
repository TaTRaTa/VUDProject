
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vud/', include('VUD.urls')),
    path('tests/', include('Tests.urls')),
    path('acc/', include('Accounts.urls')),

]
