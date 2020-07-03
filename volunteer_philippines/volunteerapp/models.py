from django.db import models
from django.utils import timezone



# class User(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50) 
#     email = models.CharField(max_length=50)
#     birthday = models.DateField()  
#     password = models.CharField(max_length=10)    

#     def __str__(self):
#         return self.first_name + ' ' + self.last_name



class Post(models.Model):
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='images/', max_length=150,)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title 



class Organization(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='images/', max_length=150,)
    description = models.TextField()
    org_link = models.URLField(max_length = 200)
    def __str__(self):
        return self.name


                                    