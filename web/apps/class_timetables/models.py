from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class ClassTimetable(models.Model):
    file_uploaded = models.FileField(upload_to='class_timetables/')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Entry 1"
