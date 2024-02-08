from django.views.generic import ListView
from history.models import Log
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class HistoryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    '''класс-контроллер для просмотра списка логов, работающий с шаблоном log_list.html'''
    model = Log
    extra_context = {'name_page': 'Отчет о проведенных рассылках'}
    permission_required = 'history.view_log'
