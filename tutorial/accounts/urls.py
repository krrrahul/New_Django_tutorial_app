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
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import login,logout,password_reset,password_reset_done,password_reset_confirm,password_reset_complete
#now name in  URl is used for removing the hardcoded URLS 
urlpatterns = [
    url(r'^$',views.home), #temporary not using this 
     url(r'^login/$',login,{'template_name':'accounts/login.html'},name='login'),# we are using {'template_name':'accounts/login.html'} 
     #this as because though we using django form functionality but we don't use form default page provide by django
     #instead we want to render our own page
     url(r'^logout/$',logout,{'template_name':'accounts/logout.html'},name='logout'),#same explaination as for login
     url(r'^register/$',views.register,name='register'),
     url(r'^profile/$',views.view_profile,name='view_profile'),
     url(r'^profile/edit/$',views.edit_profile,name='edit_profile'),
     url(r'^change_password/$',views.change_password,name='change_password'),
     #how it works
    # url(r'^reset_password/$',password_reset,name="reset_password"),
    #here password_reset come in default format and we have overwridden that template with our own reset_password template
     #Note: when you give the namespace in main urls file this thing will be broken
     #becoz clicking this call post_reset_redirect which looks to password_reset_done which is used as reverse and 
     # it will try to find accounts:password_reset_done and we can change it by adding post_reset_redirect':'accounts:password_reset_done'
     
     url(r'^reset_password/$',password_reset,{'template_name':'accounts/reset_password.html',
                                              'post_reset_redirect':'accounts:password_reset_done',
                                              'email_template_name':'accounts/reset_password_email.html'},name="reset_password"),

     url(r'^reset_password/done/$',password_reset_done,{'template_name':'accounts/reset_password_done.html'},name="password_reset_done"),
     #note that reset_password will internally call password_reset_done by 
     #seeing the name in password_reset_done url and name should "password_reset_done" only
     
     url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',password_reset_confirm,{'template_name':'accounts/reset_password_confirm.html',
                                                                                                     'post_reset_redirect':'accounts:password_reset_complete'},name="password_reset_confirm"),#in this also name is importnat
     #in above url note that keyword argument will try to send to URL a token and uidb64 
     #reset_password try send data to confirm URL 
     #Note after one more error will come in which it send mail through an emial server and we can python
     #inbuild email debbuging server .you can get the details from http://stackoverflow.com/questions/5802189/django-errno-111-connection-refused/5802348#5802348
     url(r'^reset_password/complete/$',password_reset_complete,{'template_name':'accounts/reset_password_complete.html'},name="password_reset_complete"),
     
    
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
