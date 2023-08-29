from django.db import models

# Create your models here.

class Post(models.Model):

    category_choices = (("Lifestyle", "Lifestyle Blog"), ("Sports", "Sports Blog"),("Music", "Music Blog"),("Travel", "Music Blog"),)
    title = models.CharField(max_length=2044)
    content = models.TextField()
    category = models.CharField(max_length=2044, choices=category_choices)
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    publish_date = models.DateTimeField()
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.CharField(max_length=512)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)