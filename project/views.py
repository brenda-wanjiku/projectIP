from django.shortcuts import render
from .models import Profile, Project
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User


# Create your views here.
def homepage(request):
    title = "Homepage"
    return render(request,'base.html',{'title': title})



def search_results(request):
    if 'title' in request.GET and request.GET['title']:
        searched_term = request.GET.get('title')
        titles = Project.search_project(searched_term)
        message = f"{searched_term}"

        return render(request, 'search.html', {'message':message,'titles':titles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{'message':message})
