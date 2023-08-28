from django.db import models


# Create your models here.

class Post(models.Model):
    category_choices = (("Fashion", "Fashion"), ("Business", "Business"), ("Photography", "Photography"), ("Food", "Food"))

    title = models.CharField(max_length=2048)
    category = models.CharField(max_length=256)
    content = models.TextField()
    publish_date = models.DateTimeField()
    image= models.ImageField(upload_to="images/",default="null")

class Comment(models.Model):

     rating_choices = ((1, "1 Star"), (2, "2 Star"), (3, "3 Star"), (4, "4 Star"), (5, "5 Star"), )

     post = models.ForeignKey(Post, on_delete=models.CASCADE)
     name = models.CharField(max_length=512)
     content = models.TextField()
     rating = models.IntegerField(choices=rating_choices)
     created_at = models.DateTimeField(auto_now_add=True)
