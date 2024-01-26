from django.urls import path
from mailing.views import index_home_page
from mailing.apps import MailingConfig

app_name = MailingConfig.name

urlpatterns = [
    path('', index_home_page, name='route_home_page'),
]