from django.shortcuts import render

def Blog(request):
    
    mgs = "Blog us Page"
    
    Context = {
        "mgs": mgs
    }
    return render(request, "blog/index.html", Context)
