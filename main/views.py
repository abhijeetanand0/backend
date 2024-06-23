from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .common import error_response, success_response
from .models import TACourse, Exam, StudentCourse, Course, Student, AttendanceEntry
from datetime import date

from .serializers import CourseSerializer, ExamSerializer, StudentSerializer

from .scripts import generate_courses, generate_exams, generate_students, link_students_courses, link_ta_teachers
from datetime import datetime

# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_courses(request):
    try:
        user = request.user
        # if not TACourse.objects.filter(teacher=user).exists():
        #     return error_response("No Courses")
        relations = TACourse.objects.filter(teacher=user)
        ongoing_courses = []
        for relation in relations:
            if date.today() <= relation.course.end_date:
                ongoing_courses.append(relation.course)
        serializer = CourseSerializer(ongoing_courses, many=True)
        return success_response(serializer.data)
    except:
        return error_response("Something went wrong!")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_exams(request, course_id):
    try:
        if not Course.objects.filter(id=course_id).exists():
            return error_response("Invalid course code!")
        course = Course.objects.get(id=course_id)
        exams = Exam.objects.filter(course=course).order_by('-start_time')
        serializer = ExamSerializer(exams, many=True)
        return success_response(serializer.data)
    except:
        return error_response("Invalid course id!")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_students(request, course_id, exam_id):
    try:
        if not Course.objects.filter(id=course_id).exists():
            return error_response("Invalid course id!")
        if not Exam.objects.filter(id=exam_id).exists():
            return error_response("Invalid exam id!")
        course = Course.objects.get(id=course_id)
        exam = Exam.objects.get(id=exam_id)
        print(exam.title)

        relations = StudentCourse.objects.filter(course=course)
        print(list(relations))

        students = []
        present_count = 0
        absent_count = 0
        for relation in relations:

            student = relation.student
            obj = {
                'name': student.name,
                'year': student.year,
                'department': student.department,
                'roll': student.roll
            }

            if AttendanceEntry.objects.filter(student=student, exam=exam).exists():
                obj['present'] = True
                present_count += 1
            else:
                obj['present'] = False
                absent_count += 1

            students.append(obj)

        return Response(
            {"result": "success", "data": students, "present_count": present_count, "absent_count": absent_count})
    except:
        return error_response("Something went wrong!")


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def get_student_picture(request):
#     roll = request.data['roll']
#     if not Student.objects.filter(roll=roll).exists():
#         return error_response("Invalid roll number")
#
#     student = Student.objects.get(roll=roll)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def mark_attendance(request, exam_id, student_id):
    try:
        ta = request.user
        if not Exam.objects.filter(id=exam_id).exists():
            return error_response("Invalid exam id")
        if not Student.objects.filter(id=student_id):
            return error_response("Invalid student id")

        exam = Exam.objects.get(id=exam_id)
        student = Student.objects.get(id=student_id)

        if AttendanceEntry.objects.filter(student=student, exam=exam).exists():
            return success_response("Attendance already taken!")
        entry = AttendanceEntry(student=student, exam=exam, by=ta, time=datetime.now())
        entry.save()
        return success_response("Attendance added successfully!")
    except:
        return error_response("Something went wrong!")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_student_details(request, roll):
    print(roll);
    if not Student.objects.filter(roll=roll).exists():
        return error_response("Student not found!")
    student = Student.objects.get(roll=roll)
    serializer = StudentSerializer(student)
    return success_response(serializer.data)





@api_view(['GET'])
def generate(request):
    generate_courses()
    generate_exams()
    generate_students()
    link_ta_teachers()
    link_students_courses()
    return Response({"result": "success"})
