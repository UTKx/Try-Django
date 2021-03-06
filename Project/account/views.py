from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
    
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!!')
                return redirect('/auth/register/')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists!!')
                return redirect(request, '/auth/register/')
            else:
                user = User.objects.create_user(username=username, first_name=name, last_name=lastname, email=email, password=password)
                user.save()
                return redirect('/')
        else:
            messages.error(request, 'Password did not match')
            return redirect('/auth/register/')

    return render(request, 'registered.html')

# def show(request):
#     name = request.POST.get('name')
#     lastname = request.POST.get('lastname')
#     email = request.POST.get('email')
#     password = request.POST.get('password')
#     cpassword = request.POST.get('cpassword')
#     data = name, lastname, email, password, cpassword
#     return render(request, 'showregister.html', {"data": data})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid username or password!!')
            return redirect('/auth/login/')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
