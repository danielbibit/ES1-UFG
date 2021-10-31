from django.contrib import admin

# Register your models here.
from .models import Lote, Picole, Vendas

admin.site.register(Lote)
admin.site.register(Picole)
admin.site.register(Vendas)