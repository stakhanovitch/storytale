# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.base import TemplateView

from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from django.http import HttpResponse, JsonResponse

from django.contrib.auth.mixins import LoginRequiredMixin

from allauth.account.views import SignupView,  RedirectAuthenticatedUserMixin


# Create your views here.


class ThankYouView(LoginRequiredMixin,SignupView):
    """
    landing page after registration
    """
    template_name = "thankyou.html"
