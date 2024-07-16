from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static


urlpatterns = [
    # path(''),
    path('get_courses/', views.get_courses, name='get_courses'),
    path('course/<int:course_id>/exams', views.get_exams, name='get_exams'),
    path('course/<int:course_id>/exam/<int:exam_id>/students', views.get_students, name='get_students'),
    path('student/<str:roll>', views.get_student_details, name='get_student'),
    path('mark/exam/<int:exam_id>/student/<int:student_id>', views.mark_attendance, name='mark_attendance'),
    path('toilet/exam/<int:exam_id>', views.get_toilet_details, name='get_toilet_details'),
    path('toilet/create/exam/<int:exam_id>/student/<str:roll>', views.add_toilet_entry, name='add_toilet_entry'),
    path('toilet/clear/exam/<int:exam_id>', views.clear_toilet, name='clear_toilet'),

    # path('profile_pic/student/<int:roll>', views.get_profile_pic, name='get_profile_pic'),
    # path('get_')



# GENERATE DATABASE VALUES
    path('generate/', views.generate, name='generate')
]

