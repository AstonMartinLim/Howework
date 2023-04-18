from django.db import models


# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Post(models.Model):
    slug = models.CharField(max_length=150)
    title = models.CharField(max_length=300)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)
    """
    ManyToMany connection between Topic and Post
    """
    author_topic = models.ManyToManyField(Topic)

    def __str__(self):
        return self.title


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=300)
    """
    ForeignKey connection between Post and Comment
    """
    comment = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comment')

    def __str__(self):
        return self.content


class User(models.Model):
    """
    ForeignKey connection between User and Post
    """
    author_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='author_post')
    """
    ForeignKey connection between User and Comment
    """
    author_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='author_comment')
    """
    ManyToMany connection between User and Topic
    """
    author_topic = models.ManyToManyField(Topic)


