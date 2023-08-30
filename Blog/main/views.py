from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Recpie
from .models import Comment,Favorite


# Create your views here.
def home(request: HttpRequest):

    return render(request, "main/home.html")


def addRecpie(request: HttpRequest):
     
     if request.method == "POST":
        #adding a recpes
        new_recpie = Recpie(title_recipes=request.POST['title_recipes'],category=request.POST['category'],Ingredients=request.POST['Ingredients'],Instructions=request.POST['Instructions'],publish_date=request.POST['publish_date'],image=request.FILES['image'])
        new_recpie.save()
        return redirect("main:post_view")

        

     return render(request, "main/addRecipe.html")

def all_recpies(request: HttpRequest):
    
    
   
    recpies = Recpie.objects.all()
    if "search" in request.GET and "category" in request.GET:
        serech_title=request.GET['search']
        c_category=request.GET['category']
        if serech_title!='':
            recpies=Recpie.objects.filter(title_recipes__contains=serech_title)
        if c_category!='all':
            recpies=Recpie.objects.filter(category=c_category)
            
     
 
   
 
    return render(request, "main/post.html", context = {"recpies" : recpies})


def detail_recpie(request: HttpRequest,recpie_id):
   try:
    recpie = Recpie.objects.get(id=recpie_id)
    comments=Comment.objects.filter(recpie=recpie)
   except:
     return render(request, "main/notfound.html")
   
   is_favorite = False

   if request.user.is_authenticated:
        is_favorite = Favorite.objects.filter(recpie=recpie, user=request.user).exists()


   
   if request.method == "POST" and request.user.is_authenticated:
        new_comment = Comment(recpie=recpie, user=request.user, content=request.POST["content"], rating=request.POST["rating"])
        new_comment.save()
   return render(request, "main/detail_recpie.html",{"recpie":recpie ,"Comment":Comment,"comments":comments , "is_favorite" : is_favorite} )



def not_found(request: HttpRequest):

    return render(request, "main/notfound.html")

def update_recpie(request: HttpRequest,recpie_id):
    
    if not request.user.is_authenticated:
        return redirect("users:login_user")
    
    #updating recpie
    recpie = Recpie.objects.get(id=recpie_id)
    if request.method == "POST":
        recpie.title_recipes=request.POST['title_recipes']
        recpie.category=request.POST['category']
        recpie.Ingredients=request.POST['Ingredients']
        recpie.Instructions=request.POST['Instructions']
        recpie.publish_date=request.POST['publish_date']
        if "image" in request.FILES:
         recpie.image=request.FILES['image']
        recpie.save()
        return redirect("main:post_view")
        

    return render(request, "main/update_recpie.html",{"recpie":recpie} )

def delete_recpie(request: HttpRequest,recpie_id):
    
    #deleting an entry from database
    recpie = Recpie.objects.get(id=recpie_id)
    recpie.delete()
    return redirect("main:post_view")

def add_fav_recpie(request: HttpRequest,recpie_id):
    
     if not request.user.is_authenticated:
        return redirect("users:login_user")
     
     recpie=Recpie.objects.get(id=recpie_id)
     if not Favorite.objects.filter(user=request.user, recpie=recpie).exists():
        new_favorite = Favorite(user=request.user, recpie=recpie)
        new_favorite.save()
    
     return redirect("main:detail_recpie", recpie_id=recpie_id)
 
def remove_fav_recpie(request: HttpRequest,recpie_id):
    
    if not request.user.is_authenticated:
        return redirect("users:login_user")
    

    recpie=Recpie.objects.get(id=recpie_id)   
    user_favorite = Favorite.objects.filter(user=request.user, recpie=recpie).first()

    if user_favorite:
        user_favorite.delete()
        

    return redirect("main:detail_recpie", recpie_id=recpie_id)

def user_fav_recpie(request: HttpRequest):

    return render(request, 'main/favorite.html')

    
   