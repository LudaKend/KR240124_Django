from django.contrib import admin
from history.models import Log


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('id', 'current_datatime', 'mailing_id', 'mailing_time', 'mailing_period_id', 'mailing_data_start',
                    'mailing_datatime', 'data_create', 'smtp_error')
    list_filter = ('current_date', 'mailing_id', 'id', 'mailing_period_id',)
    search_fields = ('current_date', 'mailing_id', 'id', 'mailing_period_id',)
