from django.shortcuts import render
from rest_framework import generics
# from .serializers import InstructorSerializer, CourseSerializer
from .hyperlinked_serializers import InstructorSerializer, CourseSerializer
from .models import Instructor,Course

from rest_framework.permissions import IsAuthenticated,IsAdminUser,BasePermission
from rest_framework.authentication import BasicAuthentication, TokenAuthentication

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create your views here.

class WriteByAdminOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        print(request.user, 'has permission')
        user = request.user
        if request.method == 'GET':
            return True
        
        if request.method == 'POST' or request.method == 'PUT' or request.method == 'DELETE':
            if user.is_superuser:
                return True
        return False
    

class InstructorListView(generics.ListCreateAPIView):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()

class InstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()

# Authentication for authorized user(session authentication)
# class CourseListView(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = CourseSerializer
#     queryset = Course.objects.all()

# Authentication by entering username and password, with different access to authorization
# class CourseListView(generics.ListCreateAPIView):
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated ,WriteByAdminOnlyPermission]
#     serializer_class = CourseSerializer
#     queryset = Course.objects.all()

# Authentication by entering token

# users = User.objects.all()
# for user in users:
#     token = Token.objects.get_or_create(user=user)
#     print(token)

''' while sending request through postman in Headers give key "Authorization" and value
"Token 13501bf16eab7e149bdfe58d4c9fb9785e996b70" '''

# class CourseListView(generics.ListCreateAPIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated ,WriteByAdminOnlyPermission]
#     serializer_class = CourseSerializer
#     queryset = Course.objects.all()

# Authentication by JWT token
'''pip install djangorestframework-simplejwt'''
''' while sending request through postman in Headers give key "Authorization" and value
"Bearer 13501bf16eab7e149bdfe58d4c9fb9785e996b70" '''

class CourseListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated ,WriteByAdminOnlyPermission]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()