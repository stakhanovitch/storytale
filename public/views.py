# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.base import TemplateView
from allauth.account.views import SignupView
from public.forms import CustomSignUpForm
from django.shortcuts import render
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from models import Subscribe
from utils import SendSubscribeMail


# Create your views here.

class HomePageView(SignupView):
    """
    website homepage with signup capability
    """
    template_name = "home.html"

class ThankYouView(SignupView):
    """
    landing page after registration
    """
    template_name = "thankyou.html"

class CustomSignUp(SignupView):
    """
    Custom signup view from Allauth
    """
    form = CustomSignUpForm
    template_name = "allauth-custom/signup.html"
