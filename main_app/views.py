from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. view function 
def home(request):
    # Send a simple HTML response
    # each view function or view receives a request obj 
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
    contact_details = 'you can reach supports at support@cat.com'
    return render(request, 'about.html', {
        'contact':contact_details
    })
# this 'contact': is a context dict