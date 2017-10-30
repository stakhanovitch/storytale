from django import forms
from allauth.account.forms import SignupForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit,Field,Div
from crispy_forms.bootstrap import FormActions
from django.contrib.auth import get_user_model

from django.forms import TextInput

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MySignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        username = forms.CharField(label='', required=True)
        first_name = forms.CharField(max_length=30, label="", required=False, help_text='Optional.')
        last_name = forms.CharField(max_length=30, label="", required=False, help_text='Optional.')
        email = forms.EmailField(max_length=254, label="", help_text='Required. Inform a valid email address.')
        password1 = forms.CharField(max_length=254, label="", help_text='Required. Inform a valid email address.')
        password2 = forms.CharField(max_length=254, help_text='Required. Inform a valid email address.')
        widgets = {
            'username': TextInput(attrs={'placeholder':'Your username *',}),
            'first_name': TextInput(attrs={'placeholder':'Your first name (optional)'}),
            'last_name': TextInput(attrs={'placeholder':'Your last name (optional)'}),
            'email': TextInput(attrs={'placeholder':'Your email *'}),
            'password1': forms.PasswordInput(attrs={'placeholder':'enter your password *'}),
            'password2': forms.PasswordInput(attrs={'placeholder':'Your password again *'}),

        }
