from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from books.models import Book
from students.models import Student
from transactions.models import IssueBook
from transactions.views import update_issue_status   # ✅ IMPORTANT
from django.contrib.auth import logout
from django.shortcuts import redirect

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect('login')

    return render(request, 'accounts/login.html')


@login_required
def dashboard(request):

    total_books = Book.objects.aggregate(
        total=Sum("total_quantity")
    )["total"] or 0

    available_books = Book.objects.aggregate(
        available=Sum("available_quantity")
    )["available"] or 0

    issued_books = IssueBook.objects.filter(returned=False).count()

    total_students = Student.objects.count()

    return render(request, "accounts/dashboard.html", {
        "total_books": total_books,
        "available_books": available_books,
        "issued_books": issued_books,   # ✅ NUMBER ONLY
        "total_students": total_students,
    })


def logout_view(request):
    logout(request)
    return redirect('login')
