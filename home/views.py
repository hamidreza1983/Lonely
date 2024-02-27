from django.shortcuts import render

# Create your views here.


def home(request, *args, **kwargs):
    return render(request, "home/index.html")


def portfolio_details(request, *args, **kwargs):
    return render(request, "home/portfolio-details.html")
