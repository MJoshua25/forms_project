from django.urls import path

from . import views

urlpatterns = [
    path('inscription',views.inscription, name="inscription"),
    path('connexion',views.connexion, name="connexion"),
    path('dashboard',views.dashboard, name="dashboard"),
    path('deconnection',views.deconection,name='deconection'),
    path('fake',views.fake,name='fake'),
]