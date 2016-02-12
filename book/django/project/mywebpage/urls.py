from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^addprofile/$', views.addprofile, name='addprofile'),
	url(r'^editprofile/$', views.editprofile, name='editprofile'),
	url(r'^test/$', views.test, name='test'),
	url(r'^getjson.json$', views.getjson, name='getjson'),

	url(r'^tt/$', views.tt, name='tt'),
]