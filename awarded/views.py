from django.http import request
from django.shortcuts import render, redirect

# Create your views here.


def index(request):
	return render(request,'index.html',)


def dir(request):
    return render(request,'dir.html',)