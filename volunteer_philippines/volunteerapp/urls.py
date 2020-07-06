from django.urls import path
from . import views

app_name = 'volunteerapp'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('login/', views.login_page, name='login_page'),
    path('register/', views.register, name='register'),
]

