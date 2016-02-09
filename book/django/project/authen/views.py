from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# Create your views here.
def login(request):
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:				
				auth_login(request, user)
                request.session['user_username'] = user.username
                return redirect('home') 
            #else:
            	#state = "Disable account"
        else:
        	state = "Invalid login"
        return render(request,'login.html',{'state':state})
 	return	render(request,'login.html',{'state':"Please login"})


def logout(request):
	if request.POST:
		if 'user_username' in request.session:
			del request.session['user_username']				#delete user_username left from sesstion
		auth_logout(request)
	return render(request,'login.html',{'state':"Please login"})

def home(request):
	if 'user_username' in request.session:
		uname = request.session['user_username']
	else:
		uname = "Anonymous"
	return render(request,'home.html',{'state':"Hello %s"%uname})	


"""from django.http import HttpResponse
def index(request):
	return HttpResponse("Hello World!")"""

