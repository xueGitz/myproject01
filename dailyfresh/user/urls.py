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
    #登录
    url(r'^login$', views.to_login,name='login'),
    #登出
    url(r'^logout$', views.logout_view,name='logout'),
    #忘记密码
    url(r'^rspon_pwd$', views.ForgetPwdView.as_view(),name='rspon_pwd'),
    url(r'^set_new_password/(?P<token>.*)$', views.ResetPwdView.as_view(),name='new_pwd'),
    #注册
    url(r'^register$', views.RegisterView.as_view(),name='register'),
    url(r'^active/(?P<token>.*)$', views.ActiveView.as_view(),name='active'),
    #异步检测用户名是否存在
    url(r'^check_name$', views.check_name,name='check_name'),
    #验证码
    url(r'^verifycode', views.verifycode,name='verifycode'),

    #收货地址
    url(r'^user_center_site$', views.AddressView.as_view(),name='user_center_site'),
    url(r'^user_center_order/(?P<page>\d+)$', views.OrderView.as_view(),name='user_center_order'),
    url(r'^user_center_info$', views.InfoView.as_view(),name='user_center_info'),

    #省市区三级联动
    url(r'^get_province$', views.get_provice,name='get_province'),
    url(r'^get_areas$', views.get_area,name='get_area'),

    #测试form内建表单的使用
    url(r'^register1$',views.register1),
    url(r'^resetpwd$',views.reset)
]
