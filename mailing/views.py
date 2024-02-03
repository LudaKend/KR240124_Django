from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from mailing.models import Mailing
from mailing.forms import MailingForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404


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
        self.object.user_email = self.get_object()  #записываю текущего пользователя в качестве автора
        self.object.save()
        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    '''класс-контроллер для изменения рассылки,работающий с шаблоном mailing_form.html'''
    model = Mailing
    extra_context = {'name_page': 'Изменение рассылки'}
    form_class = MailingForm
    permission_required = 'mailing.change_mailing'

    def get_object(self, queryset=None):
        '''изменять рассылку можно только автору'''
        self.object = super().get_object(queryset)
        if self.object.user_email != self.request.user:
            raise Http404('Изменения доступны только автору')
        return self.object

    def get_success_url(self):
        return reverse_lazy('mailing:route_mailing_view', args=[self.kwargs.get('pk')])


class MailingListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    '''класс-контроллер для просмотра списка рассылок, работающий с шаблоном mailing_list.html'''
    model = Mailing
    extra_context = {'name_page': 'Список рассылок'}
    permission_required = 'mailing.view_mailing'

    def get_object(self, queryset=None):
        '''метод,чтобы взять email пользователя, который залогинился'''
        # self.object = super().get_object(queryset)
        # user = self.request.user
        # is_moderator = user.groups.filter(name='moderator').exists()
        # if is_moderator:
        return self.request.user

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        user = self.get_object()
        if user.is_staff:
            return queryset
        else:
            queryset = queryset.filter(user_email=self.get_object())
            return queryset


class MailingDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    '''класс-контроллер для просмотра рассылки, работающий с шаблоном mailing_detail.html'''
    model = Mailing
    extra_context = {'name_page': 'Карточка рассылки'}
    permission_required = 'mailing.view_mailing'

    def get_object(self, queryset=None):
        '''просматривать рассылку можно только автору'''
        self.object = super().get_object(queryset)
        if self.object.user_email != self.request.user:
            raise Http404('Просмотр доступен только автору')
        return self.object


class MailingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    '''класс-контроллер для удаления рассылки,работающий с шаблоном mailing_confirm_delete.html'''
    model = Mailing
    extra_context = {'name_page': 'Удаление рассылки'}
    success_url = reverse_lazy('mailing:route_mailing_list')
    permission_required = 'mailing.delete_mailing'

    def get_object(self, queryset=None):
        '''удалять рассылку можно только автору'''
        self.object = super().get_object(queryset)
        if self.object.user_email != self.request.user:
            raise Http404('Удаление рассылки доступно только автору')
        return self.object

def index_mailing_stop(requests, pk):
    '''отключение рассылки'''
    temp_mailing = get_object_or_404(Mailing, pk=pk)
    if temp_mailing.status_id == 2:
        temp_mailing.status_id = 3
        temp_mailing.save()
    return redirect(reverse('mailing:route_mailing_list'))
