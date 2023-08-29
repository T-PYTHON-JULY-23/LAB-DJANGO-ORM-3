from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Blog , Comment
 

# Create your views here.


def add_post_view(request: HttpRequest):

    if request.method == "POST":
        #adding a post
        new_post = Blog(title=request.POST["title"], Content=request.POST["Content"], category= request.POST["category"], publish_date=request.POST["publish_date"], image=request.FILES["image"])
        new_post.save()

        return redirect("blog:all_post_view")

    return render(request, 'blog/add_post.html',{"Blog":Blog})



def all_post_view(request: HttpRequest):

    blogs = Blog.objects.all()

    return render(request, "blog/all_post.html", context = {"blogs" : blogs})


def search_view(request: HttpRequest):

    if "search" in request.GET:
        blogs = Blog.objects.filter(title__contains=request.GET["search"])
    else:
        blogs = Blog.objects.all()

    return render(request, 'blog/searchResult.html', {"blogs" : blogs})



def details_post_view(request:HttpRequest, blog_id):

    blog = Blog.objects.get(id=blog_id)

    comments = Comment.objects.filter(blog=blog)

    if request.method == "POST":
        new_comment = Comment(blog=blog, name=request.POST["name"], content=request.POST["content"])
        new_comment.save()

    return render(request,"blog/details_post.html",{"blog" : blog, "comments" : comments})



def update_post_view(request:HttpRequest,blog_id):
       
    blog = Blog.objects.get(id=blog_id)

    if request.method == "POST":
        blog.title = request.POST["title"]
        blog.Content = request.POST["Content"]
        blog.category = request.POST["category"]
        blog.publish_date = request.POST["publish_date"]
        if "image" in request.FILES:
            blog.image = request.FILES["image"]
        blog.save()

        return redirect("blog:details_post_view", blog_id=blog.id)

    return render(request, "blog/update_post.html", {"blog": blog})


def delete_post_view(request:HttpRequest,blog_id):
    blog=Blog.objects.get(id=blog_id)
    blog.delete()

    return redirect("blog:all_post_view")

