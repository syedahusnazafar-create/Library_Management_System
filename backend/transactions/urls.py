from django.urls import path
from . import views

urlpatterns = [
    path("issue-book/", views.issue_book, name="issue_book"),
    path("return-book/", views.return_book, name="return_book"),
    path("update-issue-status/", views.update_issue_status, name="update_issue_status"),
    path("issued-books/", views.issue_list, name="issue_list"),
    
]
