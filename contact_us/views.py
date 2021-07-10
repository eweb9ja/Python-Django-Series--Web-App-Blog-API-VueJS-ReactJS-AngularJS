from django.shortcuts import render

def ContactUs(request):
    
    mgs = "Contact us Page"
    
    Context = {
        "mgs": mgs
    }
    return render(request, "contact_us/index.html", Context)
