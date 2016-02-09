from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.login, name='login'),
	url(r'^logout/$', views.logout, name='logout'),
	#url(r'^index/$', views.index, name='index'),
	url(r'^home/$', views.home, name='home'),
]