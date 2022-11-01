from django import forms
from RPG.validar import *
from RPG.models import Personagem1
class Personagem(forms.ModelForm):
    class Meta():
        model = Personagem1
        fields = '__all__'
    

    def clean(self):
        nome = self.cleaned_data.get('nome')
        idade = self.cleaned_data.get('idade')
        classe_Person = self.cleaned_data.get('classe_Person')
        Raca = self.cleaned_data.get('Raca')
        destino = self.cleaned_data('destino')
        listaErros = {}

        NomeComNumero(nome, 'nome', listaErros)
        NaoTemNumero(idade, 'idade', listaErros)
        Classe (classe_Person, listaErros)
        SemRumo(destino, listaErros)

        if listaErros is not None:
            for erro in listaErros:
                mensagem_erro = listaErros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data