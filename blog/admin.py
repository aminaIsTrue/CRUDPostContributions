from django.contrib import admin
from .models import Post, Contribution
# Register your models here.

admin.site.register(Post),
admin.site.register(Contribution)