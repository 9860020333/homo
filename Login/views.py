from django.shortcuts import render, redirect
from .forms import Login_Form
from django.contrib.auth import authenticate as auth
from django.contrib.auth import login as lgn
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def Login_View(request):
    try:
        key = request.session['member-id']
        return redirect('/home/')
    except:
        if request.method == "POST":
            form = Login_Form(request.POST)
            username = request.POST['username']
            password = request.POST['password']
            user = auth(username=username, password=password)
            if user is not None:
                lgn(request, user)
                request.session['member-id'] = user.id
                messages.success(request, "Logged In successfully!")
                return redirect('/home/')
            else:
                return render(request, "Home/home.html", {'form': form, 'error': 'True'})


def Logout_View(request):
    del request.session['member-id']
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/home/')


@login_required
def Profile_View(request):
    return render(request, "Login/Profile.html", {})


def signup_view(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('/home/')
    else:
        f = UserCreationForm()
    return render(request, 'Signup/signup.html', {'form': f})
