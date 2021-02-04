from django.shortcuts import render,redirect
from .models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def register(request):
    if request.method=='POST':
        if request.POST['password']==request.POST['confirmPassword']:
            try:
                user=Users.objects.get(username=request.POST['username'])
                return render(request,'register.html',{'message':'Username Name has already been taken'})
            except Users.DoesNotExist:
                user=Users.objects.create(username=request.POST['username'],password=request.POST['password'])
                return render(request, 'register.html', {'alert': 'User Created Successfully!!!!'})
        else:
            return render(request, 'register.html', {'message': 'Passwords must match'})
    return render(request,'register.html')


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            user_data=Users.objects.get(username=username,password=password)
            return redirect('userbase')
        except ObjectDoesNotExist:
            return render(request, 'login.html',{'error':'Username or Password is incorrect.'})
    else:
        return render(request,'login.html')

def userbase(request):
    return render(request,'userbase.html')
