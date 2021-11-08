from django import forms

from .models import Lote, Picole

class LoteForm(forms.ModelForm):

    class Meta:
        model = Lote
        fields = ('estoque', 'vendedor_origem','data_compra','data_validade','quantidade_picoles','preco_lote')


class PicoleForm(forms.ModelForm):

    class Meta:
        model = Picole
        fields = ('marca', 'sabor','calorias','peso','temperatura_ideal')