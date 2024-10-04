from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at=models.DateTimeField(auto_now_add=False)
    updated_at=models.DateTimeField(auto_now=True)


