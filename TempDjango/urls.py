"""TempDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from django.views.generic import RedirectView
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/all/', views.list_all_reg, name='list_all_reg'),
    path('login/', views.login_user, name='login_user'),
    path('login/submit', views.submit_login, name='submit_login'),
    path('logout/', views.logout_user, name='logout_user'),
    path('registro/', views.registros),
    path('', RedirectView.as_view(url='reg/all/')),

    #path('login/', views.login_user),

    #path('', views.home, name='home'),

    #path('base.html', views.baseht, name='baseht'),
    #

    #url(r'admin/', admin.site.urls),
    #url(r'', TemplateView.as_view(template_name='index.html')),
]
