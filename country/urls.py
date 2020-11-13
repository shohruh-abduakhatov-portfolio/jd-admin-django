from django.urls import path
from country import views

urlpatterns = [
    path('', views.index, name='country_index'),
    path('create', views.create, name='country_create'),
    path('view', views.view, name='country_view'),
    path('list', views.table_list, name='countrys_list_json'),
    path('activate', views.activate, name='countrys_activate_json'),
]
