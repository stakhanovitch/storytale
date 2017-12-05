from django import forms
from django.forms import HiddenInput

from public.models.workshop import Workshop
from public.models.userworkshopregistration import UserWorkshopRegistration

class UserWorkshopRegistrationForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        workshop = kwargs.pop('workshop', None)
        user = kwargs.pop('user', None)
        super(UserWorkshopRegistrationForm, self).__init__(*args,**kwargs)

        self.fields['workshop'].initial = workshop.id
        self.fields['workshop'].widget = HiddenInput()
        self.fields['user'].initial = user.id
        self.fields['user'].widget = HiddenInput()

    class Meta:
        model = UserWorkshopRegistration
        fields = 'user', 'workshop',
