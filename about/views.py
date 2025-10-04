from django.shortcuts import render
fom django.http import HttpResponse

# Create your views here.
def about_me(request):
    return HttpResponse("This would be the about page" )
def about_me(request):
    if request.method == "POST":
        return HttpResponse("You must have POSTed something" )
    return HttpResponse(request.method)
