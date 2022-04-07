from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.shortcuts import render,HttpResponse,redirect
from . import forms
from django.contrib import messages
from .models import Library
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

# Create your views here.
# SIGNUP
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signup(request):
    context={
        "form":forms.RegistrationForm,
    }
    return render(request,'signup.html',context)

# USER SIGN UP
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def addUser(request):
    username=request.POST['username']
#    phone=request.POST['phone']
    email=request.POST['email']
    password=request.POST['password']
    repassword=request.POST['rep']
    
    # Checking if both passwords are true
    if password!=repassword:
        messages.add_message(request,messages.ERROR,"Passwords doesn't match")
        return redirect(signup)

    # Checking if email already exists in database
    elif User.objects.filter(email=email).exists():
        messages.add_message(request,messages.WARNING,"Your records already exists. Please try resetting your password")
        return redirect('signup')
    # Checking if Username exists in database
    elif User.objects.filter(username=username).exists():
        messages.add_message(request,messages.WARNING,"Your records already exists. Please try resetting your password")
        return redirect('signup')
    # Else we can save the user
    else:
        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        return redirect('logon')
    return render(request,'signup.html')
    
# LOGIN PANEL
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logon(request):
    context={
        "form":forms.RegistrationForm
    }
    return render(request,'login.html',context)

# AUTHENTICATE USER
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def loggedin(request):
    username=request.POST['username']
    password=request.POST['password']
    user=authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        return redirect('index')
    else:
        messages.add_message(request,messages.ERROR,"Wrong USER ID/Password or Account does not exist")
        return redirect('logon')

# LOGOUT USER
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def log_out(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('logon')

#LMS INDEX
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='logon')
def index(request):
    book = Library.objects.all()

    context={
        'books':book,
    }
    return render(request,'index.html',context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def add(request):
    if request.method == "POST":
        bname=request.POST.get('bname')
        bauthor=request.POST.get('bauthor')
        book=Library(
            bname=bname,
            bauthor=bauthor
        )
        book.save()
        return redirect('index')
    return render(request,'index.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def edit(request):
    book = Library.objects.all()

    context={
        'books':book,
    }
    # On edit it will show us the previous name
    return render(request,'index.html',context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def update(request,id):
    if request.method=="POST":
        bname=request.POST.get('bname')
        bauthor=request.POST.get('bauthor')
        book=Library(
            id=id,
            bname=bname,
            bauthor=bauthor
        )
        book.save()
        return redirect('index')
    return render(request,'index.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delete(request,id):
    book=Library.objects.filter(id=id)
    book.delete()
    context={
        'books':book,
    }
    return redirect("index")