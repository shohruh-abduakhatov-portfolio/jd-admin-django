from django.urls import path
from train import views

urlpatterns = [
    path('', views.index, name='train_index'),
    path('create', views.create, name='train_create'),
    path('view', views.view, name='train_view'),
    path('list', views.table_list, name='trains_list_json'),
    path('activate', views.activate, name='trains_activate_json'),
]