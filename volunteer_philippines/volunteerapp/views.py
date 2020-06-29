from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    context = {
        'message': 'home page'
    }
    return render(request, 'volunteerapp/home.html', context)

def news(request):
    context = {
        'message': 'news page'
    }
    return render(request, 'volunteerapp/news.html', context)

