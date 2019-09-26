# vim: set fileencoding=utf-8 :
from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models


class ProfileAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'contacts', 'affiche_image', 'birth_date')
    list_filter = (
        'user',
        'birth_date',
        'id',
        'user',
        'contacts',
        'birth_date',
    )
    def affiche_image(self, obj):
        return mark_safe('<img src="{url}" width="100" height="100" > </img>'.format(url = obj.image.url))

class YoutubeAdmin(admin.ModelAdmin):

    list_display = ('id', 'titre', 'url', 'statut', 'date_add', 'date_upd')
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
        'id',
        'titre',
        'url',
        'statut',
        'date_add',
        'date_upd',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Profile, ProfileAdmin)
_register(models.Youtube, YoutubeAdmin)
