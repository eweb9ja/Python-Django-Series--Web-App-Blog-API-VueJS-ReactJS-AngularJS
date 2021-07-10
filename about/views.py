from django.shortcuts import render

def About(request):
    
    mgs = "About us Page"
    
    Context = {
        "mgs": mgs
    }
    return render(request, "about/index.html", Context)
