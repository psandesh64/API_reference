from .models import Course, Instructor
from rest_framework import serializers

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['id','url','title','rating','instructor']

class InstructorSerializer(serializers.HyperlinkedModelSerializer):
    courses = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='course-detail')
    class Meta:
        model = Instructor
        fields = ['id','name','email','courses']