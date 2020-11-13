from django.urls import path
from station import views

urlpatterns = [
    path('', views.index, name='station_index'),
    path('create', views.create, name='station_create'),
    path('view', views.view, name='station_view'),
    path('admin/list1', views.table_list, name='stations_list_json'),
    path('activate', views.activate, name='stations_activate_json'),
]
