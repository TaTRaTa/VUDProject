from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from VUD.models import HelpRequests, HelpRequestsDetail, HelpResponces
from VUD.forms import ReqEditForm, ReqDetEditForm, ClinicForm, CityForm, RawCreateForm

def Home(request):
    return render(request, "vud/home.html", )