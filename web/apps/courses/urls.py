"""
"""
from django.urls import path, re_path

from apps.courses import views
from .jayson import json_courses

urlpatterns = [
    # courses/
    path('create/', views.CourseCreateView.as_view(), name='courses_create'),
    path('list/', views.CourseListView.as_view(), name='courses'),

    path('list/json/', json_courses, name='json_courses'),
]
