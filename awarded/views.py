from django.http import request
from django.shortcuts import render, redirect
from django.conf import settings
from django.conf.urls.static import static
from django.urls.resolvers import URLPattern

# Create your views here.


def index(request):
	return render(request,'index.html',)


def dir(request):
    return render(request,'dir.html',)


def create_profile(request):
    return render(request,'create_profile.html',)

def profile(request):
    return render(request,'profile.html',)


def new_award(request):
    return render(request,'new_award.html',)








# if settings.DEBUG:
#     URLPattern += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)