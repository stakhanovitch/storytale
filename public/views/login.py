# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from django.http import HttpResponse, JsonResponse

from django.contrib.auth.mixins import LoginRequiredMixin

from allauth.account.views import LoginView, RedirectAuthenticatedUserMixin
from public.forms.login import CustomLoginForm

# Create your views here.
class CustomLoginView(LoginView):
    """
    Custom login view from Allauth
    """
    def get_context_data(self, **kwargs):
        context = super(CustomLogin, self).get_context_data(**kwargs)
        context.update({'title': self.title, 'help_text': self.help_text})
        return context

    title = 'Connectez-vous'
    help_text = 'Veuillez rentrer votre login et votre mot de passe pour vous connecter.'

    form = CustomLoginForm
    template_name = "allauth-custom/login.html"
