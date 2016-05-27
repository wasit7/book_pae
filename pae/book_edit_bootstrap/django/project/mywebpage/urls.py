from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^showprofile/$', views.showprofile, name='showprofile'),
	url(r'^home/$', views.home, name='home'),
	url(r'^homeD3/$', views.homeD3, name='homeD3'),
	url(r'^addprofile/$', views.addprofile, name='addprofile'),
	url(r'^editprofile/$', views.editprofile, name='editprofile'),
	url(r'^predict/$', views.predict, name='predict'),
	url(r'^userprofile/$', views.userprofile, name='userprofile'),
	url(r'^test/$', views.test, name='test'),
	url(r'^jsonSubject.json$', views.jsonSubject, name='jsonSubject'),  #get data
	url(r'^jsonEnrollment.json$', views.jsonEnrollment, name='jsonEnrollment'),
	url(r'^jsonStudent.json$', views.jsonStudent, name='jsonStudent'),
	url(r'^jsonProvience.json$', views.jsonProvience, name='jsonProvience'),
	url(r'^coordinate_home.json$', views.coordinate_home, name='coordinate_home'),
	url(r'^coordinate_predict.json$', views.coordinate_predict, name='coordinate_predict'),
]