from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from VUD.models import HelpRequests, HelpRequestsDetail, HelpResponces
from VUD.forms import ReqEditForm, ReqDetEditForm, ClinicForm, CityForm, RawCreateForm
from Accounts.models import UserType

from django.contrib.auth.decorators import login_required

def login(request):
  return render(request, 'accounts/login.html')
