from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models


class ProfileAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'contacts', 'image', 'birth_date')
    list_filter = (
        'user',
        'birth_date',
        'id',
        'user',
        'contacts',
        'image',
        'birth_date',
    )


class Y_VideoAdmin(admin.ModelAdmin):

    list_display = ('affiche_video','id', 'titre', 'lien', 'date_add', 'date_upd', 'statut')
    list_filter = (
        'date_add',
        'date_upd',
        'statut',
        'id',
        'titre',
        'lien',
        'date_add',
        'date_upd',
        'statut',
    )

    def affiche_video(self, obj):
        return  mark_safe('<iframe width="84" height="63"src="{url}"></iframe>'.format(url=obj.lien))


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Profile, ProfileAdmin)
_register(models.Y_Video, Y_VideoAdmin)
