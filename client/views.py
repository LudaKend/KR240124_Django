from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from client.models import Client
from client.forms import ClientForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404

class ClientCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    '''класс-контроллер для создания клиента,работающий с шаблоном client_form.html'''
    model = Client
    extra_context = {'name_page': 'Создание клиента'}
    form_class = ClientForm
    success_url = reverse_lazy('client:route_client_list')
    permission_required = 'client.add_client'

    def get_object(self, queryset=None):
        '''метод,чтобы взять email пользователя, который залогинился'''
        return self.request.user

    def form_valid(self, form):
        '''метод чтобы записать email спаммера, которому принадлежит клиент'''
        self.object = form.save()  #сначала нужно сохранить
        self.object.user_email = self.get_object()  #записываю текущего пользователя в качестве автора
        self.object.save()
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    '''класс-контроллер для изменения клиента,работающий с шаблоном client_form.html'''
    model = Client
    extra_context = {'name_page': 'Изменение клиента'}
    form_class = ClientForm
    permission_required = 'client.change_client'

    def get_object(self, queryset=None):
        '''изменять клиента можно только автору'''
        self.object = super().get_object(queryset)
        if self.object.user_email != self.request.user:
            raise Http404('Изменения доступны только автору')
        return self.object

    def get_success_url(self):
        return reverse_lazy('client:route_client_view', args=[self.kwargs.get('pk')])


class ClientListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    '''класс-контроллер для просмотра списка клиентов, работающий с шаблоном client_list.html'''
    model = Client
    extra_context = {'name_page': 'Список клиентов'}
    permission_required = 'client.view_client'

    def get_object(self, queryset=None):
        '''метод,чтобы взять email пользователя, который залогинился'''
        return self.request.user

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(user_email=self.get_object())
        return queryset

class ClientDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    '''класс-контроллер для просмотра клиента, работающий с шаблоном client_detail.html'''
    model = Client
    extra_context = {'name_page': 'Карточка клиента'}
    permission_required = 'client.view_client'

    def get_object(self, queryset=None):
        '''просматривать клиента можно только автору'''
        self.object = super().get_object(queryset)
        if self.object.user_email != self.request.user:
            raise Http404('Просмотр данных о клиенте доступен только автору')
        return self.object


class ClientDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    '''класс-контроллер для удаления клиента,работающий с шаблоном client_confirm_delete.html'''
    model = Client
    extra_context = {'name_page': 'Удаление клиента'}
    success_url = reverse_lazy('client:route_client_list')
    permission_required = 'client.delete_client'

    def get_object(self, queryset=None):
        '''удалить клиента можно только автору'''
        self.object = super().get_object(queryset)
        if self.object.user_email != self.request.user:
            raise Http404('Изменения доступны только автору')
        return self.object
