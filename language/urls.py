from django.urls import path
from language import views

urlpatterns = [
    path('', views.index, name='language_index'),
    path('create', views.create, name='language_create'),
    path('view', views.view, name='language_view'),
    path('list', views.table_list, name='languages_list_json'),
    path('activate', views.activate, name='languages_activate_json'),
]
