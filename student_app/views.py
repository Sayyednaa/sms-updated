from django.shortcuts import render,redirect
from todo.models import Task
from django.contrib import messages
from django.contrib.auth.models import User
from pyislam import Quran
from django.contrib.auth import authenticate, login,logout
from .import pygq
import os
from todo.models import Task,syallbuss

import random
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


from django.views.decorators.csrf import csrf_protect,csrf_exempt



Q = pygq.PyGQ()


@login_required
def home(request):
    if request.user.is_authenticated:
        x = datetime.date.today()
        date=x.strftime('%m/%d/%Y')
       
        
        task=Task.objects.filter(description=datetime.date.today(),user=request.user)



        TaskData=Task.objects.filter(user=request.user).all()
        completedTask=Task.objects.filter(completed=True,user=request.user).count()
        Tc=syallbuss.objects.filter(user=request.user).all().count()
        CompletedC=syallbuss.objects.filter(completed=True,user=request.user).count()
        Rc=Tc-CompletedC
        ct=completedTask
        pt=TaskData.count()-completedTask




        return render(request, 'main/home.html',{'totalTask':TaskData.count(),
                                                'completedTask':ct,
                                                'pendingTask':pt,
                                                
                                                'task':task,
                                                'Tc':Tc,
                                                'CompletedC':CompletedC,
                                                'Rc':Rc,
                                             

                                                })
    return redirect("/login")

@csrf_exempt
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')

        else:
            # Return an 'invalid login' error message.
            messages.error(request, 'Invalid Email or Password')
    return render(request,'main/login.html')

@login_required
def logoutUser(request):
   logout(request)
   return redirect('/login')


def forgetPass(request):
    pass
def createac(request):
    if request.user.is_authenticated:

        return redirect('/')
    if request.method=='POST':
            print("hurray")
            password=request.POST['password']
            username=request.POST['username']
            email=request.POST['email']
            fist_name=request.POST['first_name']
            last_name=request.POST['last_name']
            user = User.objects.create_user(username, email, password,first_name=fist_name,last_name=last_name,)
            user.save()
            messages.success(request, 'Account Created Successfully')

    return render(request,'main/signup.html')



@login_required
def user_profile(request):
    user = request.user  # The logged-in user's details
    recent_activities = [
        {"description": "Logged in", "date": "2025-01-28"},
        {"description": "Updated profile", "date": "2025-01-25"}
    ]  # Example activities; you can fetch these from a database
    return render(request, 'user/profile.html', {'user': user, 'recent_activities': recent_activities})