from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
from django.views import generic
from .models import HelpRequests, HelpRequestsDetail, HelpResponces
# Create your views here.

def Home(request):
    return render(request, "vud/index.html", )

class HomeView(generic.ListView):
    
    template_name = 'vud/home.html'
    context_object_name = 'reqs'

    def get_queryset(self):
        """Return the last five published questions."""
        return HelpRequests.objects.all()[:10].values('pk', 'created_by__username', 'created_at', 'city__name', 'title', 'expected_ppl_cnt', 'confirmed_ppl_cnt', 'onhold_ppl_cnt', 'valid_days', 'isopen')

class DetailView(generic.DetailView):

    model = HelpRequestsDetail
    template_name = 'vud/detail.html'

class EditView(generic.UpdateView):

    model = HelpRequestsDetail

    fields = [
        'description',
        'phone',
        'Facebook',
        'instagram',
        'email',   
    ]

    template_name = 'vud/edit.html'