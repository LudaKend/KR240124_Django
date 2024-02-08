from django.urls import path
from history.views import HistoryListView
from history.apps import HistoryConfig

app_name = HistoryConfig.name

urlpatterns = [
    path('list_view/', HistoryListView.as_view(), name='route_history_report'),
]
