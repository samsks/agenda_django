from django.contrib import admin

from core_app.models import Event

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'event_date', 'create_date')
    list_filter = ('user', 'event_date')


admin.site.register(Event, EventAdmin)
