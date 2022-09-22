"""
"""
from django.urls import path, re_path
from django.views.generic import TemplateView

from apps.class_timetables import views

# from .jayson import upload_timetable_logic

urlpatterns = [

    # timetables/
    path('class/', views.ClassTimetableListView.as_view(), name='class_timetables'),
    path('class/upload_template/',
         views.TemplateView.as_view(template_name='class_timetables/class_timetables.html'),
         name='class_timetable_upload_template'),
    # path('class/upload/', upload_timetable_logic, name='class_timetable_upload'),
]
