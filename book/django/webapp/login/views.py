from django.shortcuts import render

# Create your views here.
#print("book")

from django.http import HttpResponse
def myfunction(request):
    #return HttpResponse("Hello World!")
    html = """<html>
<body>

<form>
First name:<br>
<input type="text" name="firstname">
<br>
Last name:<br>
<input type="text" name="lastname">
</form>

<p>Note that the form itself is not visible.</p>

<p>Also note that the default width of a text field is 20 characters.</p>

</body>
</html>"""

    return HttpResponse(html)
