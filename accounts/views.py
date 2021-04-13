from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.

def Register(request):
    return redirect('/adminRegistration')



def Login(request):

    if request.method == 'POST':
        context = dict()

        username = request.POST['username']
        password = request.POST['password']

        context['userName'] = username

        # print(context)

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/adminDashBoard', context)
        else:
            return redirect ('/adminLogin')
    
    return redirect('/adminLogin')


def Logout(request):
    auth.logout(request)
    return redirect('/index')
