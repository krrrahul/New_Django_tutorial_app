from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save #save obejct and when fisnished run the code sfter post
#they allow you to execute code some code based on certain thing happening with database usually when you save object or
#do something with models

# Create your models here.
class UserProfile(models.Model):
     #inhererit from models 
    user=models.OneToOneField(User)
    description=models.CharField(max_length=100,default='')
    city=models.CharField(max_length=10,default='')
    website=models.URLField(default='')
    phone=models.IntegerField(default=0)
    image =models.ImageField(upload_to='profile_image',blank=True) # generally we don't store
    #image in databse becuase it slow the system down as they are very large and it will upload to 
    # profile_image folder in the project if it is not present it will create it

    def __str__(self):
        #if we will not wtite this it will simple give 
        #userobject as username everywhere
        return self.user.username
    
    
def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile=UserProfile.objects.create(user=kwargs['instance'])
        
post_save.connect(create_profile,sender=User) 
"""on any change in data of User provided by django
it will create an new user in UserProfile(by sending signal class automatically"""
    
    