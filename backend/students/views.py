from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Student

@login_required
def add_student(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        roll_number = request.POST.get("roll_number")

        if not name or not phone or not email or not roll_number:
            messages.error(request, "All fields are required")
            return redirect("add_student")

        Student.objects.create(
            name=name,
            phone=phone,
            email=email,
            roll_number=roll_number
        )

        messages.success(request, "Student Added Successfully")
        return redirect("add_student")

    return render(request, "students/add_student.html")
