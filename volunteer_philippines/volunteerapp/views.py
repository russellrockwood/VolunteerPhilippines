from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Organization, Post
from django.contrib.auth.forms import UserCreationForm


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
        'form': 'form'
    }


    return render(request, 'volunteerapp/register.html', context)



def login_page(request):
    context = {
        'message': 'login page'
    }
    return render(request, 'volunteerapp/login.html', context)
