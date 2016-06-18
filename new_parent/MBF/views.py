from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import CareTaker, BreastFed, BottleFed, DiaperStatus, Temperature, Sleep, Wake
from .forms import CreateUserForm, CareTakerForm, BabyForm, BreastFedForm, \
                   BottleFedForm, DiaperStatusForm, TemperatureForm, SleepForm, WakeForm

@login_required
def dashboard(request):
    breastList = BreastFed.objects.order_by('-event_time')
    bottleList = BottleFed.objects.order_by('-event_time')
    diaperList = DiaperStatus.objects.order_by('-event_time')
    tempList = Temperature.objects.order_by('-event_time')
    sleepList = Sleep.objects.order_by('-event_time')
    wakeList = Wake.objects.order_by('-event_time')
    context = {'breastList': breastList,
               'bottleList': bottleList,
               'diaperList': diaperList,
               'tempList': tempList,
               'sleepList': sleepList,
               'wakeList': wakeList}
    return render(request, 'MBF/dashboard.html', context)

def create_user(request):
    if request.method == 'POST':
        caretaker_form = CareTakerForm(request.POST)
        user_form = CreateUserForm(request.POST)
        if user_form.is_valid() and caretaker_form.is_valid():
            user = user_form.save()
            phone = caretaker_form.cleaned_data['phone_number']
            relation = caretaker_form.cleaned_data['relation']
            caretaker = CareTaker.objects.create(user=user, phone_number=phone, relation=relation)
            return HttpResponseRedirect('/login/')
    else:
        caretaker_form = CareTakerForm(initial={'phone_number': '+12345555555'})
        user_form = CreateUserForm()


    return render(request, 'MBF/create_user.html',
                 {'caretaker_form': caretaker_form, 'user_form': user_form})

def create_child(request):
    baby_form = BabyForm(request.POST)
    if baby_form.is_valid():
        baby = baby_form.save()
        return HttpResponseRedirect('/MBF/')

    return render(request, 'MBF/create_baby.html', {'baby_form': baby_form})

@login_required
def update_breast(request):
    breast_form = BreastFedForm(request.POST)
    if breast_form.is_valid():
        breast = breast_form.save()
        breast.baby = baby
        return HttpResponseRedirect('/MBF/')

    return render(request, 'MBF/update_breast.html', {'breast_form': breast_form})

@login_required
def update_bottle(request):
    bottle_form = BottleFedForm(request.POST)
    if bottle_form.is_valid():
        bottle = bottle_form.save()
        return HttpResponseRedirect('/MBF/')

    return render(request, 'MBF/update_bottle.html', {'bottle_form': bottle_form})

@login_required
def update_diaper(request):
    diaper_form = DiaperStatusForm(request.POST)
    if diaper_form.is_valid():
        ct = CareTaker.objects.get(user=request.user)
        baby = ct.family.babys[0]
        diaper = diaper_form.save()
        diaper.baby = baby
        diaper.save()
        return HttpResponseRedirect('/MBF/')

    return render(request, 'MBF/update_diaper.html', {'diaper_form': diaper_form})

@login_required
def update_temperature(request):
    temp_form = TemperatureForm(request.POST)
    if temp_form.is_valid():
        temp = temp_form.save()
        return HttpResponseRedirect('/MBF/')

    return render(request, 'MBF/update_temp.html', {'temp_form': temp_form})

@login_required
def update_sleep(request):
    sleep_form = SleepForm(request.POST)
    if sleep_form.is_valid():
        sleep = sleep_form.save()
        return HttpResponseRedirect('/MBF/')

    return render(request, 'MBF/update_sleep.html', {'sleep_form': sleep_form})

@login_required
def update_wake(request):
    wake_form = WakeForm(request.POST)
    if wake_form.is_valid():
        wake = wake_form.save()
        return HttpResponseRedirect('/MBF/')

    return render(request, 'MBF/update_wake.html', {'wake_form': wake_form})
