"""
"""
from django.urls import path, re_path
from apps.courses import views

urlpatterns = [
    # courses/
    path('create/', views.CourseCreateView.as_view(), name='courses_create'),
    path('list/', views.CourseListView.as_view(), name='courses'),
]
