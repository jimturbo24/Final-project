from django import forms
from .models import CareTaker
from django.contrib.auth.models import User

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']

class CareTakerForm(forms.ModelForm):
    class Meta:
        model = CareTaker
        fields = ['phone_number', 'relation']
