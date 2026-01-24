from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    roll_number = models.CharField(max_length=50, unique=True)
    class_name = models.CharField(max_length=50)
    session = models.CharField(max_length=50)

    def __str__(self):
        return self.name
