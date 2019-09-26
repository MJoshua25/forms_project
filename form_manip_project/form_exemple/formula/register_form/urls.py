
from django.urls import path,include
from . import views
urlpatterns = [
    path('connexion',views.connect,name='connection'),
    path('inscription',views.register,name='inscription'),
    path('',views.login),
    path('started',views.home,name='dashboard'),
    path('deconnection',views.deconection,name='deconection'),
]
