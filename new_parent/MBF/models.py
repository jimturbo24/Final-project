from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class CareTaker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    family = models.ForeignKey('Family')
    phone_number = PhoneNumberField()
    parent = 'PA'
    family = 'FA'
    friend = 'FR'
    nanny = 'NA'
    relation_choices = (
            (parent, 'Parent'),
            (family, 'Family'),
            (friend, 'Friend'),
            (nanny, 'Nanny'))
    relation = models.CharField(max_length=2,
                                choices=relation_choices,
                                default=parent)

    # def __str__(self):
    #     return self.user

class Family(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Baby(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
