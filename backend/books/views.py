from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum

from .models import Subject, Book
from students.models import Student
from transactions.models import IssueBook
from transactions.views import update_issue_status   # 🔥 IMPORTANT


# ==============================
# DASHBOARD (UPDATED)
# ==============================

@login_required
def dashboard(request):

    # 🔥 Auto update issue status (Late / Due Today / On Time)
    update_issue_status()

    total_books = Book.objects.count()

    available_books = Book.objects.aggregate(
        total=Sum('available_quantity')
    )['total'] or 0

    issued_books = IssueBook.objects.filter(
        returned=False
    ).count()

    total_students = Student.objects.count()

    late_books = IssueBook.objects.filter(
        status="Late",
        returned=False
    ).count()

    due_today_books = IssueBook.objects.filter(
        status="Due Today",
        returned=False
    ).count()

    context = {
        "total_books": total_books,
        "available_books": available_books,
        "issued_books": issued_books,
        "total_students": total_students,
        "late_books": late_books,
        "due_today": due_today_books,
    }

    return render(request, "books/dashboard.html", context)


# ==============================
# SUBJECT MANAGEMENT
# ==============================

@login_required
def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'books/subject_list.html', {'subjects': subjects})


@login_required
def subject_books(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    books = Book.objects.filter(subject=subject)

    context = {
        'subject': subject,
        'books': books
    }
    return render(request, 'books/subject_books.html', context)


# ==============================
# ADD BOOK MODULE (FIXED)
# ==============================

@login_required
def add_book(request):
    if request.method == "POST":

        book_name = request.POST.get('book_name')
        author_name = request.POST.get('author_name')
        quantity = request.POST.get('quantity')
        subject_id = request.POST.get('subject')
        new_subject_name = request.POST.get('new_subject')

        if not book_name or not book_name.strip():
            messages.error(request, "Book Name is required")
            return redirect('add_book')

        if not quantity:
            messages.error(request, "Quantity is required")
            return redirect('add_book')

        quantity = int(quantity)

        if new_subject_name and new_subject_name.strip():
            subject, created = Subject.objects.get_or_create(
                name=new_subject_name.strip()
            )
        else:
            if not subject_id:
                messages.error(request, "Please select or add a subject")
                return redirect('add_book')
            subject = get_object_or_404(Subject, id=subject_id)

        Book.objects.create(
            title=book_name.strip(),
            author=author_name.strip() if author_name else "",
            subject=subject,
            total_quantity=quantity,
            available_quantity=quantity
        )

        messages.success(request, "Book Added Successfully")
        return redirect('add_book')

    subjects = Subject.objects.all()
    return render(request, 'books/add_book.html', {'subjects': subjects})


# ==============================
# ADD SUBJECT MODULE
# ==============================

@login_required
def add_subject(request):
    if request.method == "POST":
        subject_name = request.POST.get('subject_name')

        if Subject.objects.filter(name=subject_name).exists():
            messages.warning(request, "Subject already exists")
        else:
            Subject.objects.create(name=subject_name)
            messages.success(request, "Subject added successfully")

        return redirect('add_subject')

    return render(request, 'books/add_subject.html')
