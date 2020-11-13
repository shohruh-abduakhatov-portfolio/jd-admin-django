from django.urls import path, include

from cms_panel import views


urlpatterns = [
    path('index', views.index, name='cms_index'),
    path('', views.to_admin, name='to_admin'),
    # path('cms/', include('cms_panel.cms_panel.cms_panel.urls')),
]
