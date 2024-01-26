from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from mailing.models import Mailing

def index_home_page(requests):
    context = {
        'name_page': 'Главная'
    }
    return render(requests, 'mailing/home_page.html', context)


class MailingCreateView(CreateView):
    '''класс-контроллер для создания рассылки,работающий с шаблоном mailing_form.html'''
    model = Mailing
    extra_context = {'name_page': 'Создание рассылки'}


class MailingListView(ListView):
    '''класс-контроллер для просмотра списка рассылок, работающий с шаблоном mailing_list.html'''
    model = Mailing
    extra_context = {'name_page': 'Список рассылок'}


class MailingDetailView(DetailView):
    '''класс-контроллер для просмотра рассылки, работающий с шаблоном mailing_detail.html'''
    model = Mailing
    extra_context = {'name_page': 'Карточка рассылки'}


class MailingUpdateView(UpdateView):
    '''класс-контроллер для изменения рассылки,работающий с шаблоном mailing_form.html'''
    model = Mailing
    extra_context = {'name_page': 'Изменение рассылки'}


class MailingDeleteView(DeleteView):
    '''класс-контроллер для удаления рассылки,работающий с шаблоном mailing_confirm_delete.html'''
    model = Mailing
    extra_context = {'name_page': 'Удаление рассылки'}

