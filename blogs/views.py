from django.shortcuts import HttpResponse, redirect

def blogs(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def blogsNew(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def blogsCreate(request):
    return redirect("/")

def blogsShow(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def blogsEdit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")

def blogsDestroy(request, number):
    return redirect("/")