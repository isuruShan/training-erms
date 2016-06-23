"""ermsProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ermsapp/',include('ermsapp.urls')),
    url(r'^interviewer/',include('interviewer.urls')),

#user login urls
    url(r'^accounts/login', login_view),
    url(r'^accounts/auth', auth_view),
    url(r'^accounts/invalid', invalid_view),
    url(r'^accounts/logout', logout_view),

#user registration urls
    url(r'^accounts/register', registration_view),
    url(r'^accounts/register_success', registration_success),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root= settings.STATIC_ROOT)