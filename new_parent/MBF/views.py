from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from chartit import DataPool, Chart
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import CareTaker, BreastFed, BottleFed, DiaperStatus, Temperature, Sleep, Wake, Baby
from .forms import CreateUserForm, CareTakerForm, BabyForm, BreastFedForm, \
                   BottleFedForm, DiaperStatusForm, TemperatureForm, SleepForm, WakeForm

@login_required
def dashboard(request):
    care_taker = CareTaker.objects.get(user=request.user)
    babys = care_taker.family.baby_set.all()
    context = {
               'babys': babys}
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

@login_required
def create_child(request):
    baby_form = BabyForm(request.POST)
    if baby_form.is_valid():
        baby = baby_form.save()
        return HttpResponseRedirect('/MBF/')

    return render(request, 'MBF/create_baby.html', {'baby_form': baby_form})

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
def add_event(request, event_type):
    event_form_list = {'breast': BreastFedForm,
                       'bottle': BottleFedForm,
                       'diaper': DiaperStatusForm,
                       'temperature': TemperatureForm,
                       'sleep': SleepForm,
                       'wake': WakeForm}
    care_taker = CareTaker.objects.get(user=request.user)

    if request.method == "GET":
        try:
            baby_id = int(request.GET['baby_id'])
            baby = Baby.objects.get(id=baby_id)
        except Baby.DoesNotExist:
            return HttpResponseServerError("No records exist!")

    if request.method == "POST":
        form = event_form_list[event_type](request.POST)
        baby_id = int(request.POST['baby_id'])
        baby = Baby.objects.get(id=baby_id)
        if form.is_valid():
            event = form.save(commit=False)
            event.baby = baby
            event.save()
            return HttpResponseRedirect('/MBF/')
    else:
        form = event_form_list[event_type]()

    if care_taker.family == baby.family:
        return render(request, 'MBF/add_event.html', {'form': form,
                                                      'baby_id': baby_id})
    else:
        raise PermissionDenied

def bottle_chart(request):
    baby_id = int(request.GET['baby_id'])
    #Step 1: Create a DataPool with the data we want to retrieve.
    event_data = \
        DataPool(
           series=
            [{'options': {
               'source': BottleFed.objects.get(baby.id=baby_id)},
              'terms': [
                'event_time',
                'amount']}
             ])
    def dt_convert(dt_object):
        return dt_object.strftime('%a %b %d')

    #Step 2: Create the Chart object
    cht = Chart(
            datasource = event_data,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'event_time': [
                    'amount']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Bottle Feeding'},
               'xAxis': {
                    'title': {
                       'text': 'Date'}},
                'yAxis': {
                    'title': {
                        'text': 'Amount (oz)'}}},
            x_sortf_mapf_mts = (None, dt_convert, False))

    #Step 3: Send the chart object to the template.
    return render(request, 'MBF/bottle_chart.html',{'chart': cht})
