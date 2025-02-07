from django.shortcuts import render

# Create your views here.

def home(req):
    return render(req, "home.html")

def portfolio(request):
    return render(request, "portfolio.html")

def about_me(request):
    return render(request, "about_me.html")