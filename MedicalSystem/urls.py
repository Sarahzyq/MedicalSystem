"""MedicalSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url

#from django.contrib import auth
from django.contrib.auth import views

import zscg.urls
from django.contrib import admin
from zscg.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
   # url(r'^login/', include('zscg.urls')), 
    url(r'^', include(zscg.urls)), 
    #url(r'^', include(zscg.urls,namespace='zscg')), 
#    url(r'^logout/', views.logout), 
#    url(r'^login/$', auth_views.LoginView.as_view(
#        template_name='users/login.html'),
#        name='users_login'),
#    url(r'^logout/$', auth_views.LogoutView.as_view(
#        template_name='users/logout.html'),
#        name='users_logout'),

]
    
