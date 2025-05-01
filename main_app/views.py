from django.shortcuts import render
from .models import Cat

# Create your views here. view function 
def home(request):
    # Send a simple HTML response
    # each view function or view receives a request obj 
    return render(request, 'home.html')

def about(request):
    contact_details = 'you can reach supports at support@cat.com'
    return render(request, 'about.html', {
        'contact':contact_details
    })
# this 'contact': is a context dict


def cat_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {
        'cats': cats
    })

def cat_detail(request, cat_id):
    cat = Cat.objects.get(id = cat_id)
    return render(request, 'cats/detail.html', {
        "cat": cat 
    })