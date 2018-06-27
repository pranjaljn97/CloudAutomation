from django.conf.urls import url,include
from . import views

urlpatterns = [
	url(r'^$', views.dashboard, name='dashboard'),
	url(r'^userprofile/', views.user, name='userprofile'),
	url(r'^java/', views.javaform, name='javaform'),
    url(r'^drupal/', views.drupalform, name='drupalform'),
    url(r'^node/', views.nodeform, name='nodeform'),
    url(r'^test/', views.userdata, name='userdata'),
    url(r'^cprovider/', views.cloudprovider, name='cprovider'),
    url(r'^thanks/', views.thanks, name='thanks'),
]