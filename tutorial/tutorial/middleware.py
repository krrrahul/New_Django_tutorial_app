# from django.contrib.auth.decorators import login_required
from django.conf import settings
import re
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.urls import reverse  # this is used for removing the hardcoded Urls

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]
    
class LoginRequiredMiddleware:
    '''we are using to remove the burden of putting
    decorator like @login_required on each view or class in the 
    views file'''
    def __init__(self, get_response):  # whenever we create a middleware the init is passed with some parameter
        self.get_response = get_response  # print (get_response)
       
    def __call__(self, request):
        response = self.get_response(request)
        return response
        
    def process_view(self, request, view_func, view_args, view_kwargs):  # it is inbuilt django function # just before going from URL to views it call a intermediate middleware i.e.
        # process_views and name of the function in views for which you are going will be passed as parameter in view_func
        assert hasattr(request, 'user')  # request object as the attribute should have user means request.user should exist #validation
        path = request.path_info.lstrip('/')  # path contain string of url of which user is trying to request
        # print ("i am printinh the pass",path)
       # if not request.user.is_authenticated():
       #     if not any(url.match(path) for url in EXEMPT_URLS):
       #         #print(settings.LOGIN_URL)
       #         return redirect(settings.LOGIN_URL)
        url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)
        print("This is reverse %s" % reverse('accounts:logout'))
        if path == reverse('accounts:logout').lstrip('/'):#here accounts: came from namespace in url main files 
        #if path == reverse('logout').lstrip('/'):  # reverse is used here for remoing the hardcoded URL
            # reverse inside bracket of it name of url us written where you want to redirect
            # but the thing is reverse send url with forward slash(/)appended to it and 
            # path only compare URL with forward slash appended to it.
            logout(request)
            
            
        if request.user.is_authenticated() and url_is_exempt:
            return redirect(settings.LOGIN_REDIRECT_URL)
        elif request.user.is_authenticated() or url_is_exempt:
            return None
        else:
            return redirect(settings.LOGIN_URL)
            
        
            
                      
        
        
        
    
        
