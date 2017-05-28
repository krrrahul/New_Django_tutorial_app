from django.contrib import admin
from .models import UserProfile
from django.db import models


#not much important
class UserProfileManager(models.Manager):#basically used to customize the existing things
    #eg play around with users thing
    def get_queryset(self):
        return super(UserProfileManager.self).get_queryset().filter(city='London')

class UserProfileAdmin(admin.ModelAdmin): # we are changing the table user profile
    #list_display=('user','description')# when you open admin page and click on 
    # userprofile ,inside the list display you will add coloumn whatever you want to show
    # and you can chnage column name too like we have given down user_info down here .
    list_display=('user','user_info','city','website','phone')
    # now user_info is not present in our model so will assign to some column from model
    # by below method
    london=UserProfileManager()
    def user_info(self,obj):
        return obj.description
    #user_info will be shown on the admin page.user_info will be also a method .and you want give some different name
    #which will be shown in admin page do by below thing  
    user_info.short_description='INFOrmation' #try this .this to short if there is long data in attribute
    # this 
    def get_queryset(self, request):#this is inbuilt method and overriding it 
        queryset=super(UserProfileAdmin,self).get_queryset(request)#use the default method queryset and customize that method
        queryset=queryset.order_by("phone")
        return queryset
    
    
# Register your models here.
admin.site.register(UserProfile,UserProfileAdmin)

#admin.site.site_header='Administrator' # its is for changing the admin pAGE but by one element only

# there are two way to alter the admin page .one by above method or other by overriding the admin page
# by  extending the existing admin html page                                                                