from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import CreateUserForm

def dashboard(request):
    context = {}
    return render(request, 'MBF/dashboard.html', context)

def create_user(request):
    form = CreateUserForm(request.POST)
    if form.is_valid():
        user_name = form.cleaned_data['user_name']
        password = form.cleaned_data['password']
        user = User.objects.create_user(username=user_name, password=password)
        return HttpResponseRedirect('/MBF/')

    return render(request, 'MBF/create_user.html', {'form': form})
