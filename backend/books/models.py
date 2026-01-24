from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    total_quantity = models.IntegerField()
    available_quantity = models.IntegerField()
    def __str__(self):
        return self.title



