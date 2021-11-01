from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Lote, Picole
from .forms import EstoqueForm

def index(request):
    lotes = Lote.objects.all()
    picoles = Picole.objects.all()
    return render(request, 'estoque/lista.html',{'lotes': lotes, 'picoles': picoles} )

def estoque(request, id):
    estoque = get_object_or_404(Lote, pk=id)
    return render(request, 'estoque/estoque.html', {'estoque': estoque})

def adiciona_estoque(request):
    form = EstoqueForm()
    print('entrei')
    return render(request, 'estoque/novo_estoque.html', {'form': form})

def edit_estoque(request, id):
    estoque = get_object_or_404(Lote, pk=id)
    form = EstoqueForm(instance=estoque)
    return render(request, 'estoque/edit_estoque.html', {'form': form,'estoque': estoque })
