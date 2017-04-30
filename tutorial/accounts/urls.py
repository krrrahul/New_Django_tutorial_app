"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.contrib.auth.views import login,logout
urlpatterns = [
    url(r'^$',views.home),
     url(r'^login/$',login,{'template_name':'accounts/login.html'}),# we are using {'template_name':'accounts/login.html'} 
     #this as because though we using django form functionality but we don't use form default page provide by django
     #instead we want to render our own page
     url(r'^logout/$',logout,{'template_name':'accounts/logout.html'}),#same explaination as for login
     url(r'^register/$',views.register,name='register')

]
