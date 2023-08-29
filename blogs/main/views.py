from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.shortcuts import resolve_url
from .models import Blog , Comment
# Create your views here.

def home_page(request:HttpRequest):
    blogs =Blog.objects.all()
    return render(request,"main/index.html",{"blogs" : blogs})


def add_page(request:HttpRequest):
    if request.method == "POST":
        if "image" in request.FILES:
            new_blog = Blog(title=request.POST["title"], Content=request.POST["Content"], publish_date=request.POST["publish_date"],Bootcamp=request.POST["Bootcamp"], image=request.FILES["image"])
        else:
            new_blog = Blog(title=request.POST["title"], Content=request.POST["Content"], publish_date=request.POST["publish_date"],Bootcamp=request.POST["Bootcamp"])

        new_blog.save()
        return redirect("main:home_page")
    return render(request,"main/add.html", {"Bootcamps_ch": Blog.Bootcamps_ch})

def blog_detail_view(request : HttpRequest, blog_id):
    
    blog = Blog.objects.get(id=blog_id)
    comments = Comment.objects.filter(blog=blog)

    if request.method == "POST":
        new_comment = Comment(blog=blog, name=request.POST["name"], content=request.POST["content"])
        new_comment.save()
    return render(request, "main/blog_detail.html", {"blog" : blog ,  "comments" : comments, "Comment" : Comment})


def blog_update_view(request:HttpRequest, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.method == "POST":
        blog.title = request.POST["title"]
        blog.Content = request.POST["Content"]
        blog.Bootcamp = request.POST["Bootcamp"]
        blog.publish_date = request.POST["publish_date"]
        blog.save()

        return redirect("main:blog_detail_view", blog_id = blog.id)
    return render(request, "main/update.html",{"blog" : blog})

def blog_delete_view(request : HttpRequest , blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()

    return redirect("main:home_page")
def search(request:HttpRequest):
    search_phrase = request.GET.get("search")
    blog = Blog.objects.filter(title__contains=search_phrase)

    return render(request, "main/index.html", {"blogs" : blog})

# def add_comment(request:HttpRequest, post_id):
#     if request.method == "POST":
#         blog_object = Blog.objects.get(id=blog_id)
#         new_comment = Comment(blog=blog_object, )

