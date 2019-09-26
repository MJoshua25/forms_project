from django.db import models

# Create your models here.
# Import

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver




#----------------------------------- USER -->> PROFILE --------------------------------#

class Profile(models.Model):

    # Appel de user
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')  # 1 user <---> 1 profil
    
    # Champs suplementaires
    
    contacts = models.CharField(max_length=30, null=True)
    image = models.ImageField(upload_to='profile/', default='useravatar.jpg')
    birth_date = models.DateField(null=True)

    # Initialisation a la creation
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, created, **kwargs):
        
        instance.profile.save()


class Y_Video(models.Model):
    """Model definition for Y_Video."""

    # TODO: Define fields here
    titre = models.CharField(max_length=250)
    lien = models.URLField(max_length=300)
    date_add = models.DateTimeField(auto_now=True)
    date_upd = models.DateTimeField(auto_now_add=True)
    statut = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Y_Video."""

        verbose_name = 'Y_Video'
        verbose_name_plural = 'Y_Videos'

    def __str__(self):
        """Unicode representation of Y_Video."""
        return self.titre
