from django.conf.urls import url,include
from . import views

urlpatterns = [
	url(r'^$', views.dashboard, name='dashboard'),
	url(r'^userprofile/', views.user, name='userprofile'),
	url(r'^java/', views.javaform, name='javaform'),
    url(r'^drupal/', views.drupalform, name='drupalform'),
    url(r'^node/', views.nodeform, name='nodeform'),
    url(r'^test/', views.userdata, name='userdata'),
    url(r'^cprovider/', views.cprovider, name='cprovider'),
    url(r'^thanks/', views.thanks, name='thanks'),
    url(r'^forapproval/', views.forapproval, name='forapproval'),
    url(r'^approvedsuccessfully/(?P<id>[0-9]+)', views.approvedsuccessfully, name='approvedsuccessfully'),
    url(r'^rejectedsuccessfully/(?P<id>[0-9]+)', views.rejectedsuccessfully, name='rejectedsuccessfully'),
    url(r'^approved/', views.approved, name='approved'),
    url(r'^rejected/', views.rejected, name='rejected'),
    url(r'^detailform/?(?P<id>[0-9]+)', views.detailform, name='detailform'),
    url(r'^hostdetailform/?(?P<id>[0-9]+)', views.hostdetailform, name='hostdetailform'),
    url(r'^submitted/(?P<requester>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',views.submitted, name='submitted'),
    url(r'^finalmail/?(?P<id>[0-9]+)', views.finalmail, name='finalmail'),
    url(r'^hostadded/(?P<id>[0-9]+)', views.hostadded, name='hostadded'),
    url(r'^rstackview/', views.rstackview, name='rstackview'),
    url(r'^checkstatus/(?P<id>[0-9]+)', views.checkstatus, name='checkstatus'),
    url(r'^rerun/?(?P<id>[0-9]+)', views.rerun, name='rerun'),
    url(r'^mysqlform/', views.mysqlform, name='mysqlform'),
    url(r'^submittedmysql/(?P<requester>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',views.submittedmysql, name='submittedmysql'),
    url(r'^forapprovalmysql/', views.forapprovalmysql, name='forapprovalmysql'),
    url(r'^approvedmysql/', views.approvedmysql, name='approvedmysql'),
    url(r'^rejectedmysql/', views.rejectedmysql, name='rejectedmysql'),
    url(r'^rejectedsuccessfullymysql/(?P<id>[0-9]+)', views.rejectedsuccessfullymysql, name='rejectedsuccessfullymysql'),
    url(r'^approvedsuccessfullymysql/(?P<id>[0-9]+)', views.approvedsuccessfullymysql, name='approvedsuccessfullymysql'),
    url(r'^mongoformpage/', views.mongoformpage, name='mongoformpage'),
    url(r'^submittedmongo/(?P<requester>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',views.submittedmongo, name='submittedmongo'),
    url(r'^forapprovalmongo/', views.forapprovalmongo, name='forapprovalmongo'),
    url(r'^approvedmongo/', views.approvedmongo, name='approvedmongo'),
    url(r'^rejectedmongo/', views.rejectedmongo, name='rejectedmongo'),
    # url(r'^rejectedsuccessfullymongo/(?P<id>[0-9]+)', views.rejectedsuccessfullymongo, name='rejectedsuccessfullymongo'),
    url(r'^approvedsuccessfullymongo/(?P<id>[0-9]+)', views.approvedsuccessfullymongo, name='approvedsuccessfullymongo'),



]