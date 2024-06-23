from django.urls import path
from . import views

urlpatterns = [
    # path(''),
    path('get_courses/', views.get_courses, name='get_courses'),
    path('course/<int:course_id>/exams', views.get_exams, name='get_exams'),
    path('course/<int:course_id>/exam/<int:exam_id>/students', views.get_students, name='get_students'),
    path('student/<str:roll>', views.get_student_details, name='get_student'),
    path('mark/exam/<int:exam_id>/student/<int:student_id>', views.mark_attendance, name='mark_attendance'),
    # path('get_')



# GENERATE DATABASE VALUES
    path('generate/', views.generate, name='generate')
]
