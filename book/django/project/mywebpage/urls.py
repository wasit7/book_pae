from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^showprofile/$', views.showprofile, name='showprofile'),
	url(r'^homep/$', views.homep, name='home'),
	url(r'^addprofile/$', views.addprofile, name='addprofile'),
	url(r'^editprofile/$', views.editprofile, name='editprofile'),
	url(r'^predict/$', views.predict, name='predict'),
	url(r'^test/$', views.test, name='test'),
	url(r'^jsonSubject.json$', views.jsonSubject, name='jsonSubject'),  #get data
	url(r'^jsonEnrollment.json$', views.jsonEnrollment, name='jsonEnrollment'),
	url(r'^coordinate.json$', views.coordinate, name='coordinate'),
	#url(r'^update/$', views.update, name='update'),
]