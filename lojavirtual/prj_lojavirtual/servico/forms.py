
from django import forms

OPCOES_QUANTIDADE_SERVICO = []

for i in range(1,6):
    OPCOES_QUANTIDADE_SERVICO.append((i,str(i)))    

class FormAdicionarServicoAoCarrinho(forms.Form):
    quantidade = forms.TypedChoiceField(
        choices=OPCOES_QUANTIDADE_SERVICO, coerce=int)
    
    atualizar = forms.BooleanField(required=False, widget=forms.HiddenInput)