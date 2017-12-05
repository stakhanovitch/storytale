# -*- coding: utf-8 -*-
from allauth.account.views import SignupView
from public.forms.signup import CustomSignupForm

from django.urls import reverse, reverse_lazy
from public.models.workshop import Workshop
class HomePageView(SignupView):
    """
    website homepage with signup capability
    """
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context.update({'title': self.title,
                        'help_text': self.help_text,
                        'redirect_field_value': self.redirect_field_value,
                        'workshops':self.workshops})
        return context

    title = 'Créez votre compte'
    help_text = 'Veuillez rentrer les informations suivantes pour créer votre compte.'
    workshops = Workshop.objects.all()

    redirect_field_value = reverse_lazy('emailverification')

    form = CustomSignupForm
    template_name = "public/home.html"
