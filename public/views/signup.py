# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from django.http import HttpResponse, JsonResponse

from django.contrib.auth.mixins import LoginRequiredMixin

from allauth.account.views import SignupView, RedirectAuthenticatedUserMixin
from public.forms.signup import CustomSignupForm

# Create your views here.
class CustomSignupView(SignupView):
    """
    Custom signup view from Allauth
    """
    def get_context_data(self, **kwargs):
        context = super(CustomSignupView, self).get_context_data(**kwargs)
        context.update({'title': self.title, 'help_text': self.help_text, 'redirect_field_value': self.redirect_field_value})
        return context

    title = 'Créez votre compte'
    help_text = 'Veuillez rentrer les informations suivantes pour créer votre compte.'
    redirect_field_value = reverse_lazy('emailverification')

    form = CustomSignupForm
    template_name = "allauth-custom/signup.html"
