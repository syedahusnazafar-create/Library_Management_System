from django.urls import path
from . import views

urlpatterns = [
    path('subjects/', views.subject_list, name='subject_list'),
    path('subjects/<int:subject_id>/', views.subject_books, name='subject_books'),
    path('add-book/', views.add_book, name='add_book'),
    path('add-subject/', views.add_subject, name='add_subject'),   # NEW
]
