# from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path
from blog import views

"""pytest URL Configuration

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

urlpatterns = [
    path('', views.home_page, name='home'),
    path('test/<test_res>', views.test_arg, name='test'),
    path('template/', views.home_template, name='template'),
    path('template/id/<post_id>/', views.post_detail, name='post_detail'),
    path('template/create/', views.post_create, name='post_create'),
    path('template/<post_id>/update/', views.update, name='post_update'),
    path('template2/add/', views.add_post, name='add_post'),
    path('admin/', admin.site.urls, name='admin'),
    
]
