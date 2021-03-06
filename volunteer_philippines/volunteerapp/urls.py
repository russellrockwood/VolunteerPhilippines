from django.urls import path
from . import views

app_name = 'volunteerapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('login/', views.login_page, name='login_page'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout_user'),
    path('add/', views.add_organization, name='add_organization'),
    path('roi/', views.roi, name='roi'),

]

