# Generated by Django 4.2.7 on 2024-02-05 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_datatime', models.DateTimeField(verbose_name='Текущие дата и время на моменты отправления письма')),
                ('current_date', models.DateField(verbose_name='Текущая дата на момент отправления письма')),
                ('current_time', models.TimeField(verbose_name='Текущее время на момент отправления письма')),
                ('min_datatime', models.DateTimeField(verbose_name='Минимальный временной порог выборки рассылок для отправления')),
                ('max_datatime', models.DateTimeField(verbose_name='Максимальный временной порог выборки рассылок для отправления')),
                ('mailing_id', models.IntegerField(verbose_name='id рассылки')),
                ('mailing_time', models.TimeField(verbose_name='время рассылки')),
                ('mailing_period_id', models.IntegerField(verbose_name='id периода рассылки')),
                ('mailing_data_start', models.DateField(verbose_name='Дата старта рассылки')),
                ('mailing_datatime', models.DateTimeField(verbose_name='Расчетные дата и время отправления письма')),
                ('data_create', models.DateField(auto_now_add=True, verbose_name='дата создания лога')),
                ('smtp_error', models.CharField(max_length=100, verbose_name='Ошибка отправления')),
            ],
            options={
                'verbose_name': 'Лог',
                'verbose_name_plural': 'Логи',
                'ordering': ['-data_create'],
            },
        ),
    ]
