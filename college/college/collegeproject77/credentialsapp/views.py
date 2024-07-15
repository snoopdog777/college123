from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return render(request, "newpage.html")
        else:
            messages.info(request, "Invalied credentials")
            return redirect('login')
    return render(request,'login.html')


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:

            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect('register')

            # elif User.objects.filer(username=Username).exists():
            #     messages.info(request, "Username already exists")
            #     return redirect('register')


            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save();
                return redirect('login')

        else:
            messages.info(request,"Password does not match")
            return redirect('register')
        return redirect('/')

    return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def newpage(request):
    return render(request, "newpage.html")

def form(request):
    return render(request,'form.html')