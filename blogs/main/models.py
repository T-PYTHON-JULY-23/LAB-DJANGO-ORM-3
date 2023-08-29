from django.db import models

# Create your models here.

class Blog(models.Model):
    Bootcamps_ch = (("python" , "python"),("java" , "java"),("Data saince" , "Data saince"),("aws" , "aws"),)

    title= models.CharField(max_length=15)
    Content=models.TextField()
    publish_date = models.DateField()
    Bootcamp = models.CharField(max_length=128 , choices = Bootcamps_ch)
    image = models.ImageField(upload_to="images/", default="images/default.jpg")

class Comment(models.Model):

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=512)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

