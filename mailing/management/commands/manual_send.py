from django.core.management import BaseCommand
from mailing.management.commands.auto_send import auto_send


class Command(BaseCommand):
    def handle(self, *args, **options):
        '''формирует список отправлений: выбирает записи рассылок со статусом 2 - в работе,и рассылает с адреса
        пользователя-спаммера, которому принадлежит рассылка, по адресам его клиентов, каждому персонально'''
        auto_send()

