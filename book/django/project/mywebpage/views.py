from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Subject, Enrollment
#from django.core import serializers
import json
# Create your views here.
def profile(request):
	#show = "Hello profile"
	return render(request,'profile')

def addprofile(request):
	subjectData = Subject.objects.all()
	enrollmentData = Enrollment.objects.all()

	grade = ['A', 'B', 'B+','C', 'C+', 'D', 'D+', 'F', 'W', 'S', 'S#']
	#grade = ['0', '1']
	return render(request,'addprofile.html',{'subjectData':subjectData, 'enrollmentData':enrollmentData, 'grade':grade})

def editprofile(request):

	return render(request,'editprofile.html')

def test(request):
	subjectData = Subject.objects.all()
	enrollmentData = Enrollment.objects.all()
	#subjects = Subject.objects.all()
	#data = serializers.serialize('json',subjectData,fields=('sub_name'))
	#js_subjects = simplejson.dumps(subjectData)
	
	grade = ['A', 'B', 'B+','C', 'C+', 'D', 'D+', 'F', 'W', 'S', 'S#','U','U#']
	return render(request,'test.html',{'subjectData':subjectData, 'enrollmentData':enrollmentData, 'grade':grade,
		})

def getjson(request):
	subjectData = Subject.objects.all()
	js_subjects = []
	for i in subjectData:
		js_subjects.append({'text':i.sub_name})
	return JsonResponse({'js_subjects':js_subjects})