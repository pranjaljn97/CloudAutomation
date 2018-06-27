"""youngcombat URL Configuration

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
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url('', include('social_django.urls', namespace='social')),
    #url(r'^home/', views.home, name='home'),
    url(r'^$', TemplateView.as_view(template_name='youngcombat/index.html'), name='index'),
    url(r'^login/$', auth_views.login, {'template_name': 'youngcombat/login1.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'youngcombat/logged_out.html'}, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^error/',views.error, name='error'),
    #url(r'^test/', views.dashboard, name='dashboard'),
    url('^dashboard/',include('dashboard.urls')),
]
