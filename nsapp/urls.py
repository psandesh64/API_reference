from django.contrib import admin
from django.urls import path
from . import viewspermisssion

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('instructors/',viewspermisssion.InstructorListView.as_view()),
    path('courses/',viewspermisssion.CourseListView.as_view()),
    path('courses/<int:pk>',viewspermisssion.CourseDetailView.as_view(),name='course-detail'),
    path('instructors/<int:pk>',viewspermisssion.InstructorDetailView.as_view(),name='instructor-detail'),
    # path('auth/login/',obtain_auth_token,name='create-token'),                  #for generating token for entered user
    path('auth/login/',TokenObtainPairView.as_view(),name='create-token'),                  #for generating jwt token for entered user
    path('auth/token/refresh',TokenRefreshView.as_view(),name='refresh-token'),                  #for generating token for entered refresh value
]