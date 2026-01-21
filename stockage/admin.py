from django.contrib import admin
from .models import Stock

class StockAdmin(admin.ModelAdmin):
    list_display = ['producteur', 'type_stock', 'quantite']
    list_filter = ['type_stock']

admin.site.register(Stock, StockAdmin)
