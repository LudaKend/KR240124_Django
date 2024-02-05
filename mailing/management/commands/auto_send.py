import smtplib

from mailing.models import Mailing
from client.models import Client
from django.core.mail import send_mail
import datetime
from datetime import datetime, timedelta

def auto_send():
    '''формирует список отправлений: выбирает записи рассылок со статусом 2 - в работе,и рассылает с адреса
    пользователя-спаммера, которому принадлежит рассылка, по адресам его клиентов, каждому персонально'''
    mailing_list = Mailing.objects.filter(status='2')
    print(f'все майлинги со статусом в работе:', mailing_list)  # для отладки
    current_datatime = datetime.now()      # текущая дата и время
    print(f'текущая дата и время: {current_datatime}')     # для отладки
    current_date = datetime.now().date()  # только текущяя дата
    print(f'текущая дата: {current_date}')         # для отладки
    current_time = datetime.now().time()   # только текущее время
    print(f'текущее время: {current_time}')         # для отладки
    min_datatime = current_datatime - timedelta(minutes=30)
    print(f'min_datatime: {min_datatime}')          # для отладки
    max_datatime = current_datatime + timedelta(minutes=30)
    print(f'max_datatime: {max_datatime}')          # для отладки
    print()
    for item in mailing_list:
        # надо получить datatime отправки рассылки, зная data_start, time, period
        print(f'данные из mailinga: {item.time, item.period, item.period_id, item.data_start}')   # для отладки
        if item.period_id == 1 and item.data_start <= current_date:     #если рассылка ежедневная и дата старта настала
            mailing_datatime = datetime.combine(current_date, item.time)  # собираем datatime отправки
            print(f'полученный mailing_datatime ежедневной рассылки: {mailing_datatime}')         # для отладки
            if min_datatime < mailing_datatime <= max_datatime:
                spammer_email = item.user_email
                client_list = Client.objects.filter(user_email=spammer_email)
                print(f'client_list', client_list)  # для отладки
                for client in client_list:
                    try:
                        send_mail(subject=item.subject, message=item.mailing_text,
                                      from_email=spammer_email, recipient_list=[client.client_email, ])
                    except (smtplib.SMTPRecipientsRefused, smtplib.SMTPDataError) as smtp_error:
                        print(smtp_error)
            else:
                print('время отправки рассылки вне текущего интервала')   # для отладки
                print()

        elif item.period_id == 2 and item.data_start <= current_date:   #если рассылка еженедельная и дата старта настала
            current_week_day = datetime.today().strftime("%w")  #берем текущий день недели
            print(f'текущий день недели: {current_week_day}')   # для отладки
            #print(type(current_week_day))
            start_week_day = item.data_start.strftime("%w")     #берем день недели из даты старта в рассылке
            print(f'день недели из data_start рассылки: {start_week_day}')    # для отладки
            #print(type(start_week_day))
            if int(current_week_day) == int(start_week_day):
                mailing_datatime = datetime.combine(current_date, item.time)  # собираем datatime отправки
                print(f'полученный mailing_datatime еженедельной рассылки: {mailing_datatime}')    # для отладки
                if min_datatime < mailing_datatime <= max_datatime:
                    spammer_email = item.user_email
                    client_list = Client.objects.filter(user_email=spammer_email)
                    print(f'client_list', client_list)  # для отладки
                    for client in client_list:
                        try:
                            send_mail(subject=item.subject, message=item.mailing_text,
                                          from_email=spammer_email, recipient_list=[client.client_email, ])
                        except (smtplib.SMTPRecipientsRefused, smtplib.SMTPDataError) as smtp_error:
                            print(smtp_error)
                else:
                    print('время отправки рассылки вне текущего интервала')      # для отладки
                    print()

        elif item.period_id == 3 and item.data_start <= current_date:  # если рассылка ежемесячная и дата старта настала
            current_month_year = datetime.today().strftime("%m.%Y")  #берем текущий месяц и год
            print(current_month_year)           # для отладки
            mailing_day = item.data_start.strftime("%d")          #берем число из даты старта в рассылке
            print(mailing_day)                  # для отладки
            mailing_data = mailing_day + '.' + current_month_year
            print(mailing_data)                 # для отладки
            #print(type(mailing_data))
            try:
                mailing_data = datetime.strptime(mailing_data, "%d.%m.%Y")
            except:
                print('такой даты нет')      # для отладки
                mailing_day = int(mailing_day) - 1    #31-1=30
                print(mailing_day)           # для отладки
                mailing_data = str(mailing_day) + '.' + current_month_year
                print(mailing_data)          # для отладки
                #print(type(mailing_data))
                try:
                    mailing_data = datetime.strptime(mailing_data, "%d.%m.%Y")
                except:
                    print('такой даты нет')              # для отладки
                    mailing_day = int(mailing_day) - 1   #30-1=29
                    print(mailing_day)                   # для отладки
                    mailing_data = str(mailing_day) + '.' + current_month_year
                    print(mailing_data)                  # для отладки
                    #print(type(mailing_data))
                    try:
                        mailing_data = datetime.strptime(mailing_data, "%d.%m.%Y")
                    except:
                        print('такой даты нет')              # для отладки
                        mailing_day = int(mailing_day) - 1   #29-1=28
                        print(mailing_day)                   # для отладки
                        mailing_data = str(mailing_day) + '.' + current_month_year
                        print(mailing_data)                  # для отладки
                        #print(type(mailing_data))
                        mailing_data = datetime.strptime(mailing_data, "%d.%m.%Y")
                        print(mailing_data)                  # для отладки
                        print(type(mailing_data))            # для отладки
            mailing_datatime = datetime.combine(mailing_data, item.time)  # собираем datatime отправки
            print(f'полученный mailing_datatime ежемесячной рассылки: {mailing_datatime}')    # для отладки
            if min_datatime < mailing_datatime <= max_datatime:
                spammer_email = item.user_email
                client_list = Client.objects.filter(user_email=spammer_email)
                print(f'client_list', client_list)        # для отладки
                for client in client_list:
                    try:
                        send_mail(subject=item.subject, message=item.mailing_text, from_email=spammer_email,
                                      recipient_list=[client.client_email, ])
                    except (smtplib.SMTPRecipientsRefused, smtplib.SMTPDataError) as smtp_error:
                        print(smtp_error)
            else:
                print('время отправки рассылки вне текущего интервала')        # для отладки
                print()

