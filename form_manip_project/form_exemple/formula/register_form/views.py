from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method == "POST":
        nom=request.POST.get('nom')   
        prenom=request.POST.get('prenom')   
        contact=request.POST.get('contact')
        date=request.POST.get('date')
        image=request.FILES.get('image')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('pass')
        repeat_pass=request.POST.get('repeat-pass')
        print('\r\n',nom,prenom,contact,date,image,email,username,password,repeat_pass,'\r\n')
        if password == repeat_pass:
            user = User(
                username=username,
                first_name=nom,
                last_name=prenom,
                email=email
            )
            try:
                user.save()
                user.profile.contacts=contact
                user.profile.image=image
                user.profile.birth_date=date
                user.save()
                user.password = password
                user.set_password=user.password
                user.save()
                print('success')
            except:
                print('error')

    return render(request,'register.html')

def connect(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        _next = request.GET.get('next', False)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            
            print("user is login")

            login(request, user)
            if _next: 
                return redirect(_next)
            else:
                return redirect('dashboard')
        else:
            return render(request, 'connexion.html')
    return render(request, 'connexion.html')
@login_required(login_url='connection')
def home(request):
    return render(request,'dashboard.html')

def deconection(request):
    logout(request)
    return redirect('connection') 