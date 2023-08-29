from django.shortcuts import render, get_object_or_404, redirect
from .models import Post  # استيراد النموذج Post فقط
from .models import Comment  # استيراد النموذج Comment
from django.db.models import Q

def home(request):
    return render(request, 'pages/home.html')

def posts(request):
    posts = Post.objects.all()
    return render(request, 'pages/posts.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        category = request.POST['category']
        image = request.FILES['image']  # تحميل الصورة من المستخدم

        if not title or not content or not category or not image:
            error_message = 'Please fill in all required fields.'
            return render(request, 'pages/add_post.html', {'error_message': error_message})
        
        post = Post.objects.create(title=title, content=content, category=category, image=image)  # حفظ الصورة في النموذج
        return redirect('post_detail', post_id=post.id)
    
        if not (title and content and category):
            error_message = 'Please fill in all fields.'
            return render(request, 'pages/add_post.html', {'error_message': error_message})
    return render(request, 'pages/add_post.html')

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post)
    context = {'post': post, 'comments': comments}
    comments = post.comments.all()
    return render(request, 'pages/post_detail.html', context)

def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.category = request.POST['category']
        
        if 'image' in request.FILES:  # تحميل الصورة المحدثة من المستخدم
            post.image = request.FILES['image']
        
        post.save()
        return redirect('post_detail', post_id=post.id)
    return render(request, 'pages/update_post.html', {'post': post})

def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('posts')
    return render(request, 'pages/delete_post.html', {'post': post})

def search_posts(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(category__icontains=query)
        )
        return render(request, 'pages/posts.html', {'posts': posts})
    
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment

def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        content = request.POST.get('content')
        timestamp = request.POST.get('timestamp')

        comment = Comment(post=post, name=name, content=content, timestamp=timestamp)
        comment.save()

    return redirect('post_detail', post_id=post_id)