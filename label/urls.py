from django.urls import path
from label import views

urlpatterns = [
    path('', views.index, name='label_index'),
    path('create', views.create, name='label_create'),
    path('view', views.view, name='label_view'),
    path('list', views.table_list, name='labels_list_json'),
    path('activate', views.activate, name='labels_activate_json'),
]
