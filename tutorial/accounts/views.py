from django.shortcuts import render,HttpResponse

# Create your views here.
#two type of views 1.function based views and 2nd is classes based views

def home(request):
    number={1,2,3,4}
    name='Rahul Kumar'
    args={'myname':name,'numbers':number}
    return render(request,'accounts/home.html',args)