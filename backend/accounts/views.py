from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count
from django.utils import timezone

from books.models import Book
from students.models import Student
from transactions.models import IssueBook


# =========================
# LOGIN VIEW
# =========================
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect("login")

    return render(request, "accounts/login.html")


# =========================
# DASHBOARD VIEW
# =========================
@login_required
def dashboard(request):

    # 🔔 Auto update overdue status (better way)
    today = timezone.now().date()

    IssueBook.objects.filter(
        returned=False,
        return_date__lt=today
    ).update(status="Overdue")   # make sure status field exists in model

    # 📚 Total Books (Sum of total_quantity)
    total_books = Book.objects.aggregate(
        total=Sum("total_quantity")
    )["total"] or 0

    # 📘 Available Books
    available_books = Book.objects.aggregate(
        available=Sum("available_quantity")
    )["available"] or 0

    # 📕 Currently Issued (not returned)
    issued_books = IssueBook.objects.filter(returned=False).count()

    # 👩‍🎓 Total Students
    total_students = Student.objects.count()

    # 🔴 Overdue Count
    overdue_count = IssueBook.objects.filter(
        returned=False,
        return_date__lt=today
    ).count()

    # 🕒 Recent Issued Books (Last 5 Records - including returned)
    recent_issued = IssueBook.objects.select_related(
        "book", "student"
    ).order_by("-issue_date")[:5]

    context = {
        "total_books": total_books,
        "available_books": available_books,
        "issued_books": issued_books,
        "total_students": total_students,
        "overdue_count": overdue_count,
        "recent_issued": recent_issued,
    }

    return render(request, "accounts/dashboard.html", context)


# =========================
# LOGOUT VIEW
# =========================
@login_required
def logout_view(request):
    logout(request)
    return redirect("login")
