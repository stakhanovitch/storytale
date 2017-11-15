# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.base import TemplateView
from allauth.account.views import SignupView, LoginView, LogoutView
from public.forms import CustomSignUpForm,CustomLoginForm
from django.shortcuts import render
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from models import Subscribe
from utils import SendSubscribeMail

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.




class HomePageView(SignupView):
    """
    website homepage with signup capability
    """
    template_name = "home.html"

class CustomSignUp(SignupView):
    """
    Custom signup view from Allauth
    """
    def get_context_data(self, **kwargs):
        context = super(CustomSignUp, self).get_context_data(**kwargs)
        context.update({'title': self.title, 'help_text': self.help_text})
        return context

    title = 'Créez votre compte'
    help_text = 'Veuillez rentrer les informations suivantes pour créer votre compte.'

    form = CustomSignUpForm
    template_name = "allauth-custom/signup.html"

class CustomLogin(LoginView):
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

class CustomLogout(LogoutView):
    """
    Custom login view from Allauth
    """
    def get_context_data(self, **kwargs):
        context = super(CustomLogout, self).get_context_data(**kwargs)
        context.update({'title': self.title, 'help_text': self.help_text})
        return context

    title = 'Déconnexion'
    help_text = 'Etes-vous sûr de vouloir vous déconnecter ?'
    template_name = "allauth-custom/logout.html"

class ThankYouView(LoginRequiredMixin,SignupView):
    """
    landing page after registration
    """
    template_name = "thankyou.html"
