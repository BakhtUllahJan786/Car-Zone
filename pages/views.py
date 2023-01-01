from django.contrib import messages
from django.core.mail import send_mail
from  django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .models import Team
from cars.models import Car
# Create your views here.
def home(request):
    teams=Team.objects.all()
    featured_cars=Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars=Car.objects.order_by('-created_date')
    model_search=Car.objects.values_list('model',flat=True).distinct()
    year_search=Car.objects.values_list('year',flat=True).distinct()
    city_search=Car.objects.values_list('city',flat=True).distinct()
    body_style_search=Car.objects.values_list('body_style',flat=True).distinct()

    context={
        'teams':teams,
        'featured_cars':featured_cars,
        'all_cars':all_cars,
        'body_style_search': body_style_search,
        'model_search': model_search,
        'year_search': year_search,
        'city_search': city_search,

    }
    return render(request,'pages/home.html',context)

def about(request):
    teams=Team.objects.all()
    context={
        'teams':teams
    }
    return render(request,'pages/about.html',context)

def services(request):
    return render(request,'pages/services.html')

def contact(request):
    if request.method == 'POST':   
        name=request.POST.get('name','')
        subject=request.POST.get('subject','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        message=request.POST.get('message','')
        
        email_subject='Message from carzone'+subject
        message_body='Name :'+name+ '. Email :'+email+ '. Phone :'+phone+  '. Messsage :' + message
        admin_info=User.objects.get(is_superuser=True)
        admin_email=admin_info.email
        send_mail(
            email_subject,
            message_body,
            'bakhtullahjan81@gmail.com',
            [admin_email],
            fail_silently=False,
        )
        
        
        
        messages.success(request,'Thank  You foe contacting us')
        return redirect('contact')
    return render(request,'pages/contact.html')