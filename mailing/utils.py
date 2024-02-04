from mailing.models import Mailing
from blog.models import Post
from client.models import Client

def count_mailing():
    '''для подсчета количества рассылок'''
    quantity_mailing = 0
    mailing_list = Mailing.objects.all()
    for item in mailing_list:
        quantity_mailing += 1
    return quantity_mailing

def count_active_mailing():
    '''для подсчета количества активных рассылок'''
    quantity_active_mailing = 0
    mailing_list = Mailing.objects.filter(status='2')
    for item in mailing_list:
        quantity_active_mailing += 1
    return quantity_active_mailing

def get_last_post():
    '''выбирает 3 последние статьи блога'''
    post_list = Post.objects.filter(is_published=True)
    print(post_list)
    post_id_list = []  #соберем список id опубликованных статей
    for item in post_list:
        post_id_list.append(item.id)
    print(post_id_list)
    post_id_list.sort(reverse=True) #сортируем по убыванию
    print(post_id_list)
    last_post_id = post_id_list[:3]  #нужны 3 последние id
    last_post_list = []
    for item in last_post_id:
        last_post = Post.objects.filter(id=item)
        last_post_list.append(last_post)  #собираем список из последних постов
    return last_post_list

def count_uniq_clients():
    '''считает количество уникальных клиентов сервиса'''
    client_list = Client.objects.filter(is_active=True)
    client_email_list = []  #собираю емейлы клиентов в список
    for item in client_list:
        client_email_list.append(item.client_email)
    unig_client_set = set(client_email_list)
    return len(unig_client_set)
