from django.db import models

# Create your models here.
class StudentData(models.Model):
    email = models.EmailField(max_length=256)
    name = models.CharField(max_length=256)

class Course(models.Model):
    student = models.ForeignKey(StudentData, on_delete=models.CASCADE, default=0)
    course_name = models.CharField(max_length=256)