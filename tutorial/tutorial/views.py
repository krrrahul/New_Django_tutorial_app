'''
Created on Apr 30, 2017

@author: rahul
'''
from django.shortcuts import redirect
'''This is made so that if user should redirect if he type '/' simply in the url'''
def login_redirect(request):
    return redirect('/account/login')