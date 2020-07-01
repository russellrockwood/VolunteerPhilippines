from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Organization, Post, User


def home(request):
    organizations = Organization.objects.all()
    print(organizations)

    context = {
        'organizations': organizations
        
    }
    return render(request, 'volunteerapp/home.html', context)




def news(request):
    context = {
        'message': 'news page'
    }
    return render(request, 'volunteerapp/news.html', context)

def register(request):
    context = {
        'message': 'register page'
    }
    return render(request, 'volunteerapp/register.html', context)

def login(request):
    context = {
        'message': 'login page'
    }
    return render(request, 'volunteerapp/login.html', context)
