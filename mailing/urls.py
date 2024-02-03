from django.urls import path
from mailing.views import index_home_page, index_mailing_stop
from mailing.apps import MailingConfig
from mailing.views import MailingCreateView, MailingListView, MailingDetailView, MailingUpdateView, MailingDeleteView


app_name = MailingConfig.name

urlpatterns = [
    path('', index_home_page, name='route_home_page'),
    path('create/', MailingCreateView.as_view(), name='route_mailing_create'),
    path('list_view/', MailingListView.as_view(), name='route_mailing_list'),
    path('view/<int:pk>/', MailingDetailView.as_view(), name='route_mailing_view'),
    path('update/<int:pk>/', MailingUpdateView.as_view(), name='route_mailing_update'),
    path('delete/<int:pk>/', MailingDeleteView.as_view(), name='route_mailing_delete'),
    path('mailing_stop/<int:pk>/', index_mailing_stop, name='route_mailing_stop'),
]
