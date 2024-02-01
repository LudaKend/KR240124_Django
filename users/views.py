from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from users.models import User
from django.contrib.auth.views import LoginView
from users.forms import UserRegisterForm, UserLoginForm, UserForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class RegisterView(CreateView):
    '''контроллер для регистрации пользователей'''
    model = User
    form_class = UserRegisterForm
    extra_context = {'name_page': 'Регистрация пользователей'}
    success_url = reverse_lazy('users:route_login_users')


class UserLoginView(LoginView):
    '''контроллер, чтобы залогиниться пользователю'''
    model = User
    form_class = UserLoginForm
    extra_context = {'name_page': 'Вход пользователей'}


class UserListView(LoginRequiredMixin, ListView):
    '''класс-контроллер для просмотра списка пользователей-спаммеров, работающий с шаблоном user_list.html'''
    model = User
    extra_context = {'name_page': 'Список пользователей-спаммеров'}


class UserDetailView(LoginRequiredMixin, DetailView):
    '''класс-контроллер для просмотра пользователя-спаммера, работающий с шаблоном user_detail.html'''
    model = User
    extra_context = {'name_page': 'Карточка пользователя-спаммера'}


class UserUpdateView(LoginRequiredMixin, UpdateView):
    '''класс-контроллер для изменения пользователя-спаммера,работающий с шаблоном user_form.html'''
    model = User
    extra_context = {'name_page': 'Изменение пользователя-спаммера'}
    form_class = UserForm

    def get_success_url(self):
        return reverse_lazy('users:route_users_view', args=[self.kwargs.get('pk')])

class UserDeleteView(LoginRequiredMixin, DeleteView):
    '''класс-контроллер для удаления пользователя-спаммера,работающий с шаблоном user_confirm_delete.html'''
    model = User
    extra_context = {'name_page': 'Удаление пользователя-спаммера'}
    success_url = reverse_lazy('users:route_users_list')
