from django.contrib import admin
from .models import CourseUnit


class CourseUnitAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'code',
        'lecturer',
        'updated',
        'timestamp',
        )
    search_fields = ('name', )


admin.site.register(CourseUnit, CourseUnitAdmin)
