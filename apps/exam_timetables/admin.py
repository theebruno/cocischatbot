from django.contrib import admin
from .models import ExamTimetable


class ExamTimetableAdmin(admin.ModelAdmin):
    list_display = (
        'course_unit_name',
        'course_unit_code',
        'room_number',
        'block',
        'exam_date',
        'timestamp',
        'updated',
        )
    search_fields = ('course_unit_name', 'course_unit_code' )


admin.site.register(ExamTimetable, ExamTimetableAdmin)
