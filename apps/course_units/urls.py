"""
"""
from django.urls import path, re_path
from apps.course_units import views

urlpatterns = [

    # course_units/
    path('list/', views.CourseUnitListView.as_view(), name='course_units'),
    # path('exam/', views.CourseUnitListView.as_view(), name='exam_timetables'),
]
