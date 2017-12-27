"""course URL Configuration

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
from django.urls import path
from django.conf.urls import include, url
from django.views.static import serve
from django.views.generic import TemplateView

from course.settings import MEDIA_ROOT

from users.views import LogoutView, LoginView, RegisterView, AciveUserView, ForgetPwdView, ResetView, ModifyPwdView
from users.views import IndexView

from organization.views import *

import xadmin

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    # url(r'^$', TemplateView.as_view(template_name="test.html"), name="index"),
    url('^$', IndexView.as_view(), name="index"),
    url('^login/$', LoginView.as_view(), name="login"),
    url('^logout/$', LogoutView.as_view(), name="logout"),
    url('^register/$', RegisterView.as_view(), name="register"),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', AciveUserView.as_view(), name="user_active"),
    url(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name="reset_pwd"),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name="modify_pwd"),

    #课程机构url配置
    url(r'^org/', include('organization.urls', namespace="org")),

    #课程相关url配置
    url(r'^course/', include('subjects.urls', namespace="courses")),

    #配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$',  serve, {"document_root":MEDIA_ROOT}),

    # url(r'^static/(?P<path>.*)$',  serve, {"document_root":STATIC_ROOT}),

    #课程相关url配置
    url(r'^users/', include('users.urls', namespace="users")),


]

#全局404页面配置
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'
