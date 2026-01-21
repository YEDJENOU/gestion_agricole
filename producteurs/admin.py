from django.contrib import admin
from .models import Producteur, Arrondissement, Commune

@admin.register(Commune)
class CommuneAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)

@admin.register(Arrondissement)
class ArrondissementAdmin(admin.ModelAdmin):
    list_display = ('nom', 'commune')
    search_fields = ('nom', 'commune__nom')
    list_filter = ('commune',)

@admin.register(Producteur)
class ProducteurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'telephone', 'arrondissement', 'superficie')
    search_fields = ('nom', 'telephone', 'arrondissement__nom')
    list_filter = ('arrondissement',)
