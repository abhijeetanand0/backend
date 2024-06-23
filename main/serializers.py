from rest_framework import serializers
from .models import Course, Exam, Student


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'code', 'semester', 'year']


class ExamSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()

    class Meta:
        model = Exam
        fields = ['id', 'title', 'start_time', 'end_time', 'date']

    def get_date(self, obj):
        return obj.start_time.strftime('%d %B, %Y').replace(' 0', ' ')



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'year', 'department', 'roll']
