import os
from pathlib import Path
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as login_user, logout as logout_user
from apps.models import Poster, TodayUser


def index(request):
    print()
    if request.user.is_authenticated:
        return redirect('profil')
    return render(request=request, template_name='index.html')

def contact(request):
    if request.user.is_authenticated:
        return redirect('profil')
    return render(request=request, template_name='contact.html')
    
def about(request):
    if request.user.is_authenticated:
        return redirect('profil')
    return render(request=request, template_name='about.html')    

def dashbord(request):
    if request.user.is_authenticated:
        return redirect('profil')
    return render(request=request, template_name='dashbord.html')
    
def profil(request):
    if request.user.is_authenticated:
        return render(request=request, template_name='profil.html')
    return redirect('login')
    
def login(request):
    if(request.POST):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,username=email, password=password)
        print(email,password)
        if (user):
            print(user)
            login_user(request, user)
            if(user.is_admin):
                return redirect('dashbord')
            return redirect('profil')
        else:
            data={'msg':'email or password are inccorect'}
            return render(request=request, template_name='login.html',context=data)
    else:
        return render(request=request, template_name='login.html')
    

def register(request):
    if request.POST:
        email = request.POST['email']
        if len(email)<=8:
            print("invalid email")
        else:
            try:
                user = TodayUser.objects.get(email=email)
            except TodayUser.DoesNotExist:
                try:
                    user = TodayUser.objects.get(username=email[0:8])
                except TodayUser.DoesNotExist:
                    user = None
            if user is not None :
                print('email alrelly used')
            else:
                password = request.POST['password']
                cpassword = request.POST['cpassword']
                if len(password)<=8:
                    print('short password')
                else:
                    if password!=cpassword:
                        print("password and Cpassword didn't match")
                    else:
                        first_name = request.POST['first_name']
                        last_name = request.POST['last_name']
                        new_user = TodayUser.objects.create(
                            first_name=first_name,last_name=last_name,email=email,
                            is_admin=False,is_active_number=False,is_number=False,
                            username=email[0:8],password=password)
                        new_user.save()
                        login_user(request,new_user)
                        return redirect('second_page_register')
    return render(request=request, template_name='register.html')

def second_page_register(request):
    if request.POST:
        user = TodayUser.objects.get(pk=request.user.id)
        if(user):
            user.date_birth = request.POST['birthday'] 
            user.address = request.POST['address'] 
            user.save()
            return redirect('complet_page_register')
    return  render(request, 'second_page_register.html')

def complet_page_register(request):
    if request.POST:
        user = TodayUser.objects.get(pk=request.user.id)
        if(user):
            print(request.FILES['file'])
            user.img = request.FILES['file']

            user.save()
            return redirect('profil')
    return  render(request, 'complet_page_register.html')


def logout(request):
    logout_user(request)
    return redirect('login')
        
        
def postes(request):
    if request.user.is_authenticated:
        postes = Poster.objects.all()
        data = {'postes':postes}
        return render(request=request, template_name='postes.html',context = data)
    return redirect('index')
    