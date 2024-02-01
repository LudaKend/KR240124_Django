from django.shortcuts import render

from django.views.generic import ListView, DetailView
from blog.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin

class PostListView(LoginRequiredMixin, ListView):
    '''класс-контроллер для просмотра списка статей блога, работающий с шаблоном post_list.html'''
    model = Post
    extra_context = {'name_page': 'Список статей блога'}


class PostDetailView(LoginRequiredMixin, DetailView):
    '''класс-контроллер для просмотра статьи блога, работающий с шаблоном post_detail.html'''
    model = Post
    extra_context = {'name_page': 'Статья блога'}

