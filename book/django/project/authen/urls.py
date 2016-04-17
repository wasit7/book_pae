from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^login/$', views.login, name='login'),
	url(r'^logout/$', views.logout, name='logout'),
	#url(r'^index/$', views.index, name='index'),
	#url(r'^home/$', views.home, name='home'),
	url(r'^registration/$', views.registration, name='registration'),
]