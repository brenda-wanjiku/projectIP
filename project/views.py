from django.shortcuts import render,redirect
from .models import Profile, Project, Rating
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import EditProfileForm, PostProjectForm, RateProjectForm
from rest_framework.views import APIView
from .serializer import ProjectSerializer,ProfileSerializer
from rest_framework.response import Response
from .permissions import IsAuthenticated

# Create your views here.
def homepage(request):
    projects = Project.objects.all()
    return render(request,'homepage.html',{'projects': projects})



def search_results(request):
    if 'title' in request.GET and request.GET['title']:
        searched_term = request.GET.get('title')
        titles = Project.objects.filter(title__icontains=searched_term)
        print('string'*20)
        print(titles)
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


@login_required(login_url="/accounts/login/")
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



def view_project(request,id):
    project = Project.objects.get(id=id)
    ratings = Rating.objects.filter(project=project)
    
    return render(request, 'project.html', {'project': project, "ratings": ratings})


@login_required(login_url="/accounts/login/")
def rate_project(request,id):
    project = Project.objects.get(pk = id)
    current_user = request.user
    if request.method == "POST":
        form = RateProjectForm(request.POST, request.FILES)
        if form.is_valid():
            design = form.cleaned_data['design']
            usability = form.cleaned_data['usability']
            content = form.cleaned_data['content']
            rate  = Rating(design=design, usability=usability, content=content,project=project, user=current_user)
            rate.save()
            avg = rate.average()
            rate.average = avg
            rate.save()

            return redirect(view_project, id=project.id)
    else:
        form = RateProjectForm()

    return render(request, 'rating.html', {"form": form, 'project': project})

class ProfileView(APIView):
    permission_classes = (IsAuthenticated)
    def get(self,request,format = None):
        profiles =  Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)  



class ProjectView(APIView):
    permission_classes = (IsAuthenticated)
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response({"projects": serializer.data})