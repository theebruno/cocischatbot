from django.contrib import admin
from .models import LecturerOffice


class LecturerOfficeAdmin(admin.ModelAdmin):
    list_display = (
        'office_number',
        'block',
        'timestamp',
        'updated',
        )
    search_fields = ('office_number', )


admin.site.register(LecturerOffice, LecturerOfficeAdmin)
