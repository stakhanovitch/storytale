from django.views.generic.detail import DetailView
from public.models.workshop import Workshop
from public.models.userworkshopregistration import UserWorkshopRegistration

from public.forms.workshopregistration.register import UserWorkshopRegistrationForm
from public.forms.signup import CustomSignupForm

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy,reverse


class WorkshopRegistrationView(CreateView):
    template_name = "public/workshops/registration.html"
    #form_class = UserWorkshopRegistrationForm

    def get_form_class(self):
        if self.request.user:
            form_class = UserWorkshopRegistrationForm
        else:
            form_class = CustomSignupForm
        return form_class
        self.fail('message')
    def get_context_data(self, **kwargs):
        context = super(WorkshopRegistrationView, self).get_context_data(**kwargs)
        context.update({'workshop': Workshop.objects.get(slug = self.kwargs['slug']),})
        return context

    def get_success_url(self):
        return reverse('workshopregistration',args=(self.object.workshop.slug,))
        #success_url = self.object.workshop.get_absolute_url()

    def get_form_kwargs(self):
        kwargs = super(WorkshopRegistrationView, self).get_form_kwargs()
        kwargs['user'] = self.request.user # pass the 'user' in kwargs

        try:
            kwargs['workshop'] = Workshop.objects.get(slug = self.kwargs['slug'])
        except Exception as e:
            pass
        return kwargs
