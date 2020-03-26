from django.contrib import admin
from .models import HelpRequests, HelpRequestsDetail, Clinics, Cities, Status, HelpResponces
# Register your models here.

admin.site.register([HelpRequests, HelpRequestsDetail, Clinics, Cities, Status, HelpResponces])
