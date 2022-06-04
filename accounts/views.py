from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from tkinter import Entry
# Create your views here.
def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['Password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                    auth.login(request,user)
                    messages.success(request, 'You are now logged in.')
                    return redirect('home')
                    user.save()
                    messages.success(request, 'You are registered successfully.')
                    return redirect('login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')

@login_required(login_url='login')
def dashboard(request):
    user_inquiry= Contact.objects.order_by('-create_date').filter(user_id=request.user.id)
    data = {
        'inquiries':user_inquiry,
    }
    return render(request, 'accounts/dashboard.html',data)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)

        return redirect('home')
    return redirect('home')
# def forgot(request):
#
#
#     return render(request,'accounts/forgot.html')

def fetch(request):
    if request.method=='POST':
        un=request.POST['un']
        email1=request.POST.get('em')
        username1=User.objects.all().filter(username=un)
        data = list(username1.values())
        password=User.objects.filter(password)&User.objects.filter(username1)

    email_subject = 'You have requested a password'
    message_body = 'UserName:-'+email1

    email=EmailMessage(email_subject,message_body,'sainath23.django@gmail.com',[email1])
    email.send()
    return redirect('login')
