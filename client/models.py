from django.db import models
from users.models import User

NULLABLE = {'null': True, 'blank': True}

class Client(models.Model):
    '''класс-модель для получателей рассылок'''
    client_name = models.CharField(max_length=100, verbose_name='Имя клиента')
    client_email = models.EmailField(verbose_name='email клиента', **NULLABLE)
    user_email = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='email пользователя-спаммера', **NULLABLE)
    is_active = models.BooleanField(verbose_name='действителен', default=True)
    data_create = models.DateField(verbose_name='дата создания', auto_now_add=True, **NULLABLE)
    data_change = models.DateField(verbose_name='дата изменения', auto_now=True, **NULLABLE)

    def __str__(self):
        '''строковое отображение обьекта'''
        return f'{self.client_name}, {self.client_email}, {self.is_active}, {self.user_email}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['-data_create', '-data_change']
