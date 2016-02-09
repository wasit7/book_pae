from django.http import HttpResponse
from datetime import datetime
def home(request):
	now = datetime.now()
	html = "<html><body>It is now %s.</body></home>" % now
	return HttpResponse(html)