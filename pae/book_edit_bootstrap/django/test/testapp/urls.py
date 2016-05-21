from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^homep/$', views.homep, name='home'),

]