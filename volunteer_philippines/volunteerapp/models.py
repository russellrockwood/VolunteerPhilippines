from django.db import models
from django.utils import timezone
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='images/', max_length=150,)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.title 



class Organization(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='images/', max_length=150,)
    description = models.TextField()
    org_link = models.URLField(max_length = 200)
    def __str__(self):
        return self.name

class ReturnOnInvestment(models.Model):
    project = models.CharField(max_length=250)
    multiplier = models.IntegerField(default=0)
    info = models.TextField()
    def __str__(self):
        return self.project + ' ' + self.info + ' ' +str(self.multiplier)
    
                                    