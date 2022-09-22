from django.contrib import admin
from .models import EventOrganiser


class EventOrganiserAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'updated',
        'timestamp',
        )
    search_fields = ('name', )


admin.site.register(EventOrganiser, EventOrganiserAdmin)
