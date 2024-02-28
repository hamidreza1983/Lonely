from django.shortcuts import render

def portfolio_details(request, *args, **kwargs):
    return render(request, "home/portfolio-details.html")