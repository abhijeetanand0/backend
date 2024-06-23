from datetime import time, datetime, timedelta

from .models import Course, Exam, Student, StudentCourse, TACourse
from random import randrange
from django.contrib.auth.models import User


def random_bool():
    x = randrange(0, 10)
    return x > 2


start = (datetime.now() - timedelta(days=50))
end = (datetime.now() + timedelta(days=50))

courses = [
    ['Introduction to Electronics', 'ECN-102', 'spring', '2024'],
    ['Computer Programming and Utilization', 'CS-101', 'spring', '2024'],
    ['Quantum Physics and Application', 'PH-107', 'spring', '2024']
]


def generate_courses():
    for course in courses:
        obj = Course(
            title=course[0],
            code=course[1],
            semester=course[2],
            year=course[3],
            start_date=start,
            end_date=end
        )
        obj.save()
    print(f"GENERATED {len(courses)} COURSES SUCCESSFULLY")


exams = [
    'Quiz 1', 'Quiz 2', 'Mid-Term Exam', 'End-Term Exam'
]


def generate_exams():
    count = 0
    courses = Course.objects.all()
    for course in courses:
        st = datetime.now() - timedelta(days=40)
        se = datetime.now() - timedelta(days=40) + timedelta(hours=3)
        for exam in exams:
            obj = Exam(course=course, title=exam, start_time=st, end_time=se)
            obj.save()
            count += 1
            st += timedelta(days=11)
            se += timedelta(days=11)
    print(f"GENERATED {count} EXAMS SUCCESSFULLY")


students = [
    ['Kamal Nayan', '2022', 'CSE', '22B1022'],
    ['Sanskar Shaurya', '2022', 'CSE', '22B1039'],
    ['Chetan Arya', '2022', 'ECE', '22B1034'],
    ['Kartik Gulia', '2021', 'CE', '22B2098']
]


def generate_students():
    for student in students:
        obj = Student(name=student[0], year=student[1], department=student[2], roll=student[3])
        obj.save()
    print(f"GENERATED {len(students)} STUDENTS SUCCESSFULLY")


def link_students_courses():
    count = 0
    courses = Course.objects.all()
    students = Student.objects.all()
    for course in courses:
        for student in students:
            if (random_bool()):
                obj = StudentCourse(student=student, course=course)
                obj.save()
                count += 1

    print(f"GENERATED {count} STUDENTS-COURSE RELATION SUCCESSFULLY")


def link_ta_teachers():
    teacher = User.objects.get(username='abhijeet@gmail.com')
    courses = Course.objects.all()
    for course in courses:
        obj = TACourse(teacher=teacher, course=course)
        obj.save()
    print(f"GENERATED {len(courses)} TA-COURSE RELATION SUCCESSFULLY")
