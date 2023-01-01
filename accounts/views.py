from django.shortcuts import redirect, render
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from contacts.models import Contact
# Create your views here.
def login(request):
        if request.method == 'POST':   
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request,'You are logged in')
                return redirect('dashboard')
            else:
                messages.error(request,'Invalid Credationals')
                return redirect('login')
        return render(request,'accounts/login.html')

               
def register(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username Already Register')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email Already Register')
                return redirect('register')
                    
            else:
                user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,password=password,email=email)
                user.save()  
                messages.success(request,'You are registered successfully')
                return redirect('login')
        else:
           messages.error(request,'Password doest match')
           return redirect('register')
    return render(request,'accounts/register.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        messages.success(request,'You are succesfully logged out')
    return redirect('home')

@login_required(login_url='login')
def dashboard(request):
    user_inquiry=Contact.objects.order_by('-create_date').filter(user_id=request.user.id) 
    data={
        'inquires':user_inquiry
    }   
    return render(request,'accounts/dashboard.html',data)
