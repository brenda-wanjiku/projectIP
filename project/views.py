from django.shortcuts import render,redirect
from .models import Profile, Project
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import EditProfileForm, PostProjectForm


# Create your views here.
def homepage(request):
    projects = Project.objects.all()
    return render(request,'base.html',{'projects': projects})



def search_results(request):
    if 'title' in request.GET and request.GET['title']:
        searched_term = request.GET.get('title')
        titles = Project.search_project(searched_term)
        message = f"{searched_term}"

        return render(request, 'search.html', {'message':message,'titles':titles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{'message':message})


def profile(request):
    '''
    Displays a user's profile
    '''
    current_user = request.user
    profile = Profile.objects.get(user =current_user)
    return render(request, 'profile.html', {"profile" : profile} )


def update_profile(request):
    current_user = request.user

    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile_pic = form.cleaned_data['profile_pic']
            bio  = form.cleaned_data['bio']
            contact = form.cleaned_data['contact']

            updated_profile = Profile.objects.get(user= current_user)
            updated_profile.profile_pic = profile_pic
            updated_profile.bio = bio
            updated_profile.save()
        return redirect('profile')
    else:
        form = EditProfileForm()
    return render(request, 'update_profile.html', {"form": form})



def post_project(request):
    current_user = request.user

    if request.method == "POST":
        form = PostProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = request.user
            project.save()
        return redirect('homepage')
    else:
        form = PostProjectForm()
    return render(request, 'post_project.html', {"form": form})
