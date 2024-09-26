from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    author = models.ManyToManyField(User)

    def __str__(self):
        return self.title


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey('main_app.Comment', null=True, blank=True, on_delete=models.DO_NOTHING,
                                related_name='comments')

    def __str__(self):
        return self.content


class Post(models.Model):
    slug = models.SlugField(null=True, unique=True)
    title = models.CharField(max_length=300)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    topic = models.ManyToManyField(Topic)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    prepopulated_fields = {'slug': ('title',)}

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     return super().save(*args, **kwargs)

    def save(self,  *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)
