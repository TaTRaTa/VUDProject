from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
# Create your views here.

def Home(request):
    return render(request, "vud/index.html", )