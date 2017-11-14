from django import forms
from allauth.account.forms import SignupForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit,Field,Div
from crispy_forms.bootstrap import FormActions
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.forms import TextInput

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomSignUpForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super(CustomSignUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'signup_form'
        self.helper.form_class = 'signup'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('thankyou')

        # and then the rest as usual:
        self.helper.form_show_labels = False
        self.helper.add_input(Submit('signup', 'Sign Up'))
