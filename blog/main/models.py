from django.db import models
# Create your models here.

class Post(models.Model):

    category_choices = (("Misc", "Miscellenous"), ("Bio", "Biography"), ("Fantasy", "Fantasy"), ("Novel", "Novel"))

    title=models.CharField(max_length=256)
    content=models.TextField()
    publish_date =models.DateField()
    category = models.CharField(max_length=128, choices=category_choices)
    image = models.ImageField(upload_to="images/", default="images/Default.png")


class Comment(models.Model):

    rating_choices = ((1, "1 Star"), (2, "2 Star"), (3, "3 Star"), (4, "4 Star"), (5, "5 Star"), )

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=512)
    content = models.TextField()
    rating = models.IntegerField(choices=rating_choices)
    created_at = models.DateTimeField(auto_now_add=True)
