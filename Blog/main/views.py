from django.shortcuts import render ,redirect
from django.http import HttpResponse , HttpRequest
from .models import Recipe,Comment

# Create your views here.

def home_view(request):

    return render(request , 'main/home.html')

def add_post(request):
    if request.method == "POST":
        #adding a Recipe
        new_Recipe = Recipe(title=request.POST["title"], content=request.POST["content"], catagory=request.POST["catagory"], publish_date=request.POST["publish_date"], image=request.FILES["image"])
        new_Recipe.save()
        return redirect("main:all_recipes_view")
    return render(request,('main/add_post.html'))

def all_recipes_view(request: HttpRequest):

    if "search"in request.GET:
        recipes= Recipe.objects.filter(title__contains=request.GET["search"])

    recipes = Recipe.objects.all()

    return render(request, "main/all_Recipes.html", context = {"recipes" : recipes})

'''------------detail page--------------------------------------'''

def recipe_detail_view(request : HttpRequest, recipe_id):
    
    recipe= Recipe.objects.get(id=recipe_id)
    comments= Comment.objects.filter(recipe=recipe)
    if request.method == "POST":
        new_comment = Comment(recipe=recipe, name=request.POST["name"], content=request.POST["content"], rating=request.POST["rating"])
        new_comment.save()

    return render(request, "main/recipe_detail.html", {"recipe" : recipe , "comments" : comments, "Comment" : Comment})

'''------------------------------------------------'''
def recipe_update_view(request:HttpRequest, recipe_id):
    
    recipe = Recipe.objects.get(id=recipe_id)

    #updating a recipe
    if request.method == "POST":
        recipe.title = request.POST["title"]
        recipe.content = request.POST["content"]
        recipe.catagory = request.POST["catagory"]
        recipe.publish_date = request.POST["publish_date"]
        recipe.save()

        return redirect("main:recipe_detail_view", recipe_id=recipe.id)

    return render(request, "main/update_recipe.html", {"recipe": recipe})


def recipe_delete_view(request: HttpRequest, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    recipe.delete()

    return redirect("main:all_recipes_view")


def recipe_search_view(request: HttpRequest):

    if "search" in request.GET:
        recipe = Recipe.objects.filter(title__contains=request.GET["search"])
    else:
        recipe = Recipe.objects.all()

    return render(request, 'main/search_results.html', {"recipe" : recipe})
