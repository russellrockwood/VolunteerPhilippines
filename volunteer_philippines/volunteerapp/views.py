from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Organization, Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse



def home(request):
    organizations = Organization.objects.all()
    

    context = {
        'organizations': organizations
        
    }
    return render(request, 'volunteerapp/home.html', context)




def news(request):
    posts = Post.objects.all()
    
    context = {
        'posts': posts
    }
    return render(request, 'volunteerapp/news.html', context)



def register(request):
    message = ''
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
        login(request, user)
        return HttpResponseRedirect(reverse('volunteerapp:news'))

    return render(request, 'volunteerapp/register.html', {'message': message})



def login_page(request):
    message = ''
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('volunteerapp:news'))
        else:
            return render(request, 'volunteerapp/login.html', {'message': 'Invalid Login'})

    return render(request, 'volunteerapp/login.html', {'message': message})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('volunteerapp:login_page'))
    
