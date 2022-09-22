from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'location',
        'event_date',
        # 'event_time',
        'organiser',
        'updated',
        'timestamp',
        )
    search_fields = ('name', 'organiser')


admin.site.register(Event, EventAdmin)
