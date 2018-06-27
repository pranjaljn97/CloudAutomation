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
    url(r'^forapproval/', views.forapproval, name='forapproval'),
    url(r'^forapproval1/(?P<id>[0-9]+)', views.forapproval1, name='forapproval1'),
    url(r'^forapproval2/(?P<id>[0-9]+)', views.forapproval2, name='forapproval2'),
    url(r'^approved/', views.approved, name='approved'),
    url(r'^rejected/', views.rejected, name='rejected'),
    url(r'^detailform/?(?P<id>[0-9]+)', views.detailform, name='detailform'),
]