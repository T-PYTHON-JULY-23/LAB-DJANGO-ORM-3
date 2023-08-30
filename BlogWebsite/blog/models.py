from django.db import models

# Create your models here.


class Post(models.Model):
    category_choices = (('programing language','programing language'),('DataBase','DataBase'),('artificial intelligence','artificial intelligence'),('internet of things','internet of things'))

    title = models.CharField(max_length=2048)
    content = models.TextField()
    category = models.CharField(max_length=256 , choices=category_choices)
    image_upload = models.ImageField(upload_to='images/' , default='images/default.png')
    publish_date =models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.title}"




class Comment(models.Model):

    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    name= models.CharField(max_length=512)
    content_comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name}"