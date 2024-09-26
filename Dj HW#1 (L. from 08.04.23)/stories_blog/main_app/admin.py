from django.contrib import admin
from .models import Topic, Comment, Post, User

admin.site.register(Topic)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(User)
