from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from .models import BlogWebsite,Comment

# Create your views here.

def home_view(request:HttpRequest):

    blogs= BlogWebsite.objects.all()

    return render(request,"main/home_view.html", context = {"blogs" : blogs})

def add_blog_view(request: HttpRequest):

    if request.method == "POST":
        #adding a blog
        new_blog = BlogWebsite(title=request.POST["title"], content=request.POST["content"], category=request.POST["category"],  publish_date=request.POST["publish_date"],image=request.FILES["image"])
        new_blog.save()

        return redirect("main:home_view")

    return render(request, "main/add_blog_view.html",{"Categorys": BlogWebsite.Categorys})

def blog_detail_view(request : HttpRequest, blog_id):
    
    #to get a single entry in the database
    blog = BlogWebsite.objects.get(id=blog_id)
    comments = Comment.objects.filter(blog=blog)
    if request.method == "POST":
        new_comment = Comment(blog=blog, name=request.POST["name"], content=request.POST["content"])
        new_comment.save()

    return render(request, "main/blog_detail.html", {"blog" : blog, "comments" : comments, "Comment" : Comment})

def blog_update_view(request:HttpRequest, blog_id):
    
    try:
        update_blog = BlogWebsite.objects.get(id=blog_id)
        
        #updating a book
        if request.method == "POST":
            update_blog.title = request.POST["title"]
            update_blog.content = request.POST["content"]
            update_blog.category = request.POST["category"]
            update_blog.publish_date = request.POST["publish_date"]
            if "image" in request.FILES:
                update_blog.image = request.FILES["image"]
            update_blog.save()
            return redirect("main:blog_detail_view", blog_id=blog_id)    
    except:
        return render(request, "main/not_found.html")
    
    return render(request, "main/update_blog.html", {"blog" : update_blog})

def blog_delete_view(request: HttpRequest, blog_id):
    #deleting an entry from database
    delete_blog = BlogWebsite.objects.get(id=blog_id)
    delete_blog.delete()

    return redirect("main:home_view")

def bolg_search(request: HttpRequest):
    
    if "search" in request.GET:
        blogs = BlogWebsite.objects.filter(title__contains=request.GET["search"])
    else:
        blogs = BlogWebsite.objects.all()

    return render(request, 'main/search.html', {"blogs" : blogs})


