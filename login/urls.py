from django.urls import path, include
from login import views


urlpatterns = [
    path('', views.auth, name='auth'),
    path('logout', views.logout, name='logout'),

    # path('create', views.create, name='user_create'),
    # path('view', views.view, name='user_view'),
    # path('list', views.table_list, name='users_list_json'),
    # path('activate', views.activate, name='users_activate_json'),
]
