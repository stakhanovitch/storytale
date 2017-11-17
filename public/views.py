# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.base import TemplateView

from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from django.http import HttpResponse, JsonResponse
from models import Subscribe
from utils import SendSubscribeMail

from django.contrib.auth.mixins import LoginRequiredMixin


from allauth.account.views import SignupView, LoginView, LogoutView, RedirectAuthenticatedUserMixin
from public.forms import CustomSignUpForm,CustomLoginForm

# Create your views here.

def redirect_page_not_found(request):
  return render_to_response('template/404.html', {}, context_instance=RequestContext(request));

def redirect_500_error(request):
  return render_to_response('template/500.html', {}, context_instance=RequestContext(request));

class HomePageView(SignupView):
    """
    website homepage with signup capability
    """
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context.update({'title': self.title, 'help_text': self.help_text,'redirect_field_value': self.redirect_field_value})
        return context

    title = 'Créez votre compte'
    help_text = 'Veuillez rentrer les informations suivantes pour créer votre compte.'
    redirect_field_value = reverse_lazy('emailverification')

    form = CustomSignUpForm
    template_name = "home.html"

class CustomSignUp(SignupView):
    """
    Custom signup view from Allauth
    """
    def get_context_data(self, **kwargs):
        context = super(CustomSignUp, self).get_context_data(**kwargs)
        context.update({'title': self.title, 'help_text': self.help_text, 'redirect_field_value': self.redirect_field_value})
        return context

    title = 'Créez votre compte'
    help_text = 'Veuillez rentrer les informations suivantes pour créer votre compte.'
    redirect_field_value = reverse_lazy('emailverification')

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
