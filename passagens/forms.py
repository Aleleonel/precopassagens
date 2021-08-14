from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from .class_viagem import tipos_de_classe
from .validaion import *
from passagens.models import Passagem, ClasseViagem, Pessoa


class PassagemForms(forms.ModelForm):
    datapesquisa = forms.DateField(label='Data da Pesquisa', disabled=True, initial=datetime.today)

    class Meta:
        model = Passagem
        fields = '__all__'
        labels = {
                'origem': 'Local da Partida',
                'destino': 'Destino',
                'data_ida': 'Data de Partida',
                'data_volta': 'Data de Retorno',
                'datapesquisa': 'Data da Pesquisa',
                'class_viagem': 'Classe',
                'informacoes': 'Informações',
                }
        widgets = {
            'data_ida': DatePicker(),
            'data_volta': DatePicker()
        }


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
        verifica_data_da_compra(data_ida, datapesquisa, lista_de_erros)
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data
