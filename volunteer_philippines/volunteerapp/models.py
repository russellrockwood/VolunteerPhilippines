from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    picture = models.ImageField()
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title 


class Organization(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField()
    description = models.TextField()
    org_link = models.URLField(max_length = 200)
    def __str__(self):
        return self.title
                                                    