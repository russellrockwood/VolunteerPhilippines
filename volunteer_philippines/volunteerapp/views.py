from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Organization, Post, ReturnOnInvestment
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



@login_required
def add_organization(request):
    

    if request.method == 'POST':
        organization_name = request.POST["organization_name"]
        organization_url = request.POST["organization_url"]
        organization_description = request.POST["organization_description"]
        organization_image = request.FILES.get("organization_image")
        
        organization = Organization(name = organization_name,
                                    picture = organization_image,
                                    description = organization_description,
                                    org_link = organization_url,)

        organization.save()
        return HttpResponseRedirect(reverse('volunteerapp:home'))
    

    return render(request, 'volunteerapp/add_organization.html')




def news(request):
    posts = Post.objects.all()
    
    context = {
        'posts': posts
    }
    return render(request, 'volunteerapp/news.html', context)




def roi(request):
    investment_models = ReturnOnInvestment.objects.all()
    # print(investment_models)

    # print(request.POST)
    
    if request.method == 'POST':
        selected_project = request.POST['projects']
        dollar_amount = int(request.POST['dollar_amount'])
       
        
        selected_roi = ReturnOnInvestment.objects.filter(project=selected_project)

        selected_multiplier = ReturnOnInvestment.objects.get(project=selected_project)
        dis_roi = selected_multiplier.multiplier
        dis_roi *= dollar_amount

        
        context = {
            'investment_models': investment_models,
            'dollar_amount': dollar_amount,
            'selected_roi': selected_roi,
            'dis_roi': dis_roi
        }

        
    else:
        ReturnOnInvestment.objects.all()
        context = {
            'investment_models': investment_models,
        }
    return render(request, 'volunteerapp/roi.html', context)




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
        return HttpResponseRedirect(reverse('volunteerapp:home'))

    return render(request, 'volunteerapp/register.html', {'message': message})



def login_page(request):
    message = ''
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('volunteerapp:home'))
        else:
            return render(request, 'volunteerapp/login.html', {'message': 'Invalid Login'})

    return render(request, 'volunteerapp/login.html', {'message': message})

    

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('volunteerapp:login_page'))
    
