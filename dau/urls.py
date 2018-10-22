"""dau URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from suporte import views as suporte_views

urlpatterns = [
    path('', suporte_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('suporte/', include('suporte.urls')),
]


admin.site.site_header = 'Suporte DAU'
admin.site.index_title = 'Administração'
admin.site.site_title = 'Seja bem-vindo ao Suporte Técnico 2.0'