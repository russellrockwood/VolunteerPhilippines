from django.contrib import admin
from .models import Post, Organization, ReturnOnInvestment

admin.site.register(Post)
admin.site.register(Organization)
admin.site.register(ReturnOnInvestment)
