from django.contrib.auth.views import LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import RegisterView, UserLoginView, UserListView, UserDetailView, UserUpdateView, UserDeleteView
from users.views import index_deactivate, index_verify

app_name = UsersConfig.name

urlpatterns = [
    path('login/', UserLoginView.as_view(template_name='users/login.html'), name='route_login_users'),
    path('logout/', LogoutView.as_view(), name='route_logout_users'),
    path('register/', RegisterView.as_view(template_name='users/register.html'), name='route_register_users'),
    path('list_view/', UserListView.as_view(), name='route_users_list'),
    path('view/<int:pk>/', UserDetailView.as_view(), name='route_users_view'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='route_users_update'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='route_users_delete'),
    path('deactivate/<int:pk>/', index_deactivate, name='route_deactivate'),
    path('verify/', index_verify, name='route_verify'),
]
