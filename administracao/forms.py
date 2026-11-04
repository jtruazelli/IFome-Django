from django import forms
from cardapio.models import Cardapio

class CardapioForm(forms.ModelForm):
    class Meta:
        model = Cardapio
        fields = ['data', 'refeicao_manha', 'refeicao_almoco', 'refeicao_tarde']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'refeicao_manha': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Ex:\nPão com manteiga\nCafé com leite'}),
            'refeicao_almoco': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Ex:\nArroz e Feijão\nGalinhada\nSalada verde'}),
            'refeicao_tarde': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Ex:\nSuco de laranja\nBiscoito integral'}),
        }