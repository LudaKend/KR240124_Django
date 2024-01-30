from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from client.models import Client
from client.forms import ClientForm
from django.urls import reverse_lazy

class ClientCreateView(CreateView):
    '''класс-контроллер для создания клиента,работающий с шаблоном client_form.html'''
    model = Client
    extra_context = {'name_page': 'Создание клиента'}
    form_class = ClientForm
    success_url = reverse_lazy('client:route_client_list')

    def get_object(self, queryset=None):
        '''метод,чтобы взять email пользователя, который залогинился'''
        return self.request.user

    def form_valid(self, form):
        '''метод чтобы записать email спаммера, которому принадлежит клиент'''
        self.object = form.save()  #сначала нужно сохранить
        self.object.user_email = self.get_object()  #записываю текущего пользователя в качестве автора
        self.object.save()
        return super().form_valid(form)

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
    form_class = ClientForm

    def get_success_url(self):
        return reverse_lazy('client:route_client_view', args=[self.kwargs.get('pk')])


class ClientDeleteView(DeleteView):
    '''класс-контроллер для удаления клиента,работающий с шаблоном client_confirm_delete.html'''
    model = Client
    extra_context = {'name_page': 'Удаление клиента'}
    success_url = reverse_lazy('client:route_client_list')
