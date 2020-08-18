from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.forms import ValidationError

from django.contrib.auth.decorators import login_required

def login(request):
  return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                messages.error(request, f'Email {email} already exists')
                return redirect(reverse('accounts:register'))

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            form.save()
            return redirect(reverse('vud:home'))
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)

