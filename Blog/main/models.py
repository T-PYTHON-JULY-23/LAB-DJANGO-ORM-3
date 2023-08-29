from django.db import models

# Create your models here.

class Post(models.Model):
    CATEGORY_CHOICES = (
        ('LT', 'Literature'),
        ('IT', 'Technology'),
        ('FO', 'Food'),
        ('TR', 'Travel'),
        ('HE', 'Health'),
    )

    title = models.CharField(max_length=2048)
    content = models.TextField()
    category = models.CharField(max_length=64, choices=CATEGORY_CHOICES)
    publish_date = models.DateTimeField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")


class PostComment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=64)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

