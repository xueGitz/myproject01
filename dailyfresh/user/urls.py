"""dailyfresh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin


from user import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    #登录
    url(r'^login$', views.to_login,name='login'),
    #注册
    url(r'^register$', views.RegisterView.as_view(),name='register'),
    url(r'^active/(?P<token>.*)$', views.ActiveView.as_view(),name='active'),
    #异步检测用户名是否存在
    url(r'^check_name$', views.check_name,name='check_name'),

    #验证码
    url(r'^verifycode', views.verifycode,name='verifycode'),
]
