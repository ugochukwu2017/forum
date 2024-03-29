"""bobos_booboos URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import views

urlpatterns = [
    url(r'^administrator/', admin.site.urls),
    url(r'', include('booz.urls')),
    url(r'^login/$', views.login, {'template_name': 'login.html'},
        name='booz_login'),
    url(r'^logout/$', views.logout,
        {'next_page': reverse_lazy('booz_list')}, name='booz_logout'),
]
