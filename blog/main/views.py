from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Post,Comment

def home_view(request: HttpRequest):

    return render(request, "main/home.html")

def add_post_view(request: HttpRequest):
    try:
        if request.method == "POST":
            new_post = Post(title=request.POST["title"], content=request.POST["content"], category=request.POST["category"],image=request.FILES["image"])
            new_post.save()

            return redirect("main:all_posts_view")

        return render(request, 'main/add_post.html')
    except:
        return render(request, "main/error.html")


def all_posts_view(request: HttpRequest):
    posts = Post.objects.all()
    

    return render(request, "main/posts.html", context = {"posts" : posts})

def post_detail_view(request: HttpRequest,post_id):
    try:
        post = Post.objects.get(id=post_id)
        comments = Comment.objects.filter(post=post)
        if request.method == "POST":
            new_comment = Comment(post=post, name=request.POST["name"], content=request.POST["content"])
            new_comment.save()

        return render(request, "main/post_detail.html", context = {"post" : post ,"comments" : comments, "Comment" : Comment})
    except:
        return render(request, "main/error.html")

def update_view(request: HttpRequest,post_id):
    try:
        post = Post.objects.get(id=post_id)
        if request.method == "POST":
            post.title = request.POST["title"]
            post.content = request.POST["content"]
            post.category = request.POST["category"]
            if "image" in request.FILES:
                post.image = request.FILES["image"]
            post.save()

            return redirect("main:post_detail_view", post_id= post.id)

        return render(request, "main/update_post.html",{"post" : post})
    except:
        return render(request, "main/error.html")

def delete_view(request: HttpRequest,post_id):
    try:
        post = Post.objects.get(id=post_id)
        post.delete()

        return redirect("main:all_posts_view")
    except:
        return render(request, "main/error.html")

def filter_view(request:HttpRequest):
    if "search" in request.GET:
        posts = Post.objects.filter(title__contains=request.GET["search"])
    elif "fashion" in request.GET:
        posts = Post.objects.filter(category = "fashion")
    elif "lifestyle" in request.GET:
        posts = Post.objects.filter(category = "lifestyle")
    elif "cooking" in request.GET:
        posts = Post.objects.filter(category = "cooking")
    elif "reviews" in request.GET:
        posts = Post.objects.filter(category = "reviews")
    elif "business" in request.GET:
        posts = Post.objects.filter(category = "business")
    else:
        posts = Post.objects.all()


    return render(request,"main/filter_post.html",{"posts" : posts,})