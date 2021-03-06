from django.shortcuts import render, redirect
from django.contrib import messages
from Tours.settings import EMAIL_HOST_USER
from .forms import EmailForm
from django.core.mail import send_mail
# Create your views here.

def contact(request):
    sub = EmailForm()
    if request.method == 'POST':
        sub = EmailForm(request.POST)
        subject = str(sub['subject'].value())
        message = str(sub['body'].value())
        recepient = str(sub['email'].value())
        name = str(sub['name'].value())
        message = "Name:"+name+'\n'+"SENDER:"+recepient+'\n'+"MESSAGE:"+message
        send_mail(subject,
                  message, EMAIL_HOST_USER, ['webcodersdjango@gmail.com'], fail_silently=False)
        messages.success(request, f'Thank you for the response. You will be contacted soon!!')
        return redirect('home')
    return render(request, 'base.html', {'form': sub})
