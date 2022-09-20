"""
"""
from django.urls import path, re_path
from apps.class_timetables import views

urlpatterns = [

    # timetables/
    path('class/', views.ClassTimetableListView.as_view(), name='class_timetables'),
    # path('exam/', views.ClassTimetableListView.as_view(), name='exam_timetables'),
]
