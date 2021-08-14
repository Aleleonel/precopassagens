def origem_destino_iguais(origem, destino, lista_de_erros):
    """Verifica se origem e destinos são iguais"""
    if origem == destino:
        lista_de_erros['destino'] = (
            'Atenção', 'O Destino não pode ser igual a Origem'
            )


def campo_tem_algum_numero(valor_campo, nome_campo, lista_de_erros):
    """Verifica se tem algum digito numérico"""
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = (
            'Atenção Somente letras'
            )


def data_ida_maior_data_volta(data_ida, data_volta, lista_de_erros):
    """Verifica a Dta de ida se  é maior que data de volta"""
    if data_ida > data_volta:
        lista_de_erros['data_volta'] = 'Data de Volta é menor que data da ida,\
        voltar no tempo ainda não esta diponível em sua Era.'


def verifica_data_da_compra(data_ida, datapesquisa, lista_de_erros):
    "Verifica se a data da compra é anterior a data da do dia - consulta"
    if data_ida < datapesquisa:
        lista_de_erros['data_ida'] = 'Consulta inválida! Data de ida inferior\
        a data de hoje'
