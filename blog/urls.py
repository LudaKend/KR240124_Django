from django.urls import path
from blog.apps import BlogConfig
from blog.views import PostListView, PostDetailView

app_name = BlogConfig.name

urlpatterns = [
    path('list_view/', PostListView.as_view(), name='route_post_list'),
    path('view/<int:pk>/', PostDetailView.as_view(), name='route_post_view'),
]
