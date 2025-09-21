from django.db import models

# Create your models here

class SocialPost(models.Model):
    platform = models.CharField(max_length=50)
    post_id = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
