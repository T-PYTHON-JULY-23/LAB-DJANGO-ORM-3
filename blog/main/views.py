from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest
from .models import Blog , Comment

# Create your views here.

def home_view(request:HttpRequest):

    return render(request, 'main/home.html')


def addblog_view(request:HttpRequest):
    if request.method == "POST":

        new_blog = Blog(title=request.POST["title"], content=request.POST["content"],image=request.FILES["image"], category=request.POST["category"], publish_date=request.POST["publish_date"])

        new_blog.save()

        return redirect("main:all_bolgs_view")
    return render(request, 'main/add_blog.html',{"category_choices": Blog.category_choices})


def all_bolgs_view(request: HttpRequest):

    blogs = Blog.objects.all()


    return render(request, "main/all_blogs.html", context = {"blogs" : blogs,"category_choices": Blog.category_choices})



def blog_detail_view(request : HttpRequest, blog_id):
    
    blog = Blog.objects.get(id=blog_id)
    comments = Comment.objects.filter(blog=blog)
    if request.method == "POST":
        new_comment = Comment(blog=blog, name=request.POST["name"], content=request.POST["content"])
        new_comment.save()

    return render(request, "main/blog_detail.html", {"blog" : blog, "comments" : comments})



def blog_update_view(request:HttpRequest, blog_id):
    
    blog = Blog.objects.get(id=blog_id)

    #updating a blog
    if request.method == "POST":
        blog.title = request.POST["title"]
        blog.content = request.POST["content"]
        blog.category = request.POST["category"]
        blog.publish_date = request.POST["publish_date"]
        if 'image'in  request.FILES:
            blog.image=request.FILES["image"]
        blog.save()

        return redirect("main:blog_detail_view", blog_id=blog.id)

    return render(request,"main/update_blog.html", {"blog": blog,"category_choices": Blog.category_choices})

def blog_delete_view(request: HttpRequest, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()

    return redirect("main:all_bolgs_view")


def blog_search_view(request:HttpRequest):
        if request.method == 'POST':
            search_query = request.POST['search_query']
            blogs = Blog.objects.filter(title__contains=search_query)


        return render(request, "main/all_blogs.html", {'query':search_query, 'blogs':blogs})
        
def update_comment_view(request:HttpRequest, comment_id):
    comment = Comment.objects.get(id=comment_id)
    blog=comment.blog
    #updating a comment
    if request.method == "POST":
        comment.name = request.POST["name"]
        comment.content = request.POST["content"]
        comment.save()

        return redirect("main:blog_detail_view", blog_id=blog.id)

    return render(request,'main/update_comment.html',{"comment": comment})

