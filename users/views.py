from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from users.models import User
from django.contrib.auth.views import LoginView
from users.forms import UserRegisterForm, UserLoginForm


class RegisterView(CreateView):
    '''контроллер для регистрации пользователя-спаммера'''
    model = User
    form_class = UserRegisterForm


class UserLoginView(LoginView):
    '''контроллер, чтобы залогиниться пользователю-спаммеру'''
    model = User
    form_class = UserLoginForm

class UserListView(ListView):
    '''класс-контроллер для просмотра списка пользователей-спаммеров, работающий с шаблоном user_list.html'''
    model = User
    extra_context = {'name_page': 'Список пользователей-спаммеров'}


class UserDetailView(DetailView):
    '''класс-контроллер для просмотра пользователя-спаммера, работающий с шаблоном user_detail.html'''
    model = User
    extra_context = {'name_page': 'Карточка пользователя-спаммера'}


class UserUpdateView(UpdateView):
    '''класс-контроллер для изменения пользователя-спаммера,работающий с шаблоном user_form.html'''
    model = User
    extra_context = {'name_page': 'Изменение пользователя-спаммера'}


class UserDeleteView(DeleteView):
    '''класс-контроллер для удаления пользователя-спаммера,работающий с шаблоном user_confirm_delete.html'''
    model = User
    extra_context = {'name_page': 'Удаление пользователя-спаммера'}

