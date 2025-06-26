from django.shortcuts import render,redirect
from django.core.mail import send_mail 
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def home(request):
    return render(request, 'main/index.html')

def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        full_message = f"""
        You have a new message from your portfolio contact form:

        Name: {name}
        Email: {email}
        Subject: {subject}

        Message:
        {message}
        """
        send_mail( 
            subject,
            full_message,
            settings.DEFAULT_FROM_EMAIL,
            ['jyothishunni653@gmail.com']  
        )
        return render(request, 'main/email_success.html')  

    return redirect('index')  











