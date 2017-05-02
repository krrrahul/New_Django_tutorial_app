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
from django.contrib.auth.views import login,logout,password_reset,password_reset_done,password_reset_confirm,password_reset_complete
urlpatterns = [
    url(r'^$',views.home),
     url(r'^login/$',login,{'template_name':'accounts/login.html'}),# we are using {'template_name':'accounts/login.html'} 
     #this as because though we using django form functionality but we don't use form default page provide by django
     #instead we want to render our own page
     url(r'^logout/$',logout,{'template_name':'accounts/logout.html'}),#same explaination as for login
     url(r'^register/$',views.register,name='register'),
     url(r'^profile/$',views.view_profile,name='view_profile'),
     url(r'^profile/edit/$',views.edit_profile,name='edit_profile'),
     url(r'^change_password/$',views.change_password,name='change_password'),
     #how it works
     url(r'^reset_password/$',password_reset,name="reset_password"),
     url(r'^reset_password/done/$',password_reset_done,name="password_reset_done"), #note that reset_password will
     #internally call password_reset_done by seeing the name in password_reset_done url and name should "password_reset_done" only
     url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',password_reset_confirm,name="password_reset_confirm"),#in this also name is importnat
     #in above url note that keyword argument will try to send to URL a token and uidb64 
     #reset_password try send data to confirm URL 
     #Note after one more error will come in which it send mail through an emial server and we can python
     #inbuild email debbuging server .you can get the details from http://stackoverflow.com/questions/5802189/django-errno-111-connection-refused/5802348#5802348
     url(r'^reset_password/complete/$',password_reset_complete,name="password_reset_complete"),
     
    
     
]
