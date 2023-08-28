from django.db import models

class Post(models.Model):

    title = models.CharField(max_length=2048)
    content = models.TextField()
    category = models.CharField(max_length=2048)
    publish_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/", default="images/default.jpg")

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=512)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)