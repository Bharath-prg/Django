from django.shortcuts import render
from .models import Alumni

def index(request):
    return render(request, "index.html")

def add_alumni(request):
    if request.method == "POST":
        Alumni.objects.create(
            name=request.POST.get("name"),
            usn=request.POST.get("usn"),
            passing_year=request.POST.get("year"),
            company=request.POST.get("company")
        )
    return render(request, "index.html")

def filter_year(request):
    alumni = []
    if request.method == "POST":
        year = request.POST.get("year")
        alumni = Alumni.objects.filter(passing_year=year)
    return render(request, "result.html", {"alumni": alumni})