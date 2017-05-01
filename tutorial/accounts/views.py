from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .form import RegistrationForm,EditProfileForm
from django.contrib.auth.forms import UserChangeForm
# Create your views here.
# two type of views 1.function based views and 2nd is classes based views

def home(request):
    number = {1, 2, 3, 4}
    name = 'Rahul Kumar'
    args = {'myname':name, 'numbers':number}
    return render(request, 'accounts/home.html', args)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print("save")
        if form.is_valid():
            print("not save")
            form.save()
            return redirect('/account')
        
    else:
        form = RegistrationForm()
        args = {'form':form}
        return render(request, 'accounts/reg_form.html', args)
    
def view_profile(request):
    args = {'user':request.user}  # this user(which is a object) came from User which we have imported
    return render(request, 'accounts/profile.html', args)
#by usercreation form gives many thing to change which is not necessary for us.If you want to see just replace EditProfileForm by UserChangeForm
# and see the change
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user) #UserChangeForm is provided by default Django
        if form.is_valid():
            form.save()
            return redirect('/account/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form':form}
        return render(request, 'accounts/edit_profile.html', args)

