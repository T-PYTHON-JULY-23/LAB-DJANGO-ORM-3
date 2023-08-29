from django.db import models

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    CATEGORY_CHOICES = (
        ('Technology', 'Technology'),
        ('Fashion', 'Fashion'),
        ('Travel', 'Travel'),
        ('Food', 'Food'),
        ('Sports', 'Sports'),
    )

    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='post_images/', default="post_images/default.jpg")
    publish_date = models.DateTimeField(auto_now_add=True)
    comments = models.ManyToManyField(Comment, related_name='post_comments')

    def __str__(self):
        return self.title