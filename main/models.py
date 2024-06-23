from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model


# Create your models here.


class Course(models.Model):
    SEMESTER_CHOICES = [
        ('spring', 'Spring'),
        ('autumn', 'Autumn'),
    ]

    title = models.CharField(max_length=50, null=False, blank=False)
    code = models.CharField(max_length=10, null=False, blank=False)
    semester = models.CharField(max_length=10, choices=SEMESTER_CHOICES, null=False, blank=False)
    year = models.IntegerField(null=False, blank=False)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)

    def __str__(self):
        return f"{self.code} - {self.year}"


class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False, blank=False)
    start_time = models.DateTimeField(null=False, blank=False)
    end_time = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return f"{self.course.title} - {self.title}"


class Student(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    year = models.IntegerField(null=False, blank=False)
    department = models.CharField(max_length=50, null=False, blank=False)
    roll = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return f"{self.year} - {self.name}"


class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course.code} - {self.student.name}"


class TACourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course.code} - {self.teacher.username}"


class AttendanceEntry(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    by = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(blank=False, null=False)



    # def __str__(self):


class StudentPicture(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    picture = models.ImageField()

    def __str__(self):
        return f"{self.student.name}"

