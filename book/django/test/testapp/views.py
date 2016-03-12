from django.shortcuts import render

# Create your views here.
def homep(request):
	return render(request, 'homep.html')