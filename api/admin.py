from django.contrib import admin
from .models import Readings, Dustbins


# Register your models here.
# This helps create extra admin options for easy administration
class ApiAppAdmin(admin.ModelAdmin):
    list_display = ['dustbin_id', 'level', 'recorded_on']
    list_display_links = ['level']
    list_filter = ['dustbin_id', 'recorded_on', 'level']
    search_fields = ['id']

    class Meta:
        model = Dustbins


class DashboardAppAdmin(admin.ModelAdmin):
    list_display = ['id', 'location_name', 'created_on', 'updated_on']
    list_display_links = ['id', 'location_name', 'created_on', 'updated_on']
    list_filter = ['id', 'location_name', 'created_on', 'updated_on']
    search_fields = ['id']

    class Meta:
        model = Readings


admin.site.register(Readings, ApiAppAdmin)
admin.site.register(Dustbins, DashboardAppAdmin)
