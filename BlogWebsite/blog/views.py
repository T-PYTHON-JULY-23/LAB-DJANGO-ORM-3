from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Post , Comment
from django.http import Http404


# Create your views here.


def home(request:HttpRequest):
    
    return render(request,'blog/home.html')







def add_post(request:HttpRequest):
    if request.method == 'POST':
        new_post = Post(title=request.POST['title'], content=request.POST['content'], category=request.POST['category'], publish_date=request.POST['publish_date'], image_upload=request.FILES['image'])
        new_post.save()

        return redirect("blog:all_post_view")

    return render(request,'blog/add_post.html' , {"Post" : Post.category_choices})






def view_post(request:HttpRequest):
    post_all = Post.objects.all().order_by('title')

    return render(request,'blog/all_post.html', context={'post':post_all} )





def detail_posts(request:HttpRequest, post_id):
    
    post_detail = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=post_detail)

    if request.method == 'POST':
        new_comment = Comment(post=post_detail, name=request.POST['name'], content_comment=request.POST['content'])
        new_comment.save()
    
    return render (request,'blog/detail_posts.html', {'post':post_detail, 'comments':comments , 'comment':Comment })




    
        
    
        


def update_post(request:HttpRequest, post_id):
    
    try:
         
        post_update = Post.objects.get(id=post_id)
        if request.method == 'POST':
            post_update.title = request.POST['title']
            post_update.content = request.POST['content']
            post_update.category = request.POST['category']
            post_update.publish_date = request.POST['publish_date']
            
            if 'image' in request.FILES:
                post_update.image_upload = request.FILES['image']

            post_update.save()

            return redirect('blog:detail_post_view', post_id=post_update.id)
    except Exception as e:
        print(e)
        return render(request,'blog/not_found.html')
        
    post_update.publish_date = post_update.publish_date.strftime("%Y-%m-%d %H:%M:%S")

    return render(request,'blog/ubdate_posts.html',{'post':post_update})




def delet_post(request:HttpRequest, post_id):
    posts = Post.objects.get(id=post_id)
    posts.delete()

    return redirect('blog:all_post_view')




def search_feature(request:HttpRequest):
    
    if 'search_query' in request.GET:
        
        posts = Post.objects.filter(title__contains=request.GET['search_query'])
    else:
        posts=Post.objects.all()

    return render(request, 'blog/search_result.html', {'posts':posts})
    


def category(request,post_choices):
    if request.method=='POSt':
        pass



    

