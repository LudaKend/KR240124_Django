from django.shortcuts import render
from django.views.generic import CreateView
from users.models import User
from django.contrib.auth.views import LoginView
from users.forms import UserRegisterForm, UserLoginForm


class RegisterView(CreateView):
    '''контроллер для регистрации пользователя'''
    model = User
    form_class = UserRegisterForm


class UserLoginView(LoginView):
    '''контроллер, чтобы залогиниться пользователю'''
    model = User
    form_class = UserLoginForm
