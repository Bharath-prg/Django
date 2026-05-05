from django.shortcuts import render
from .models import Faculty

def index(request):
    return render(request, "index.html")

def add_faculty(request):
    if request.method == "POST":
        Faculty.objects.create(
            fid=request.POST.get("fid"),
            name=request.POST.get("name"),
            branch=request.POST.get("branch"),
            title=request.POST.get("title")
        )
    return render(request, "index.html")

def cse_prof(request):
    faculty = Faculty.objects.filter(branch__iexact="cse", title__iexact="professor")
    return render(request, "result.html", {"faculty": faculty} )