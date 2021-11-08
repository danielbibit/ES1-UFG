from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Lote, Picole, Vendas
from .forms import LoteForm, PicoleForm, VendaForm

def index(request):
    lotes = Lote.objects.all()
    picoles = Picole.objects.all()
    #estoque/lista.html
    return render(request, 'estoque/sistema.html',{'lotes': lotes, 'picoles': picoles} )

def venda(request):
    vendas = Vendas.objects.all()
    lotes = Lote.objects.all()
    picoles = Picole.objects.all()

    return render(request, 'venda/lista.html',{'vendas': vendas, 'lotes': lotes, 'picoles': picoles} )

def estoque(request):
    lotes = Lote.objects.all()
    picoles = Picole.objects.all()

    return render(request, 'estoque/lista.html',{'lotes': lotes, 'picoles': picoles} )

def adiciona_venda(request):
    form = VendaForm()
    return render(request, 'venda/nova_venda.html', {'form': form})

def adiciona_lote(request):
    form = LoteForm()
    return render(request, 'estoque/novo_estoque.html', {'form': form})

def adiciona_picole(request):
    form = PicoleForm()
    return render(request, 'estoque/novo_picole.html', {'form': form})

def edit_estoque(request, id):
    estoque = get_object_or_404(Lote, pk=id)
    form = LoteForm(instance=estoque)
    return render(request, 'estoque/edit_estoque.html', {'form': form,'estoque': estoque })

def edit_venda(request, id):
    venda = get_object_or_404(Vendas, pk=id)
    form = VendaForm(instance=venda)
    return render(request, 'venda/edit_venda.html', {'form': form,'venda': venda })

