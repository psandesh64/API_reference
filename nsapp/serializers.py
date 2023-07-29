from .models import Course, Instructor
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class InstructorSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)
    class Meta:
        model = Instructor
        fields = '__all__'

# class CourseSerializer(serializers.ModelSerializer):
#     instructor = InstructorSerializer(read_only=True)
#     class Meta:
#         model = Course
#         fields = '__all__'