from django.shortcuts import render

from django.views.generic import ListView, DetailView
from blog.models import Post


class PostListView(ListView):
    '''класс-контроллер для просмотра списка статей блога, работающий с шаблоном post_list.html'''
    model = Post
    extra_context = {'name_page': 'Список статей блога'}


class PostDetailView(DetailView):
    '''класс-контроллер для просмотра статьи блога, работающий с шаблоном post_detail.html'''
    model = Post
    extra_context = {'name_page': 'Статья блога'}

