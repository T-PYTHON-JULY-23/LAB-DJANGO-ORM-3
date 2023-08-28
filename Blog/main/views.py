from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post,Comment



def add_post_view(request: HttpRequest):

    if request.method == "POST":
        new_post = Post(title=request.POST["title"], content=request.POST["content"], category=request.POST["category"], publish_date=request.POST["publish_date"],image=request.FILES["image"])
        new_post.save()
        return redirect("main:all_post_view")

    return render(request, 'main/add_post.html',{"category_choices": Post.category_choices})



def all_post_view(request: HttpRequest):

    posts = Post.objects.all()
    return render(request, "main/all_posts.html", context = {"posts" : posts})


def home_view(request: HttpRequest):
      
    return render(request, "main/home.html")

def post_detail_view(request : HttpRequest, post_id):
    
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=post)
    if request.method == "POST":
        new_comment = Comment(post=post, name=request.POST["name"], content=request.POST["content"], rating=request.POST["rating"])
        new_comment.save()

    return render(request, "main/post_detail.html", {"post" : post, "comments" : comments, "Comment" : Comment})



def post_update_view(request:HttpRequest, post_id):
    
    post = Post.objects.get(id=post_id)

    #updating a book
    if request.method == "POST":
        post.title = request.POST["title"]
        post.category = request.POST["category"]
        post.publish_date = request.POST["publish_date"]
        post.save()

        return redirect("main:post_detail_view", post_id=post.id)

    return render(request, "main/update_post.html", {"post": post})


def post_delete_view(request: HttpRequest, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()

    return redirect("main:all_post_view")



def search_view(request:HttpRequest):
    if "search_query" in request.GET:
     posts = Post.objects.filter(title__contains=request.GET["search_query"])
    else:
     posts = Post.objects.all()
    return render(request, "main/all_posts.html",{'posts':posts})
  
   