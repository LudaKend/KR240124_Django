from django.urls import path
from client.apps import ClientConfig
from client.views import ClientCreateView, ClientListView, ClientDetailView, ClientUpdateView, ClientDeleteView

app_name = ClientConfig.name

urlpatterns = [
    path('create/', ClientCreateView.as_view(), name='route_client_create'),
    path('list_view/', ClientListView.as_view(), name='route_client_list'),
    path('view/<int:pk>/', ClientDetailView.as_view(), name='route_client_view'),
    path('update/<int:pk>/', ClientUpdateView.as_view(), name='route_client_update'),
    path('delete/<int:pk>/', ClientDeleteView.as_view(), name='route_client_delete'),
]
