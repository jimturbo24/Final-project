import pytz
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from chartit import DataPool, Chart
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import CareTaker, BreastFed, BottleFed, DiaperStatus, Temperature, Sleep, Wake, Baby
from .forms import CreateUserForm, CareTakerForm, BabyForm, BreastFedForm, \
                   BottleFedForm, DiaperStatusForm, TemperatureForm, SleepForm, \
                   WakeForm, CreateFamilyForm

@login_required
def dashboard(request):
    care_taker = CareTaker.objects.get(user=request.user)
    babys = care_taker.family.baby_set.all()
    context = {'babys': babys}
    return render(request, 'MBF/dashboard.html', context)

def home(request):
    context = {}
    return render(request, 'MBF/home.html', context)

def create_user(request):
    if request.method == 'POST':
        caretaker_form = CareTakerForm(request.POST)
        user_form = CreateUserForm(request.POST)
        family_form = CreateFamilyForm(request.POST)
        if user_form.is_valid() and caretaker_form.is_valid() and family_form.is_valid():
            user = user_form.save()
            family = family_form.save()
            phone = caretaker_form.cleaned_data['phone_number']
            relation = caretaker_form.cleaned_data['relation']
            caretaker = CareTaker.objects.create(user=user, family=family, phone_number=phone, relation=relation)
            return HttpResponseRedirect('/login/')
    else:
        caretaker_form = CareTakerForm()
        family_form = CreateFamilyForm()
        user_form = CreateUserForm()


    return render(request, 'MBF/create_user.html',
                 {'caretaker_form': caretaker_form,
                  'user_form': user_form,
                  'family_form': family_form})

@login_required
def create_child(request):
    baby_form = BabyForm(request.POST)
    if baby_form.is_valid():
        baby = baby_form.save()
        return HttpResponseRedirect('/MBF/')

    return render(request, 'MBF/create_baby.html', {'baby_form': baby_form})

def create_caretaker(request):
        caretaker_form = CareTakerForm(request.POST)
        user_form = CreateUserForm(request.POST)
        if caretaker_form.is_valid() and user_form.is_valid():
            user = user_form.save()
            current_ct = CareTaker.objects.get(user=request.user)
            family = current_ct.family
            phone = caretaker_form.cleaned_data['phone_number']
            relation = caretaker_form.cleaned_data['relation']
            caretaker = CareTaker.objects.create(user=user, family=family, phone_number=phone, relation=relation)
            return HttpResponseRedirect('/MBF/')

        return render(request, 'MBF/create_caretaker.html', {'caretaker_form': caretaker_form,
                                                             'user_form': user_form})

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
               'source': BottleFed.objects.filter(baby__id=baby_id).order_by('-event_time')[0:20]},
              'terms': [
                'event_time',
                'amount']}
             ])
    def dt_convert(dt_object):
        local_tz = pytz.timezone('America/Chicago')
        local_dt = dt_object.replace(tzinfo=pytz.utc).astimezone(local_tz)
        return local_dt.strftime('%a %I:%M %p')
        # return dt_object.strftime('%a %b %d')

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
    return render(request, 'MBF/chart.html',{'chart': cht})
