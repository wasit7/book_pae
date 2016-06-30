
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.template import RequestContext


def login_user(request):
    state = "Please log in below..."
    username = password = ''                                                                #set username&password is empty string
    if request.POST:                                                                        #request method POST after click submit btn    
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)                           #authen with DB
        
        if user is not None:                                                                #find user
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"                                    #user & pass correct
            else:
                state = "Your account is not active, please contact the site admin."        #maybe username expired
        else:
            state = "Your username and/or password were incorrect."                         #user & pass incorrect

    csrfContext = RequestContext(request)   
    #return render_to_response('login.html',{'state':state, 'username': username}, csrfContext)  #called html file and sent state&username value
                                                                                                #sent csrfContext
    #return render_to_response('index.html')
    return render_to_response('login.html',{'state':state, 'username': username}, csrfContext)



    