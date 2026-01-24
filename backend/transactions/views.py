from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta

from students.models import Student
from books.models import Book
from transactions.models import IssueBook





# ==================================
# RETURN DATE REMINDER SYSTEM
# ==================================

def update_issue_status():
    today = timezone.now().date()
    issues = IssueBook.objects.filter(returned=False)

    for issue in issues:
        if today > issue.return_date:
            issue.status = "Late"
        elif today == issue.return_date:
            issue.status = "Due Today"
        else:
            issue.status = "On Time"
        issue.save()


# ==================================
# ISSUE BOOK
# ==================================

@login_required
def issue_book(request):
    students = Student.objects.all()
    books = Book.objects.all()
    today = timezone.now().date()

    if request.method == "POST":
        student_id = request.POST.get("student")
        book_id = request.POST.get("book")
        return_days = request.POST.get("return_days")

        if not student_id or not book_id or not return_days:
            messages.error(request, "All fields are required")
            return redirect("issue_book")

        try:
            return_days = int(return_days)
        except ValueError:
            messages.error(request, "Return days must be numeric")
            return redirect("issue_book")

        return_date = today + timedelta(days=return_days)

        student = get_object_or_404(Student, id=student_id)
        book = get_object_or_404(Book, id=book_id)

        if book.available_quantity > 0:
            IssueBook.objects.create(
                student=student,
                book=book,
                issue_date=today,
                return_date=return_date,
                returned=False,
                status="On Time"
            )

            book.available_quantity -= 1
            book.save()

            messages.success(request, "Book Issued Successfully")
            return redirect("issue_book")
        else:
            messages.error(request, "Book Not Available")

    return render(request, "transactions/issue_book.html", {
        "students": students,
        "books": books,
        "today": today,
    })


# ==================================
# ISSUED BOOK LIST (🔥 MISSING PART)
# ==================================
   # agar yeh function alag file mein hai

@login_required
def issue_list(request):
    update_issue_status()  # 🔔 Auto update Late / Due Today / On Time

    issued_list = IssueBook.objects.filter(returned=False)

    return render(request, "transactions/issue_list.html", {
        "issued_list": issued_list
    })


# ==================================
# RETURN BOOK
# ==================================

@login_required
def return_book(request):
    update_issue_status()

    if request.method == "POST":
        issue_id = request.POST.get("issue_id")

        issue = get_object_or_404(IssueBook, id=issue_id)

        if not issue.returned:
            issue.returned = True
            issue.save()

            book = issue.book
            book.available_quantity += 1
            book.save()

            messages.success(request, "Book Returned Successfully")

        return redirect("issue_list")

    issues = IssueBook.objects.filter(returned=False)

    return render(request, "transactions/return_book.html", {
        "issues": issues
    })
