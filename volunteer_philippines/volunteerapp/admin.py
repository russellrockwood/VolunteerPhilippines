from django.contrib import admin
from .models import Post, Organization, User

admin.site.register(Post)
admin.site.register(Organization)
admin.site.register(User)
