from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import CareTaker
from .forms import CreateUserForm, CareTakerForm

def dashboard(request):
    context = {}
    return render(request, 'MBF/dashboard.html', context)

def create_user(request):
    caretaker_form = CareTakerForm(request.POST)
    user_form = CreateUserForm(request.POST)
    if user_form.is_valid() and caretaker_form.is_valid():
        # user_name = user_form.cleaned_data['user_name']
        # password = user_form.cleaned_data['password']
        user = user_form.save()
        # user = User.objects.create_user(username=user_name, password=password)
        phone = caretaker_form.cleaned_data['phone_number']
        relation = caretaker_form.cleaned_data['relation']
        caretaker = CareTaker.objects.create(user=user, phone_number=phone, relation=relation)
        return HttpResponseRedirect('/login/')

    return render(request, 'MBF/create_user.html',
                 {'caretaker_form': caretaker_form, 'user_form': user_form})
