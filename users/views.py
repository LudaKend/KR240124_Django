from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from users.models import User
from django.contrib.auth.views import LoginView
from users.forms import UserRegisterForm, UserLoginForm, UserForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class RegisterView(CreateView):
    '''контроллер для регистрации пользователей'''
    model = User
    form_class = UserRegisterForm
    extra_context = {'name_page': 'Регистрация пользователей'}
    success_url = reverse_lazy('users:route_login_users')

    def form_valid(self, form):
        self.object = form.save()
        # нужно при регистрации пользователю присвоить группу пономочий spammer
        self.object.groups.add(1)  # в таблице users_user_group есть только id, поэтому так
        return super().form_valid(form)


class UserLoginView(LoginView):
    '''контроллер, чтобы залогиниться пользователю'''
    model = User
    form_class = UserLoginForm
    extra_context = {'name_page': 'Вход пользователей'}


class UserListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    '''класс-контроллер для просмотра списка пользователей-спаммеров, работающий с шаблоном user_list.html'''
    model = User
    extra_context = {'name_page': 'Список пользователей-спаммеров'}
    permission_required = 'users.view_user'

class UserDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    '''класс-контроллер для просмотра пользователя-спаммера, работающий с шаблоном user_detail.html'''
    model = User
    extra_context = {'name_page': 'Карточка пользователя-спаммера'}
    permission_required = 'users.view_user'

class UserUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    '''класс-контроллер для изменения пользователя-спаммера,работающий с шаблоном user_form.html'''
    model = User
    extra_context = {'name_page': 'Изменение пользователя-спаммера'}
    form_class = UserForm
    permission_required = 'users.add_user'

    def get_success_url(self):
        return reverse_lazy('users:route_users_view', args=[self.kwargs.get('pk')])

class UserDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    '''класс-контроллер для удаления пользователя-спаммера,работающий с шаблоном user_confirm_delete.html'''
    model = User
    extra_context = {'name_page': 'Удаление пользователя-спаммера'}
    success_url = reverse_lazy('users:route_users_list')
    permission_required = 'users.add_user'

def index_deactivate(requests, pk):
    '''деактивация пользователя'''
    temp_user = get_object_or_404(User, pk=pk)
    if temp_user.is_active:
        temp_user.is_active = False
    else:
        temp_user.is_active = True
    temp_user.save()
    return redirect(reverse('users:route_users_list'))
