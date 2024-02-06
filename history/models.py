from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Log(models.Model):
    '''класс-модель для хранения логов об отправлении рассылок]'''
    current_datatime = models.DateTimeField(verbose_name='Текущие дата и время на моменты отправления письма')
    current_date = models.DateField(verbose_name='Текущая дата на момент отправления письма')
    current_time = models.TimeField(verbose_name='Текущее время на момент отправления письма')
    min_datatime = models.DateTimeField(verbose_name='Минимальный временной порог выборки рассылок для отправления')
    max_datatime = models.DateTimeField(verbose_name='Максимальный временной порог выборки рассылок для отправления')
    mailing_id = models.IntegerField(verbose_name='id рассылки')
    mailing_time = models.TimeField(verbose_name='время рассылки')
    mailing_period_id = models.IntegerField(verbose_name='id периода рассылки')
    mailing_data_start = models.DateField(verbose_name='Дата старта рассылки')
    mailing_datatime = models.DateTimeField(verbose_name='Расчетные дата и время отправления письма')
    data_create = models.DateField(verbose_name='дата создания лога', auto_now_add=True)
    smtp_error = models.CharField(max_length=100, verbose_name='Ошибка отправления')

    def __str__(self):
        '''строковое отображение обьекта'''
        return f'{self.current_date}, {self.current_time}, {self.mailing_datatime}, {self.data_create},' \
               f' {self.smtp_error}'

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
        ordering = ['-data_create']
