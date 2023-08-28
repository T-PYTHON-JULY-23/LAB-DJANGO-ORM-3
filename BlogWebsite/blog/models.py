from django.db import models


# Create your models here.

class Blog(models.Model):

    category_choices=(("food","food"),("health","health"),("care and beauty","care and beauty"),("fitness","fitness"))

    title = models.CharField(max_length=2048,null=True)
    Content = models.TextField()
    category = models.TextField(max_length=128 ,choices=category_choices)
    image = models.ImageField(upload_to="images/", default="images/default.jpeg")
    publish_date = models.DateField()



class Comment(models.Model):

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=512)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    
    
  
    




