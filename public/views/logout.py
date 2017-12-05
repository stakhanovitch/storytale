# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from django.http import HttpResponse, JsonResponse

from django.contrib.auth.mixins import LoginRequiredMixin

from allauth.account.views import LogoutView, RedirectAuthenticatedUserMixin


# Create your views here.


class CustomLogoutView(LogoutView):
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
