from django.shortcuts import render


# Create your views here.
def homepage(request):
    title = "Homepage"
    return render(request,'base.html',{'title': title})