from django.contrib import admin
from mailing.models import Mailing, Period, StatusMailing


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'user_email', 'time', 'period', 'status', 'data_create', 'data_change')
    list_filter = ('user_email', 'time', 'status',)
    search_fields = ('subject', 'user_email', 'time', 'period',)


@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ('id', 'period')
    list_filter = ('period',)
    search_fields = ('period',)

@admin.register(StatusMailing)
class StatusMailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')
    list_filter = ('status',)
    search_fields = ('status',)
