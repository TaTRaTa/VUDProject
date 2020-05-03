from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import HelpRequests, HelpRequestsDetail, HelpResponces
from .forms import ReqEditForm, ReqDetEditForm
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

def detail_req_view(request, **kwargs):
    print(request, kwargs)
    template_name = 'vud/detail.html'
    model = get_object_or_404(HelpRequests, pk=kwargs.get('pk'))
    model_det = None

    # validate if user is not login then redirect into home page
    if not request.user.is_authenticated :
        return HttpResponseRedirect(reverse('vud:home'))

    # optional fields for object - HelpRequestsDetail
    try:
        model_det = HelpRequestsDetail.objects.get(pk=kwargs.get('pk'))
    except HelpRequestsDetail.DoesNotExist:
        model_det = None

    context = {
        'pk' : kwargs.get('pk'),
        'username' : model.created_by,
        'model' : model,
        'model_det': model_det,
    }

    return render(request, template_name, context)   

def edit_req_view(request, **kwargs):
    print(request, kwargs)
    template_name = 'vud/edit_req.html'
    obj, obj2 = None, None
    obj = get_object_or_404(HelpRequests, pk=kwargs.get('pk'))

    # validate if user is not login then redirect into home page
    if request.user != obj.created_by :
        return HttpResponseRedirect(reverse('vud:home'))

    # optional fields for object - HelpRequestsDetail
    try:
        obj2 = HelpRequestsDetail.objects.get(pk=kwargs.get('pk'))
    except HelpRequestsDetail.DoesNotExist:
        obj2 = None

    # forms instances
    form_req = ReqEditForm(request.POST or None, instance=obj)
    if obj2 is None:
        form_req_det = ReqDetEditForm(request.POST or None)
    else:
        form_req_det = ReqDetEditForm(request.POST or None, instance=obj2)

    if request.method == "POST":
        if form_req.is_valid() and form_req_det.is_valid():
            form_req.save()
            form_req_det.save()
            return HttpResponseRedirect(reverse('vud:detail', kwargs={'pk': kwargs.get('pk')}))
 
    context = {
        'pk' : kwargs.get('pk'),
        'username' : obj.created_by,
        'form' : form_req,
        'form2': form_req_det,
    }

    return render(request, template_name, context)

def switch_req_isopen_view(request, **kwargs):

    template_name = 'vud/detail.html'   
    obj = get_object_or_404(HelpRequests, pk=kwargs.get('pk'))

    # validate if user is not login then redirect into home page
    if request.user != obj.created_by :
        return HttpResponseRedirect(reverse('vud:home'))

    if request.method == "POST":
        if obj.isopen:
            obj.isopen = False
        else:
            obj.isopen = True
        obj.save()

        return HttpResponseRedirect(reverse('vud:detail', kwargs={'pk': kwargs.get('pk')}))   
     
    context = {
        'pk' : kwargs.get('pk'),
    }
    return render(request, template_name, context)