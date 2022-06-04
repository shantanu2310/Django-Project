from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST.get('email')
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry about this car. Please wait untill we get back to you.')
                return redirect('/cars/'+car_id)


        contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id,
        first_name=first_name, last_name=last_name, customer_need=customer_need,
        city=city, state=state, email=email, phone=phone, message=message)

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
                'New Car Inquiry',
                email +' You have the new inquiry for the car' + car_title + '. Please login to your admin panel for more info.' + phone +'',
                email,
                [admin_email],
                fail_silently=False,
            )


        # admin_info = User.objects.filter(is_superuser=True)
        # admin_emails = for i in admin_info:
        #
        # admin_emails.append(i.email)
        # send_mail(
        #         'New Car Inquiry',
        #         'You have the new inquiry for the car' + car_title + '. Please login to your admin panel for more info.',
        #         'sainath23.django@gmail.com',
        #          admin_emails,
        #          fail_silently=False,
        #     )

        contact.save()
        messages.success(request, 'Your request has been submitted, we will get back to you shortly.')
        return redirect('/cars/'+car_id)
def isauth(request):
    if(user.is_authenticated):
        print("Logged in")
        return redirect('/cars/')
    else:
        print("Not logged in")
        message.error(request,'Please login first')
        return redirect('/car_detail/')
