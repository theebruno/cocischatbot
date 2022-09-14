from django.contrib import admin
from .models import ClassTimetable


class ClassTimetableAdmin(admin.ModelAdmin):
    list_display = (
        'course_unit_name',
        'course_unit_code',
        'course_unit_lecturer',
        'days_of_the_week',
        'time_of_class',
        'timestamp',
        'updated',
        )
    search_fields = ('course_unit_name', 'course_unit_code', )


admin.site.register(ClassTimetable, ClassTimetableAdmin)
