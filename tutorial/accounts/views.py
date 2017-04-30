from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from .form import RegistrationForm
# Create your views here.
#two type of views 1.function based views and 2nd is classes based views

def home(request):
    number={1,2,3,4}
    name='Rahul Kumar'
    args={'myname':name,'numbers':number}
    return render(request,'accounts/home.html',args)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print("save")
        if form.is_valid():
            print("not save")
            form.save()
            return redirect('/account')
        
    else:
        form=RegistrationForm()
        args={'form':form}
        return render(request,'accounts/reg_form.html',args)