from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'department',
        'updated',
        'timestamp',
        )
    search_fields = ('name', 'code')


admin.site.register(Course, CourseAdmin)
