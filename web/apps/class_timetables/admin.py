from django.contrib import admin
from .models import ClassTimetable


class ClassTimetableAdmin(admin.ModelAdmin):
    list_display = (
        'timestamp',
    )


admin.site.register(ClassTimetable, ClassTimetableAdmin)
