# -*- coding: utf-8 -*-

from django import forms
from allauth.account.forms import SignupForm, LoginForm


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Field, Div, HTML
from crispy_forms.bootstrap import FormActions
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.forms import TextInput

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.utils.translation import pgettext, ugettext, ugettext_lazy as _

class CustomSignupForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        self.helper.layout.append(
            HTML(
                "{% if redirect_field_value %}"
                "<input type='hidden' name='{{ redirect_field_name }}'"
                " value='{{ redirect_field_value }}' />"
                "{% endif %}"
                )
        )

        self.helper.form_id = 'signup_form'
        self.helper.form_class = 'signup'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('signup')

        # and then the rest as usual:

        self.helper.form_show_labels = False
        self.helper.add_input(Submit('Créer mon compte', 'Créer mon compte'))
