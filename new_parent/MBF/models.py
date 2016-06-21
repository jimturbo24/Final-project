from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Family(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class CareTaker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    family = models.ForeignKey(Family, on_delete=models.SET_NULL, null=True)
    phone_number = PhoneNumberField()
    relation_choices = (('PA', 'Parent'),
                        ('FA', 'Family'),
                        ('FR', 'Friend'),
                        ('NA', 'Nanny'))
    relation = models.CharField(max_length=2,
                                choices=relation_choices,
                                default='PA')

    def __str__(self):
        return str(self.user)

class Baby(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    family = models.ForeignKey(Family, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.first_name

    def get_breast_events(self):
        eventList = BreastFed.objects.filter(baby=self).order_by('-event_time')[0:3]
        return eventList
    def get_bottle_events(self):
        eventList = BottleFed.objects.filter(baby=self).order_by('-event_time')[0:3]
        return eventList
    def get_temperature_events(self):
        eventList = Temperature.objects.filter(baby=self).order_by('-event_time')[0:3]
        return eventList
    def get_sleep_events(self):
        eventList = Sleep.objects.filter(baby=self).order_by('-event_time')[0:3]
        return eventList
    def get_wake_events(self):
        eventList = Wake.objects.filter(baby=self).order_by('-event_time')[0:3]
        return eventList
    def get_diaper_events(self):
        eventList = DiaperStatus.objects.filter(baby=self).order_by('-event_time')[0:3]
        return eventList


class BabyEvent(models.Model):
    event_time = models.DateTimeField(auto_now_add=True)
    baby = models.ForeignKey(Baby, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.event_time)

class BreastFed(BabyEvent):
    breast_choice = (('left', 'Left'),
                     ('right', 'Right'))
    breast = models.CharField(max_length=5,
                              choices=breast_choice,
                              default='left')

    def __str__(self):
        return str(self.event_time)

class BottleFed(BabyEvent):
    amount = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.amount)

class DiaperStatus(BabyEvent):
    diaper_choice = (('poo', 'Poo'),
                     ('pee', 'Pee'),
                     ('poo & pee', 'Poo & Pee'))
    diaper = models.CharField(max_length=9,
                              choices=diaper_choice,
                              default='pee')

class Temperature(BabyEvent):
    temp_choice = (('normal', 'Normal'),
                   ('warm', 'Warm'),
                   ('hot', 'Hot'))
    temp = models.CharField(max_length=6,
                              choices=temp_choice,
                              default='normal')

class Sleep(BabyEvent):
    nap = 'NP'
    night = 'NT'
    sleep_choice = ((nap, 'Nap'),
                    (night, 'Night'))
    sleep_status = models.CharField(max_length=2,
                              choices=sleep_choice,
                              default=night)

class Wake(BabyEvent):
    # sleep_event = models.OneToOneField(Sleep, on_delete=models.CASCADE)
    nap = 'NP'
    night = 'NT'
    wake_choice = ((nap, 'Nap'),
                   (night, 'Night'))
    wake_status = models.CharField(max_length=2,
                              choices=wake_choice,
                              default=night)
