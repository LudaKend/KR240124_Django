from django.db import models
from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Mailing(models.Model):
    '''класс-модель для рассылок'''
    subject = models.CharField(max_length=100, verbose_name='Тема письма')
    mailing_text = models.TextField(verbose_name='Текст письма', **NULLABLE)
    user_email = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='email автора рассылки', **NULLABLE)
    time = models.TimeField(verbose_name='время отправки', **NULLABLE)
    data_start = models.DateField(verbose_name='дата старта рассылки', **NULLABLE)
    period = models.ForeignKey('Period', on_delete=models.CASCADE, verbose_name='периодичность', **NULLABLE)
    status = models.ForeignKey('StatusMailing', on_delete=models.CASCADE, verbose_name='статус', default=1)
    data_create = models.DateField(verbose_name='дата создания', auto_now_add=True, **NULLABLE)
    data_change = models.DateField(verbose_name='дата изменения', auto_now=True, **NULLABLE)


    def __str__(self):
        '''строковое отображение обьекта'''
        return f'{self.subject}, {self.user_email}, {self.time}, {self.period}, {self.status}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ['-data_create', '-data_change']


class Period(models.Model):
    '''вспомогательный справочник для выбора периодичности запуска рассылок'''
    period = models.CharField(max_length=100, verbose_name='периодичность')

    def __str__(self):
        '''строковое отображение обьекта'''
        return f'{self.period}'

    class Meta:
        verbose_name = 'Период'
        verbose_name_plural = 'Периоды'


class StatusMailing(models.Model):
    '''вспомогательный справочник со статусами рассылок'''
    status = models.CharField(max_length=100, verbose_name='статус')

    def __str__(self):
        '''строковое отображение обьекта'''
        return f'{self.status}'

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
