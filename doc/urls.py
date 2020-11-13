from django.urls import path
from doc import views

urlpatterns = [
    path('', views.index, name='doc_index'),
    path('create', views.create, name='doc_create'),
    path('view', views.view, name='doc_view'),
    path('list', views.table_list, name='docs_list_json'),
    path('activate', views.activate, name='docs_activate_json'),
]
