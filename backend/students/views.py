from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student
from django.contrib.auth.decorators import login_required

@login_required
def add_student(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        department = request.POST.get("department")

        # ✅ Check if email already exists
        if Student.objects.filter(email=email).exists():
            messages.error(request, "Student with this email already exists!")
            return redirect("add_student")

        # ✅ Create student
        Student.objects.create(
            name=name,
            email=email,
            phone=phone,
            department=department
        )

        messages.success(request, "Student Added Successfully!")
        return redirect("add_student")

    return render(request, "students/add_student.html")