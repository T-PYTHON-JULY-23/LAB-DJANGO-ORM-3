from django.shortcuts import render , redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def register_user(request:HttpRequest):
    if request.method=="POST":
        nwe_user = User.objects.create_user(first_name=request.POST['first_name'], last_name=request.POST['last_name'], username=request.POST['username'], email=request.POST['email'], password=request.POST['password']) 
        nwe_user.save()
        return redirect('accounts:login_user_viwe')
    
  
    
    return render(request, 'accounts/register.html')


def login_user(request:HttpRequest):
    msg = None

    if request.method=='POST':
        user = authenticate(request, username=request.POST['username'] ,password=request.POST['password'])

        if user:
            login(request,user)
            return redirect('blog:home_view')
        else:
            msg = 'Username or Password is wrong. No user found'

    return render(request, "accounts/login.html", {'msg':msg})



def logout_user(request:HttpRequest):
    logout(request)

    return redirect("accounts:login_user_view")





