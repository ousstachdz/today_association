from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as login_user


def index(request):
    return render(request=request, template_name='index.html')

def login(request):
    if(request.POST):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,username=email, password=password)
        if (user):
            login_user(request, user)
            return redirect('index')
        else:
            data={'msg':'email or password are inccorect'}
            return render(request=request, template_name='login.html',context=data)
    else:
        return render(request=request, template_name='login.html')
    
def register(request):
    return render(request=request, template_name='register.html')
    
def contact(request):
    return render(request=request, template_name='contact.html')
    
def about(request):
    return render(request=request, template_name='about.html')
    