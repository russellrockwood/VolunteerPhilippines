from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Organization, Post
from django.contrib.auth.models import User


def home(request):
    organizations = Organization.objects.all()
    

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
    message = 'Profile Created'
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        retype_password = request.POST['retype_password']
        if password != retype_password:
            message = 'Passwords Do Not Match'
            return render(request, 'volunteerapp/register.html', {'message': message})
        if User.objects.filter(username=username).exists():
            message = 'That Username Already Exists'
            return render(request, 'volunteerapp/register.html', {'message': message})
        user = User.objects.create_user(username, email, password)


    return render(request, 'volunteerapp/register.html', {'message': message})



def login_page(request):
    context = {
        'message': 'login page'
    }
    return render(request, 'volunteerapp/login.html', context)
