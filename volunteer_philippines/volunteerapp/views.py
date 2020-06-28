from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'message': 'whats up'
    }
    return render(request, 'volunteerapp/index.html', context)


