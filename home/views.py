from django.shortcuts import render

def Home(request):
    
    hello = "Hello New Django Student"
    
    Context = {
        "hello": hello
    }
    return render(request, "home/index.html", Context)
