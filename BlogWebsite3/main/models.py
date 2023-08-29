from django.db import models

# Create your models here.


# Create your models here.
class Post(models.Model):
    CATEGORY_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('dinner', 'Dinner'),
        ('lunch', 'Lunch'),
        ('snacks', 'Snacks'),
    ]

    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to="images/",  default="images/Chi.jpg ")
    publish_date = models.DateTimeField()

    def __str__(self):
        return self.title
    

class Comment(models.Model):

    rating_choices = ((1, "1 Star"), (2, "2 Star"), (3, "3 Star"), (4, "4 Star"), (5, "5 Star"), )

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=512)
    content = models.TextField()
    rating = models.IntegerField(choices=rating_choices)
    created_at = models.DateTimeField(auto_now_add=True)