from django.shortcuts import render

def ServiceProduct(request):
    
    mgs = "Blog us Page"
    
    Context = {
        "mgs": mgs
    }
    return render(request, "service_product/index.html", Context)