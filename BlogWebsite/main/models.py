from django.db import models

# Create your models here.

class BlogWebsite(models.Model):

    Categorys = [
    ('FASHION','Fashion'),
    ('BEAUTY','Beauty'),
    ('TRAVEL','Travel'),
    ('PERSONAL', 'Personal'),
    ('TECH','Tech'),
    ('HEALTH','Health'),
    ('HOME','Home'),
    ('FITNESS','Fitness'),
    ('EDUCATION','Education'),
    ('FOOD','Food'),
    ('ENTERTAINMENT','Entertainment')
]
    
    title = models.CharField(max_length=512)  
    content = models.TextField()
    category = models.CharField(max_length=512, choices= Categorys,default="blog") 
    image = models.ImageField(upload_to="images/", default="images/logo.png")
    publish_date = models.DateField() 



class Comment(models.Model):
    blog = models.ForeignKey(BlogWebsite, on_delete=models.CASCADE,default=None)
    name = models.CharField(max_length=512)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)