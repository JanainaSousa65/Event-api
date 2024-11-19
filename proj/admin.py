from django.contrib import admin
from proj.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'start_date', 'end_date',)
    search_fields = ('name',)

# Register your models here.
admin.site.register(Event, EventAdmin)