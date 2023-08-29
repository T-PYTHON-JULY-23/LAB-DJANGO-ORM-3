from django.db import models

# Create your models here.


class Blog(models.Model):
    category_choices=(("IT","IT"),("Physics","Physics"),("Chemistry","Chemistry"),("Medicine","Medicine"))
    title = models.CharField(max_length=2067)
    content = models.TextField()
    category = models.CharField(max_length=140,choices=category_choices)
    image = models.ImageField(upload_to="img/",default="img/default.jpg")
    publish_date = models.DateTimeField()


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=600)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)