from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from . import models
# Create your views here.
def connexion(request):
    return render(request, 'connexion.html')


def inscription(request):
    data:{
        'message': "",
    }
    if request.method== 'POST':
        nom_p = request.POST.get('name')
        nom_full = nom_p.split(" ")
        nom = nom_full[0]
        prenom = " ".join(nom_full[1:])
        contact = request.POST.get('contact')
        birth = request.POST.get('birth_date')
        img = request.FILES.get('image')
        email = request.POST.get('email')
        username = request.POST.get('username')
        mdp = request.POST.get('pass')
        conf_mdp = request.POST.get('repeat-pass')
        try:
            user = User(
                first_name = nom,
                last_name = prenom,
                email = email,
                username = username
            )
            user.set_password(mdp)
            user.save()
            user.profile.contacts = contact
            user.profile.image = img
            user.profile.birth_date = birth
            user.save()
        except:
            data['message'] = "veuillez remplir correctement le formulaire"
        return render(request, 'inscription.html')
    else:
        return render(request, 'inscription.html')


def connexion(request):
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


@login_required(login_url='connexion')
def dashboard(request):
    titre = request.GET.get('titre')
    vi = models.Y_Video.objects.filter(statut=True)
    if titre:
        vi = vi.filter(titre__icontains=titre)
    paginator = Paginator(vi, 10)
    page = request.GET.get('page')
    try:
        vi = paginator.page(page)
    except PageNotAnInteger:
        vi = paginator.page(1)
    except:
        vi = paginator.page(paginator.num_pages)
    data = {
        'user': request.user,
        'videos': vi,
    }
    return render(request, 'dashboard.html', data)


def deconection(request):
    logout(request)
    return redirect('connection')