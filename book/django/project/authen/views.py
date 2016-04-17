from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.core.urlresolvers import reverse
from django.template import RequestContext

from django.shortcuts import redirect
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
	if request.POST:
		if 'username' in request.session:
			del request.session['username']				#delete user_username left from sesstion
		auth_logout(request)
	return render(request,'login.html',{'state':"Please login"})


def registration(request):
	pass
	return render(request,'registration.html')

#def home(request):
   	#return render(request,'mywebpage/homep.html',request.session['user_username'])