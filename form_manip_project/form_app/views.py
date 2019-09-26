from django.shortcuts import render
from django.contrib.auth.models import User
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


def dashboard(request):
    return render(request, 'dashboard.html')