from django.urls import path, include
from admin_panel import views

urlpatterns = [
    path('login', views.login, name='admin_login'),
    path('profile', views.profile, name='admin_profile_json'),
    path('create', views.create, name='admin_create'),
]
