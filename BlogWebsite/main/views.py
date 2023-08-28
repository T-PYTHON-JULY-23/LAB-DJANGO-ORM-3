from django.shortcuts import render , redirect
from django.http import HttpRequest , HttpResponse
from blog.models import Blog

# Create your views here.

def home_view(request : HttpRequest):


    return render(request, "main/index.html")



