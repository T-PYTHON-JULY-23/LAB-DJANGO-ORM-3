from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import NewBlog
from .models import Comment
# Create your views here.
def home_page_view(request: HttpRequest):

    news = NewBlog.objects.all().order_by("-publish_date")[0:3]

    return render(request, "main/homePage.html",{"news":news})


def add_new_view(request: HttpRequest):
    category=NewBlog.category_choices
    if request.method == "POST":
        #adding a book
        new_book = NewBlog(title=request.POST["title"], content=request.POST["content"], category=request.POST["category"], publish_date=request.POST["publish_date"],image=request.FILES["image"])
        new_book.save()

        return redirect("main:all_new_view")
    return render(request, 'main/add_new.html', {"category":category})

    
def all_new_view(request: HttpRequest):

    news = NewBlog.objects.all()
    if "search" in request.GET:
        news = NewBlog.objects.filter(title__contains=request.GET["search"])
    else:
        news = NewBlog.objects.all()


    return render(request, "main/all_new.html", context = {"news" : news})


def detail_view(request : HttpRequest, new_id):
    
    #to get a single entry in the database
    new = NewBlog.objects.get(id=new_id)
    comments = Comment.objects.filter(new=new)
    if request.method == "POST":
        new_comment = Comment(new=new, name=request.POST["name"], content=request.POST["content"],)
        new_comment.save()

    return render(request, "main/detali.html", {"new" : new,"comments" : comments, "Comment" : Comment})


def updeat_view(request:HttpRequest, new_id):

    new = NewBlog.objects.get(id=new_id)
    category=NewBlog.category_choices
    if request.method == "POST":
        new.title = request.POST["title"]
        new.content = request.POST["content"]
        new.category = request.POST["category"]
        new.publish_date=request.POST["publish_date"]
        new.save()


        return redirect("main:detail_view")
    return render(request, "main/updeat.html", {"new" : new,"category":category})


def delete_view(request:HttpRequest , new_id):

    new = NewBlog.objects.get(id=new_id)
    new.delete()
    
    return redirect ("main:all_new_view")

