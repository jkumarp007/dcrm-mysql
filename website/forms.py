from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


class SingUpForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='First name', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last name', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    # username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'password1', 'password2')

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(SingUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].label = 'Username'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].label = 'Confirm Password'


class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(label='First name', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last name', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    phone = forms.CharField(label='Phone', max_length=15, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    address = forms.CharField(label='Address', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    city = forms.CharField(label='City', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    state = forms.CharField(label='State', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    zipcode = forms.CharField(label='Zipcode', max_length=6, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = Record
        exclude = ('user',)
