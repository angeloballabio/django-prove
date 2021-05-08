from django import forms
from .models import Cartella


class PostCartellaForm(forms.ModelForm):
    # nome_cartella = forms.CharField()
    # tempo_riproduzione = forms.IntegerField()
    
    class Meta:
        model = Cartella
        fields = ('nome_cartella', 'tempo_riproduzione')
