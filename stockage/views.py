from django.shortcuts import render, redirect
from .forms import StockForm
from .models import Stock

# Liste du stock
def liste_stock(request):
    stocks = Stock.objects.all()
    return render(request, 'stockage/liste_stock.html', {'stocks': stocks})

# Ajouter un stock
def ajouter_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_stock')
    else:
        form = StockForm()
    return render(request, 'stockage/ajouter_stock.html', {'form': form})
