"""railwayadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.user, name='user')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='user')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include


urlpatterns = [
    path('', include('login.urls')),
    path('user/', include('user.urls')),
    path('station/', include('station.urls')),
    path('train/', include('train.urls')),
    path('admin/', include('admin_panel.urls')),
    path('content/', include('content.urls')),
    path('label/', include('label.urls')),
    path('tariff/', include('tariff.urls')),
    path('country/', include('country.urls')),
    path('doc/', include('doc.urls')),
    path('cms/', include('cms_panel.urls')),
]
