from django.db import models

# Create your models here.

class Recipe(models.Model):

    catagory_choices=(("Apptizer","Apptizer"),("Drinks","Drinks"),("Main-dish","Main dish"))

    title = models.CharField(max_length=2048)
    content = models.TextField()
    catagory=models.CharField(max_length=128 , choices= catagory_choices)
    image = models.ImageField(upload_to="images/", default="images/my-recipes-logo.png")
    publish_date = models.DateField()


class Comment(models.Model):
    rating_choices = ((1, "1 Star"), (2, "2 Star"), (3, "3 Star"), (4, "4 Star"), (5, "5 Star") )

    recipe=models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=512)
    content = models.TextField()
    rating = models.IntegerField(choices=rating_choices)
    created_at = models.DateTimeField(auto_now_add=True)
