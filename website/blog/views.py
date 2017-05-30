from django.shortcuts import render, redirect
from blog.models import Blog

def index(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request, 'blog/blog.html', context)

def create(request):
    print (request.POST)
    blog = Blog(name=request.POST['name'],
                email=request.POST['email'],
                username=request.POST['username'])
    blog.save()
    return redirect('/')

def edit(request, id):
    dog = Blog.objects.get(id=id)
    context = {"blog":blog}
    return render(request, 'blog/blog.html', context)

