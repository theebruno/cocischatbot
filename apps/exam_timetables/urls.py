"""
"""
from django.urls import path, re_path
from apps.exam_timetables import views

urlpatterns = [

    # timetables/
    # path('class/', views.ExamTimetableListView.as_view(), name='class_timetables'),
    path('exam/', views.ExamTimetableListView.as_view(), name='exam_timetables'),
]
