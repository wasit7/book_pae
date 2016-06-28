from django.shortcuts import render, render_to_response, HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.models import User
from django.shortcuts import redirect
import sys, json
from mywebpage.models import Student, Enrollment, Subject

# Create your views here.
def login(request):
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)  #verify (check username&password against a database of users)
		if user is not None:
			if user.is_active:				
				auth_login(request, user)
				request.session['username'] = username
				return redirect(reverse('home'))
				#return render_to_response('registration.html',context_instance = RequestContext(request))
			else:
				state = "Disable account"
		else:
			state = "Invalid login"
		return render(request,'login.html',{'state':state})
	return	render(request,'login.html',{'state':"Please login"})

def logout(request):
    if request.method == 'GET':
        if 'username' in request.session:
            del request.session['username']             #delete user_username left from sesstion
        auth_logout(request)
    #print request.session['username']
    return HttpResponse("OK")


def registration(request):
	if request.method == 'GET':
		return render(request,'registration.html')
	if request.method == 'POST':
		user = json.loads(request.body)
		uname = user['uname']
		password = user['password']
		cfpassword = user['cfpassword']
		if password == cfpassword:
			#print >> sys.stderr, user
			if not User.objects.filter(username=uname).exists():
				createUser = User.objects.create_user(username= uname, password= password)
				createUser.save()
				return HttpResponse("Create Account Successfully")
			elif User.objects.filter(username=uname).exists():
				return HttpResponse("User is exist")
		else:
			return HttpResponse("Password is not valid")


def pleaselogin(request):
	return render(request,'pleaselogin.html')