from django.contrib import admin

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

    list_display = ('id', 'titre', 'lien', 'date_add', 'date_upd', 'statut')
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


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Profile, ProfileAdmin)
_register(models.Y_Video, Y_VideoAdmin)
