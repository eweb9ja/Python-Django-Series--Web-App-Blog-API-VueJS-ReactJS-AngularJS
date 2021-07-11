from django.shortcuts import render, redirect
from .models import BlogPage
from django.contrib import messages

def Blog(request):
    
    blogs = BlogPage.objects.filter().order_by("-id")
    
    Context = {
        "blogs":blogs
    }
    return render(request, "blog/index.html", Context)


def ShowBlog(request, id=None):
    
    blog = BlogPage.objects.filter(id=id)
    
    Context = {
        "blog":blog
    }
    return render(request, "blog/show.html", Context)


def BlogCreate(request):
    
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        image = request.FILES.get("image", '')
        
        BlogPage.objects.create(title=title, description=description, image=image)
        
        messages.success(request, "Blog Post is Successful!")
        return redirect("blog")
    
    Context = {

    }
    return render(request, "blog/create.html", Context)
