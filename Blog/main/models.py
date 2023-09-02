from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recpie(models.Model):
    
    title_recipes = models.CharField(max_length=2048)
    category = models.CharField(max_length=2048)
    Ingredients = models.TextField()
    Instructions = models.TextField()
    publish_date = models.DateField()
    image=models.ImageField(upload_to="images/",default="/images/drecpie.jpg")
    
    def __str__(self) -> str:
       return f"{self.title_recipes}"
   
class Comment(models.Model):
  rating_choices=((1,"1 Star"),(2,"2 Star"),(3,"3 Star"),(4,"4 Star"),(5,"5 Star"))
  
  recpie=models.ForeignKey(Recpie,on_delete=models.CASCADE)
  user=models.ForeignKey(User,on_delete=models.CASCADE)

  content=models.TextField()
  rating = models.IntegerField(choices=rating_choices)
  created_at=models.DateTimeField(auto_now_add=True)
  
  def __str__(self) -> str:
       return f"{self.name ,self.content ,self.rating}"
  
  
class Favorite(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    recpie=models.ForeignKey(Recpie,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    
    

  
