from django.conf.urls import url
from public.views.workshops.registration import WorkshopRegistrationView

urlpatterns = [
    url(r'^registration/(?P<slug>[\w-]+)$', WorkshopRegistrationView.as_view(), name ='workshopregistration' ),
]
