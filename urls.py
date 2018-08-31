"""storytale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import public
from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from allauth.account.views import EmailVerificationSentView
from public.views.home import HomePageView
from public.views.thankyou import ThankYouView

from public.views.signup import CustomSignupView
from public.views.login import CustomLoginView
from public.views.logout import CustomLogoutView
urlpatterns = [
    url(r'^$',  HomePageView.as_view(), name='home'),
    url(r'^sign-up$', CustomSignupView.as_view(), name='signup'),
    url(r'^log-in$', CustomLoginView.as_view(), name='login'),
    url(r'^log-out$', CustomLogoutView.as_view(), name='logout'),
    url(r'^email-verification$', EmailVerificationSentView.as_view(), name='emailverification'),
    url(r'^thank-you$', ThankYouView.as_view(), name='thankyou'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/mailchimp/', include('mailchimp.urls')),
     #url(r'^contact/$', public.views.contact, name='contact'),
     url(r'^ateliers/', include('public.urls')),
     ]


urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

#  06/11 commit : No need for media right now
#static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
