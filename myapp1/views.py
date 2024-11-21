from django.shortcuts import render
from .models import Slider, Blog
from django.db.models import Q

# Create your views here.

def home(req):
    sliders = Slider.objects.all()
    return render(req, 'index.html', {'slider':sliders})

def search(req):
    query = req.GET.get('query')
    #name of the query is the one in the get ()
    if query:
        blogs = Blog.objects.filter(Q(title__icontains=query) | Q(author__icontains=query) | Q(description__icontains=query))
        return render(req, 'search.html',{'data': blogs,'query': query})
    return render(req, 'search.html')