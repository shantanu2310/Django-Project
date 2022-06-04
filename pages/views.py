import os
from django.shortcuts import render , redirect
# from .models import
from cars.models import Car
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from .forms import EmailForm

def home(request):
    # teams = Team.objects.all()

    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    # search_fields = Car.objects.values('model', 'city', 'year', 'body_style')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    data = {
            # 'teams':teams,
            'featured_cars':featured_cars,
            'all_cars': all_cars,
            # 'search_fields': search_fields,
            'model_search': model_search,
            'city_search': city_search,
            'year_search': year_search,
            'body_style_search': body_style_search,

     }

    return render(request,'pages/home.html', data)
# Create your views here.

def about(request):
    # teams = Team.objects.all()
    # data = {
    #        'teams':teams,
    # }
    return render(request,'pages/about.html')
def add(request):
    # teams = Team.objects.all()
    # data = {
    #        'teams':teams,
    # }
    return render(request,'pages/add.html')

def services(request):
    return render(request,'pages/services.html')

def offers(request):
    return render(request,'pages/offers.html')

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = 'You have a new message from Cartrade website regarding' + subject
        message_body = 'Name: ' + name + '. Email: ' + email + '. Phone: ' + phone + '. Message: ' + message

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
                email_subject,
                message_body,
                'sainath23. django@gmail.com',
                [admin_email],
                fail_silently=False,
            )

        messages.success(request, 'Thank U for contacting us.We will get back to you shortly')
        return redirect('contact')
    return render(request,'pages/contact.html')

def add(request):
    if request.method=='POST':
        name = request.POST['first_name']
        car_title = request.POST['car_title']
        car_model = request.POST['car_model']
        year = request.POST['year']
        condition = request.POST['condition']
        transmission = request.POST['transmission']
        ownedcount = request.POST['ownedcount']
        age = request.POST['age']
        insurancedone = request.POST['insurancedone']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']



        email_subject = 'You have a new message from Cartrade website regarding'
        message_body = 'Name:- ' + name + '. Email:- ' + email + '. Phone:- ' + phone + '. Message:- ' + message + '. Car Title- ' + car_title + '. Car Model:-' + car_model+'. Year:-' + year + '. Condition:- ' + condition + '. Transmission:- ' + transmission +'. Owner Count:-' + ownedcount + '. Age of the car:-' + age
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        # send_mail(
        #         email_subject,
        #         message_body,
        #         'sainath23.django@gmail.com',
        #         [admin_email],
        #         fail_silently=False,
        #     )

        email=EmailMessage(email_subject,message_body,'sainath23.django@gmail.com',[admin_email])


        pic1 = request.FILES['pic1']
        email.attach(pic1.name, pic1.read(), pic1.content_type)
        email.send()
        messages.success(request, 'Your car data has been sent successfully')
        return redirect('contact')
    return render(request,'pages/add.html')
