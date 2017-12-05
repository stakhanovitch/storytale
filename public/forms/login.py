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

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'login_form'
        self.helper.form_class = 'signup'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('login')
        # and then the rest as usual:
        self.helper.form_show_errors = True
        self.helper.form_show_labels = False
        self.helper.add_input(Submit('Connexion', 'Connexion'))

    error_messages = {
        'account_inactive':
        _("Ce compte est actuellement inactif."),

        'email_password_mismatch':
        _("Votre adresse E-mail et/ou votre mot de passe sont invalides."),

        'username_password_mismatch':
        _("Votre pseudo et/ou votre mot de passe sont invalides."),
    }
