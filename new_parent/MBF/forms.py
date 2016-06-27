from django import forms
from .models import CareTaker, Baby, BreastFed, BottleFed, DiaperStatus, Temperature, Sleep, Wake, Family
from django.contrib.auth.models import User

class CreateUserForm(forms.ModelForm):
    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']

class CareTakerForm(forms.ModelForm):
    class Meta:
        model = CareTaker
        fields = ['phone_number', 'relation']
        labels = {
            'phone_number': ''
        }
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'col-lg-2'}),
        }

class CreateFamilyForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = ['name']

class BabyForm(forms.ModelForm):
    class Meta:
        model = Baby
        fields = ['first_name', 'last_name', 'birth_date', 'family']

class BreastFedForm(forms.ModelForm):
    class Meta:
        model = BreastFed
        fields = {'breast'}

class BottleFedForm(forms.ModelForm):
    class Meta:
        model = BottleFed
        fields = {'amount'}

class DiaperStatusForm(forms.ModelForm):
    class Meta:
        model = DiaperStatus
        fields = {'diaper'}

class TemperatureForm(forms.ModelForm):
    class Meta:
        model = Temperature
        fields = {'temp'}

class SleepForm(forms.ModelForm):
    class Meta:
        model = Sleep
        fields = {'sleep_status'}

class WakeForm(forms.ModelForm):
    class Meta:
        model = Wake
        fields = {'wake_status'}
