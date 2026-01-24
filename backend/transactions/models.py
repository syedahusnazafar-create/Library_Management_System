from django.db import models
from books.models import Book
from students.models import Student


class IssueBook(models.Model):

    STATUS_CHOICES = (
        ("On Time", "On Time"),
        ("Due Today", "Due Today"),
        ("Late", "Late"),
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE
    )

    issue_date = models.DateField()

    return_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="On Time"
    )

    returned = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.student.name} - {self.book.title}"
