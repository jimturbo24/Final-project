from django import forms

class CreateUserForm(forms.Form):
    user_name = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=100)
