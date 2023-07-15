from django.contrib import admin

from .models import Poll, Post, Media

admin.site.register(Post)
admin.site.register(Poll)
admin.site.register(Media)
