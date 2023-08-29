from django.db import models

# Create your models here.


class NewBlog(models.Model):
    category_choices = (("Business blog", "Business blog"), ("beauty blog", "beauty blog"), ("travel blog", "travel blog"), ("music blog", "music blog"), ("Fashion blogs", "Fashion blogs"))

    title = models.CharField(max_length=2048)
    content = models.TextField()
    category = models.CharField(max_length=2048, choices=category_choices)
    publish_date = models.DateTimeField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")


class Comment(models.Model):

    new = models.ForeignKey(NewBlog, on_delete=models.CASCADE)
    name = models.CharField(max_length=512)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)