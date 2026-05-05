from django.shortcuts import render, redirect
from django.db import IntegrityError
from .models import Student

def index(request):
    students = Student.objects.all()
    return render(request, "index.html", {"students": students})


def add_student(request):
    students = Student.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        usn = request.POST.get("usn")
        semester = request.POST.get("semester")
        fee_paid = True if request.POST.get("fee_paid") == "yes" else False

        try:
            Student.objects.create(
                name=name,
                usn=usn,
                semester=semester,
                fee_paid=fee_paid
            )
            return redirect("/")   # success → reload page

        except IntegrityError:
            return render(request, "index.html", {
                "students": students,
                "error": "Student with same USN in the same semester already exists"
            })

    return render(request, "index.html", {"students": students})


def delete_unpaid(request):
    if request.method == "POST":
        Student.objects.filter(fee_paid=False).delete()
    return redirect("/")