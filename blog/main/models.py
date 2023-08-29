from django.db import models

# Create your models here.
class Blog(models.Model):
    

    category_choices = (
    ("Lifestyle", "Lifestyle"),
    ("Beauty", "Beauty"),
    ("Fashion", "Fashion"),
   
)
    title=models.CharField(max_length=256)
    content=models.TextField()
    category=models.CharField(max_length=10, choices=category_choices)
    image=models.ImageField(upload_to="images/", default='images/def.webp')
    publish_date =models.DateTimeField()

class Comment(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    name=models.CharField(max_length=512)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
