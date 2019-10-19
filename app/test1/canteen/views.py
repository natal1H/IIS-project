from django.shortcuts import render
from django.views import generic

# Create your views here.



def home_view(request):
	return render(request, 'base.html',{})

def login_view(request):
	return render(request, 'base.html',{})

