from django.urls import path
from content import views, viewss

# from label import views

urlpatterns = [
    path('', views.index, name='content_index'),
    path('create', views.create, name='content_create'),
    path('view', views.view, name='content_view'),
    path('list', views.table_list, name='contents_list_json'),
    path('activate', views.activate, name='contents_activate_json'),
    path('label', viewss.index, name='label_index'),
    path('label/create', viewss.create, name='label_create'),
    path('label/view', viewss.view, name='label_view'),
    path('label/list', viewss.table_list, name='labelss_list_json'),
    path('label/activate', viewss.activate, name='labelss_activate_json'),
]
