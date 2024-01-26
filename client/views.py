from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from client.models import Client


class ClientCreateView(CreateView):
    '''класс-контроллер для создания клиента,работающий с шаблоном client_form.html'''
    model = Client
    extra_context = {'name_page': 'Создание клиента'}


class ClientListView(ListView):
    '''класс-контроллер для просмотра списка клиентов, работающий с шаблоном client_list.html'''
    model = Client
    extra_context = {'name_page': 'Список клиентов'}


class ClientDetailView(DetailView):
    '''класс-контроллер для просмотра клиента, работающий с шаблоном client_detail.html'''
    model = Client
    extra_context = {'name_page': 'Карточка клиента'}


class ClientUpdateView(UpdateView):
    '''класс-контроллер для изменения клиента,работающий с шаблоном client_form.html'''
    model = Client
    extra_context = {'name_page': 'Изменение клиента'}


class ClientDeleteView(DeleteView):
    '''класс-контроллер для удаления клиента,работающий с шаблоном client_confirm_delete.html'''
    model = Client
    extra_context = {'name_page': 'Удаление клиента'}

