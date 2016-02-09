from django.shortcuts import render
#from django.http import HttpResponse
from .models import Subject
# Create your views here.
def profile(request):
	profileData = Subject.objects.all()
	return render(request,'profile.html',{'profileData':profileData})