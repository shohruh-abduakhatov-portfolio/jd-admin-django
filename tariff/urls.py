from django.urls import path
from tariff import views

urlpatterns = [
    path('', views.index, name='tariff_index'),
    path('create', views.create, name='tariff_create'),
    path('view', views.view, name='tariff_view'),
    path('list', views.table_list, name='tariffs_list_json'),
    path('activate', views.activate, name='tariffs_activate_json'),
]
