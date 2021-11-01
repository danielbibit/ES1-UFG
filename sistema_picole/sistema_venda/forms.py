from django import forms

from .models import Lote

class EstoqueForm(forms.ModelForm):

    class Meta:
        model = Lote
        fields = ('estoque', 'data_compra')