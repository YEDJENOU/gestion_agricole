from django.contrib import admin
from .models import Recolte, Culture

@admin.register(Culture)
class CultureAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)

@admin.register(Recolte)
class RecolteAdmin(admin.ModelAdmin):
    list_display = ('producteur', 'culture', 'quantite', 'date')
    search_fields = ('producteur__nom', 'culture__nom')
    list_filter = ('culture', 'date')
