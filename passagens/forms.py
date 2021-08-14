from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from .class_viagem import tipos_de_classe
from .validaion import *


class PassagemForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    data_ida = forms.DateField(label='Ida', widget=DatePicker())
    data_volta = forms.DateField(label='Volta', widget=DatePicker())
    datapesquisa = forms.DateField(
        label='Data da Pesquisa', disabled=True, initial=datetime.today)
    class_viagem = forms.ChoiceField(
        label='classe do vôo', choices=tipos_de_classe)
    informacoes = forms.CharField(
        label='Informações extras',
        max_length=200,
        widget=forms.Textarea(),
        required=False
    )
    email = forms.EmailField(label='E-mail', max_length=150)

    def clean(self):
        # Campos do Formulário
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        datapesquisa = self.cleaned_data.get('datapesquisa')
        lista_de_erros = {}

        # funções
        campo_tem_algum_numero(origem, 'origem', lista_de_erros)
        campo_tem_algum_numero(destino, 'destino', lista_de_erros)
        origem_destino_iguais(origem, destino, lista_de_erros)
        data_ida_maior_data_volta(data_ida, data_volta, lista_de_erros)
        verifica_data_da_compra(data_ida, data_volta, lista_de_erros)
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data
