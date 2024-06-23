from django.contrib import admin
from .models import Student, StudentCourse, Course, TACourse, AttendanceEntry, Exam, StudentPicture

# Register your models here.

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(StudentCourse)
admin.site.register(TACourse)
admin.site.register(AttendanceEntry)
admin.site.register(Exam)
admin.site.register(StudentPicture)