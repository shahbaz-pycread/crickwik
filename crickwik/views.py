from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request,'crickwik/home.htm',context)

def about(request):
    return render(request,'crickwik/about.htm',{'title':'About'})