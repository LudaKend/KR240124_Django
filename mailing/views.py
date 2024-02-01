from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from mailing.models import Mailing
from mailing.forms import MailingForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

def index_home_page(requests):
    context = {
        'name_page': 'Главная'
    }
    return render(requests, 'mailing/home_page.html', context)


class MailingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    '''класс-контроллер для создания рассылки,работающий с шаблоном mailing_form.html'''
    model = Mailing
    extra_context = {'name_page': 'Создание рассылки'}
    form_class = MailingForm
    success_url = reverse_lazy('mailing:route_mailing_list')
    permission_required = 'mailing.add_mailing'

    def get_object(self, queryset=None):
        '''метод,чтобы взять email пользователя, который залогинился'''
        return self.request.user

    def form_valid(self, form):
        '''метод чтобы записать email автора рассылки'''
        self.object = form.save()        #сначала нужно сохранить
        # temp_user = self.get_object()         #для отладки
        # print(temp_user)
        self.object.user_email = self.get_object()  #записываю текущего пользователя в качестве автора
        self.object.save()
        return super().form_valid(form)


class MailingListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    '''класс-контроллер для просмотра списка рассылок, работающий с шаблоном mailing_list.html'''
    model = Mailing
    extra_context = {'name_page': 'Список рассылок'}
    permission_required = 'mailing.view_mailing'

class MailingDetailView(LoginRequiredMixin, DetailView):
    '''класс-контроллер для просмотра рассылки, работающий с шаблоном mailing_detail.html'''
    model = Mailing
    extra_context = {'name_page': 'Карточка рассылки'}
    permission_required = 'mailing.view_mailing'

class MailingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    '''класс-контроллер для изменения рассылки,работающий с шаблоном mailing_form.html'''
    model = Mailing
    extra_context = {'name_page': 'Изменение рассылки'}
    form_class = MailingForm
    #success_url = reverse_lazy('mailing:route_mailing_list')
    permission_required = 'mailing.change_mailing'

    def get_success_url(self):
        return reverse_lazy('mailing:route_mailing_view', args=[self.kwargs.get('pk')])


class MailingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    '''класс-контроллер для удаления рассылки,работающий с шаблоном mailing_confirm_delete.html'''
    model = Mailing
    extra_context = {'name_page': 'Удаление рассылки'}
    success_url = reverse_lazy('mailing:route_mailing_list')
    permission_required = 'mailing.delete_mailing'
