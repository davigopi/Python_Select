from ast import Return
import copy
# from tarfile import DEFAULT_FORMAT
# import time
from datetime import datetime
import sys
# import json
# from tkinter import N
# import re

# from dotenv import set_key
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from decimal import Decimal

from read_salve import Read_salve

# from tempo import Tempo
# from log import Log
from conexao import Conexao
# import pandas as pd
# from tratar import Tratar
from renomear import Renomear
from var import *
# from chromeDriverauto  import ChromeDriverAuto
# from convert import Convert
from analiseConsorcio import AnaliseConsorcio

conexao = Conexao()
renomear = Renomear()
read_salve = Read_salve()
# analiseConsorcio = AnaliseConsorcio()


def is_list_data_valida(list_data):
    if isinstance(list_data, list):
        for dt in list_data:
            try:
                datetime.strptime(dt, "%d/%m/%Y")
                return True
            except (ValueError, TypeError):
                return False
    else:
        return False

def order_date(list_order, order_reverse):
    return sorted(list_order, key=lambda x: datetime.strptime(x, "%d/%m/%Y"), reverse=order_reverse)  

def salve_arq(write_file, folder_file):
    read_salve.write_file = write_file
    read_salve.folder_file = folder_file
    read_salve.to_write()

def read_arq(folder_file):
    read_salve.folder_file = folder_file
    return read_salve.to_read()

class Treat():
    def __init__(self, *args, **kwargs):
        self.disc_newcon = None

    def get_arq_list(self, path):
        try:
            list_dict_running = read_arq(path)
            if isinstance(list_dict_running, list):
                self.disc_newcon = list_dict_running
                return True
            print(f'O arquivo {list_dict_running} que esta sendo lido não é lista, é: {type(list_dict_running)}.')
            sys.exit()
        except Exception as e:
            print(f'O arquivo {list_dict_running} não dá pra converter: {e}.')
            sys.exit()

    # Excluir do dicionários que tive o key_focus com valor value_focus
    def del_disc_with_value_key(self, key_focus, value_focus):
        list_dict_running = []
        for dict_row in self.disc_newcon:
            if dict_row[key_focus] == value_focus:
                continue
            list_dict_running.append(dict_row)
        self.disc_newcon = list_dict_running
        return True
    
    # Excluir do key_del de todos os dicionários
    def del_key_from_dict(self, list_key_del):
        list_dict_running = []
        for dict_row in self.disc_newcon:
            for key_del in list_key_del:
                dict_row.pop(key_del, None)
            list_dict_running.append(dict_row)
        self.disc_newcon = list_dict_running
        return True
    
    #Excluir dos dicionários como o mesmo valor do key_controle
    def del_dict_repetition_key_controle(self):
        list_dict_running = []
        list_key_repetition = []
        for dict_row in self.disc_newcon:
            if dict_row[key_controle] in list_key_repetition:
                continue
            list_key_repetition.append(dict_row[key_controle])
            list_dict_running.append(dict_row)
        self.disc_newcon = list_dict_running
        return True
    
    # Criar colunas juntando outras colunas existentes, para realizar pesquisas mais a frente
    def create_key_controle(self, list_keys_join):
        list_dict_running =[]
        for dict_row in self.disc_newcon:
            dict_row[key_controle] = ''.join(str(dict_row[col]) for col in list_keys_join if col)
            list_dict_running.append(dict_row)
        self.disc_newcon = list_dict_running
        return True
    
    # criar um key_new com os valores que estão dentro do dicinário key_focus com valor key_dict_in_3 e colo o operator como chave
    #                                              'Lance'   ,     +       ,     '%'      ,     '-'      ,   'Desclassificados'
    def create_key_desclassificados_and_join(self, key_focus, key_dict_in_1, key_dict_in_2, key_dict_in_3, key_new):
        list_dict_running =[]
        for dict_row in self.disc_newcon: 
            dict_row_new = copy.deepcopy(dict_row) 
            # dict_out_new = {}
            dict_new_1 = {}
            dict_new_3 = {}
            i_1=0
            i_3=0
            for key_out, value_out in dict_row[key_focus].items():
                if key_dict_in_1 in value_out:
                    i_1+=1
                    dict_new_1[i_1] = {value_out[key_dict_in_2]: value_out[key_dict_in_1]}  
                    # dict_out_new[key_out] = value_out
                if key_dict_in_3 in value_out:
                    i_3+=1
                    dict_new_3[i_3] = {value_out[key_dict_in_2]: value_out[key_dict_in_3]}
            dict_row_new[key_new] = {i_3: dict_new_3}
            dict_row_new[key_focus] = {i_1: dict_new_1}
            list_dict_running.append(dict_row_new)
        self.disc_newcon = list_dict_running
        return True
            
    # Criar key_new de quantidade que se repete value_focus
    def create_key_quantity(self, key_compare, value_focus, key_new):
        list_dict_running =[]
        for dict_row in self.disc_newcon: 
            dict_row_new = copy.deepcopy(dict_row) 
            count_value = 0
            for dict_row_2 in self.disc_newcon:
                if dict_row[key_controle] == dict_row_2[key_controle] and dict_row_2[key_compare] == value_focus:
                    count_value += 1
            dict_row_new[key_new] = count_value
            list_dict_running.append(dict_row_new)
        self.disc_newcon = list_dict_running
        return True
    
    # criar um key_new_list com valores key_dict_join e organiza pela data de key_dict_join o operador ser a incluido no key
    def create_key_list_value_order(self, key_dict_join, key_new_list, operator, order_revese):
        list_dict_running = []
        for dict_row in self.disc_newcon:
            dict_row_new = copy.deepcopy(dict_row)
            dict_key_order = {}
            list_key_order = []
            for dict_row_2 in self.disc_newcon:
                if dict_row[key_controle] == dict_row_2[key_controle]:
                    dict_key_order[dict_row_2[key_dict_join]] = dict_row_2[key_dict_join]
                    list_key_order.append(dict_row_2[key_dict_join])
            if is_list_data_valida(list_key_order):
                list_key_order = order_date(list_key_order, order_revese)
            disc_key_order = {}
            for key, value_order in enumerate(list_key_order, start=1):
                disc_key_order[str(key)+operator] = dict_key_order[value_order]
            dict_row_new[key_new_list]  = disc_key_order
            list_dict_running.append(dict_row_new)
        self.disc_newcon = list_dict_running
        return True

    # atravez do dicionario criado dts_Confirmações e compara a data com a data key_dict s pega o numero key 
    # ['Lance', 'Desclassificados', 'Desclassificados_Fixo', 'Fixo'], 'Dt. Confirmação', 'Datas', 'Qts_Sorteios'
    def create_keys_dict(self, list_keys_focus, key_focus_2, key_dict_focus, key_unique):
        list_dict_running = []
        for dict_row in self.disc_newcon:
            dict_row_new = copy.deepcopy(dict_row)
            for key, value in dict_row[key_dict_focus].items():
                if dict_row[key_focus_2] != value:
                    continue
                for key_focus in list_keys_focus:
                    if key_focus == key_unique and '1' not in key:
                        dict_row_new[key_focus] = {}
                        continue
                    dict_key_alter = {}
                    dict_key_alter[key] = dict_row[key_focus]
                    dict_row_new[key_focus] = dict_key_alter
            list_dict_running.append(dict_row_new)
        self.disc_newcon = list_dict_running
        return True

    def create_key_min_max_find_value(self, list_keys_focus, key_new_1, key_new_2):
        list_dict_running = []
        for dict_row in self.disc_newcon:
            dict_row_new = copy.deepcopy(dict_row)
            list_values = [
                round(value * 100 / float(key), 2)
                for key_focus in list_keys_focus
                for dict_value_1 in dict_row[key_focus].values()
                for dict_value_2 in dict_value_1.values()
                for dict_value_3 in dict_value_2.values()
                for dict_value_4 in dict_value_3.values()
                for key, value in dict_value_4.items()
            ]
            list_values.sort()
            dict_row_new[key_new_1] = min(list_values)
            dict_row_new[key_new_2] = max(list_values)
            list_dict_running.append(dict_row_new)
        self.disc_newcon = list_dict_running
        return True      

    # Juntar colunas e colocar em um nova coluna com seus novos value
    #                 'Vr. Lance', '% Lance', 'tabela',     '+',                  '%',           '-',       'confirmada', 'Lance'
    def join_keys(self, key_join_1, key_join_2, key_join_3, key_new_name_1, key_new_name_2, key_new_name_3, value_focus, key_new):
        list_dict_running = []
        for dict_row in self.disc_newcon:
            dict_row_new = copy.deepcopy(dict_row)
            dict_new_column = {}
            # iraz negativar se não for confirmado
            if dict_row[key_join_3] == value_focus:
                dict_new_column[key_new_name_1] = Renomear(inf=dict_row[key_join_1]).valor()
                dict_new_column[key_new_name_2] = Renomear(inf=dict_row[key_join_2]).valor()
            else:
                dict_new_column[key_new_name_3] = Renomear(inf=dict_row[key_join_1]).valor()
                dict_new_column[key_new_name_2] = Renomear(inf=dict_row[key_join_2]).valor()
                # dict_new_column[key_new_name_3] = Renomear(inf=dict_row[key_join_1]).valor() 
            dict_row_new[key_new] = dict_new_column
            list_dict_running.append(dict_row_new)
        self.disc_newcon = list_dict_running
        return True

    # juntar valuees key_dict vai orderando em ordem decrecente pelo key_dict_in. Alé de deixar apena um key_compre
    #                                                         'Lance' ,     '+'      ,     '%'           '-'
    def join_key_dict_order_key_dist_in_renoma_jey_name(self, key_dict, key_dict_in_1, key_dict_in_2, key_dict_in_3):
        list_dict_running = []
        for dict_row in self.disc_newcon:
            dict_row_new = copy.deepcopy(dict_row)
            list_dict_focus = []
            for dict_row_2 in self.disc_newcon:
                if dict_row[key_controle] == dict_row_2[key_controle]:
                    list_dict_focus.append(dict_row_2[key_dict])
            list_dict_focus = sorted(list_dict_focus, key=lambda x: (x.get(key_dict_in_2, 0), x.get(key_dict_in_1, 0), x.get(key_dict_in_3, 0)), reverse=True) 
            dict_new_rumning = {}
            for key, dict_row3 in enumerate(list_dict_focus, start=1):
                dict_new_rumning[str(key)] = dict_row3 
            dict_row_new[key_dict] = dict_new_rumning
            list_dict_running.append(dict_row_new)
        self.disc_newcon = list_dict_running
        return True

    # pegar todos os valores key_new e key_add das tabelas key_equate com valor value_equate e coloca eles na mesma tabela no key mas com valor value_equate_2 em key_new_2 e key_add
    #                      'Modalidade', 'Lance Fixo', 'Lance', 'Desclassificados', 'Fixo', 'Desclassificados_Fixo'
    def join_key_focus(self, key_equate, value_equate, key_focus_1, key_focus_2, key_new_1, key_new_2):
        dict_fixo = {}
        for dict_row in self.disc_newcon:
            if dict_row[key_equate] == value_equate:
                dict_fixo[dict_row[key_controle]] = [dict_row[key_focus_1], dict_row[key_focus_2]]
        list_dict_running = []
        for dict_row in self.disc_newcon:
            dict_row_new = copy.deepcopy(dict_row)
            for key, value in dict_fixo.items():
                if dict_row[key_controle] == key:
                    dict_row_new[key_new_1] = value[0]
                    dict_row_new[key_new_2] = value[1]
            list_dict_running.append(dict_row_new)
        self.disc_newcon = list_dict_running
        list_create_key_if_not_exist = [key_focus_2, key_new_1, key_new_2]
        list_dict_running = []
        for dict_row in self.disc_newcon:
            dict_row_new = copy.deepcopy(dict_row)
            for key in list_create_key_if_not_exist:
                if key not in dict_row:
                    dict_row_new[key]  = {}
            list_dict_running.append(dict_row_new)
        self.disc_newcon = list_dict_running
        return True

    # juntar os valores de texto de todos das leitas key_focus e com o mesmo key_controle e ordena eles no mesmo sentido do dicionario key_dict_focus
    # ['Desclassificados', 'Desclassificados_Fixo', 'Fixo'], 'Dt. Confirmação', 'Datas'
    def join_key_list(self, list_key_focus, key_focus_2, key_dict_focus):
        list_dict_running = []
        for dict_row in self.disc_newcon:
            dict_row_new = copy.deepcopy(dict_row)
            for key_focus in list_key_focus:
                dict_new = {}
                for dict_row_2 in self.disc_newcon:
                    if dict_row[key_controle] == dict_row_2[key_controle]:
                        dict_new.update(dict_row_2.get(key_focus, {}))
                dict_new = dict(sorted(dict_new.items()))
                dict_row_new[key_focus] = dict_new            
            list_dict_running.append(dict_row_new)
        self.disc_newcon = list_dict_running
        return True

    # Juntar toda as data de key_focus tranformando as datas em intervalo em dias referenta a key_date_compare
    #                           'Datas'
    def join_key_dict_date(self, key_focus, operator):
        list_dict_running = []
        for dict_row in self.disc_newcon:
            dict_row_new = copy.deepcopy(dict_row)
            str_new = ''
            for key, value in dict_row[key_focus].items():
                str_new_temp = ''
                for key_2, value_2 in value.items():
                    if not value_2:
                        continue
                    renomear.inf = value_2
                    date_focus = renomear.str_to_date()
                    if '1' in key_2:
                        date_start = date_focus
                        renomear.inf = date_focus
                        str_new_temp = renomear.date_to_str()
                        str_new_temp = key + key_2 + ' ' + str_new_temp
                        continue
                    dif_date = str((date_focus - date_start).days) + operator
                    str_new_temp = str_new_temp + ', ' + key_2  + ' ' + dif_date
                if not str_new:
                    str_new = str_new_temp
                    continue
                str_new = str_new  + '  |  ' + str_new_temp
            dict_row_new[key_focus] = str_new
            list_dict_running.append(dict_row_new)
        self.disc_newcon = list_dict_running
        return True

    def join_key_5_dict_prec_fix(self, list_key_focus, operator):
        list_dict_running = []
        for dict_row in self.disc_newcon:
            dict_row_new = copy.deepcopy(dict_row)
            for key_focus in list_key_focus:
                str_new_1 = ''
                perc_fix = ''
                for key_1, dict_value_1 in dict_row[key_focus].items():
                    quant_new = sum(
                        int(key_3)
                        for dict_value_2 in dict_value_1.values()
                        for key_3 in dict_value_2.keys()
                    )
                    perc_fix = next(
                        (
                            key_5
                            for dict_value_2 in dict_value_1.values()
                            for dict_value_3 in dict_value_2.values()
                            for dict_value_4 in dict_value_3.values()
                            for key_5 in dict_value_4
                        ),
                        None
                    )
                    if not str_new_1:
                        str_new_1 =  key_1 + str(quant_new) 
                        continue
                    str_new_1 = str_new_1 + "  |  " + key_1 + str(quant_new) 
                if perc_fix:
                    str_new_1 = str(round(perc_fix, 1)) + operator + str_new_1
                dict_row_new[key_focus] = str_new_1
            list_dict_running.append(dict_row_new)
        self.disc_newcon = list_dict_running
        return True
    
    def join_key_5_dict_prec_dif(self, list_key_focus, operator):
        list_dict_running = []
        for dict_row in self.disc_newcon:
            dict_row_new = copy.deepcopy(dict_row)
            for key_focus in list_key_focus:
                str_new_1 = ''
                perc_dif = ''
                for key_1, dict_value_1 in dict_row[key_focus].items():
                    quant_new = sum(
                        int(key_3)
                        for dict_value_2 in dict_value_1.values()
                        for key_3 in dict_value_2.keys()
                    )
                    perc_dif = ', '.join(
                        str(round(key_5, 1))
                        for dict_value_2 in dict_value_1.values()
                        for dict_value_3 in dict_value_2.values()
                        for dict_value_4 in dict_value_3.values()
                        for key_5 in dict_value_4
                    )
                    if perc_dif:
                        str_new_2 = key_1 + str(quant_new) + ' [' + perc_dif + ']' + operator
                    else:
                        str_new_2 = key_1 + str(quant_new) 
                    if not str_new_1:
                        str_new_1 = str_new_2
                        continue
                    str_new_1 = str_new_1 + "  |  " + str_new_2
                dict_row_new[key_focus] = str_new_1
            list_dict_running.append(dict_row_new)
        self.disc_newcon = list_dict_running
        return True

    def join_key_3_dict(self, list_key_focus):
        list_dict_running = []
        for dict_row in self.disc_newcon:
            dict_row_new = copy.deepcopy(dict_row)
            for key_focus in list_key_focus:
                str_new_1 = ''
                qnt = 0
                for key_1, dict_value_1 in dict_row[key_focus].items():
                    for value in dict_value_1.values():
                        qnt = value
                    str_new_2 =  key_1  + str(round(qnt))
                    if not str_new_1:
                        str_new_1 =  str_new_2
                        continue
                    str_new_1 = str_new_1 + "  |  " + str_new_2 
                dict_row_new[key_focus] = str_new_1
            list_dict_running.append(dict_row_new)
        self.disc_newcon = list_dict_running
        return True

    def test_disc_newcon(self):
        i = 0
        for dict_row in self.disc_newcon:
            if dict_row['grupo'] != "003320":
                continue
            if dict_row["Modalidade"] != "Lance Livre":
                continue
            if dict_row['tabela'] != 'desclassificada':
                continue
            if dict_row['Dt. Contemplação'] != '26/11/2025':
                continue
            i += 1
        print(i)

    def get_key_5_dict_prec_dif(self, list_key_focus, new_key):
        list_dict_running = []
        for dict_row in self.disc_newcon:
            dict_row_new = copy.deepcopy(dict_row)
            for key_focus in list_key_focus:
                list_month = []
                for dict_value_1 in dict_row[key_focus].values():
                    if valores := [
                        round(key_5, 1)
                        for dict_value_2 in dict_value_1.values()
                        for dict_value_3 in dict_value_2.values()
                        for dict_value_4 in dict_value_3.values()
                        for key_5 in dict_value_4
                    ]:
                        list_month.append(valores)
            dict_row_new[new_key] = list_month 
            list_dict_running.append(dict_row_new)
        self.disc_newcon = list_dict_running
        return True

    def anbalyze_consortium(self, key_focus_1, key_focus_2, key_focus_3 ):
        list_dict_running = []
        for dict_row in self.disc_newcon:
            dict_row_new = copy.deepcopy(dict_row)
            analise = AnaliseConsorcio(
                months=dict_row[key_focus_1],
                prazo=dict_row[key_focus_2],
                realizadas=dict_row[key_focus_3]
            )
            dict_row_new.update(analise.sugestao_lances())
            list_dict_running.append(dict_row_new)
        self.disc_newcon = list_dict_running
        return True

        
    def organizar_newcon_full(self):
        self.get_arq_list(path_newcon_json)

        self.del_disc_with_value_key('tabela', cancelada)
        self.del_disc_with_value_key('Modalidade', '')

        self.del_key_from_dict(['Cota', 'Bem', 'Filial', 'Dt.Desclassificação', 'Pto. Venda'])

        # self.create_key_controle([grupo, 'Dt. Confirmação', 'Modalidade', 'tabela'])
        # salve_arq(self.disc_newcon, path_newcon_json_tratado)
        # return

        # # ira testar quantidade e imprimir na tela para saber se esta correto as quantidades
        # self.test_disc_newcon()

        # OBJETIVO 1: ISOLAR INFORMAÇÕES EM UM ÚNICO DICIONÁIRO PARA CADA GRUPO
        # bloco qu3e ira criar a quantidades de sorteios e coloca no lance livre e exclui todos os campos sorteios
        self.create_key_controle([grupo, 'Dt. Contemplação'])
        self.create_key_quantity('Modalidade', 'Sorteio', 'Qts_Sorteios')
        self.del_disc_with_value_key('Modalidade', 'Sorteio')
     
        # Bloco vai juntar todos os valores e porcentagem de lance juntando em um unico lance com valor de dicionario alem de ordenar
        self.create_key_controle([grupo, 'Modalidade', 'Dt. Contemplação', 'Dt. Confirmação'])
        self.join_keys('Vr. Lance', '% Lance', 'tabela', '+', '%', '-', 'confirmada', 'Lance')
        self.del_key_from_dict(['Vr. Lance', '% Lance', 'tabela'])
        self.join_key_dict_order_key_dist_in_renoma_jey_name('Lance', '+', '%', '-')
        self.del_dict_repetition_key_controle()

        # Todos valores no key '-' dentor do key pai 'Lance', cria um novo key 'Desclassificados' colocando sua quantidades e seus dicionários 
        self.create_key_desclassificados_and_join('Lance', '+', '%', '-', 'Desclassificados')

        # Bloco pegar todas Modalidade Lance fixo e coloca em uma no key Fixo e Desclassificado_Fixo entro da modalidade Lance Livre e depois apaga todas modalidade lance fixo
        self.create_key_controle([grupo, 'Dt. Contemplação', 'Dt. Confirmação'])
        self.join_key_focus('Modalidade', 'Lance Fixo', 'Lance', 'Desclassificados', 'Fixo', 'Desclassificados_Fixo')
        self.del_disc_with_value_key('Modalidade', 'Lance Fixo')

        # juntar de lances, desclassifidados, desclassificado_fixo e fixo com a mesma data de confirmações
        self.create_key_controle([grupo, 'Modalidade', 'Dt. Contemplação'])
        self.create_key_list_value_order('Dt. Confirmação', 'Datas', 'ª', False)
        self.create_keys_dict(['Lance', 'Desclassificados', 'Desclassificados_Fixo', 'Fixo', 'Qts_Sorteios'], 'Dt. Confirmação', 'Datas', 'Qts_Sorteios')
        self.join_key_list(['Lance', 'Desclassificados', 'Desclassificados_Fixo', 'Fixo', 'Qts_Sorteios'], 'Dt. Confirmação', 'Datas')
        self.del_dict_repetition_key_controle()
        self.del_key_from_dict(['Dt. Confirmação'])

        # juntar de lances, desclassifidados, desclassificado_fixo, fixo e dts_Confirmações com a mesma data de contemplação 
        self.create_key_controle([grupo, 'Modalidade'])
        self.create_key_list_value_order('Dt. Contemplação', 'Datas_cont_temp', 'ªct: ', True)
        self.create_keys_dict(['Lance', 'Desclassificados', 'Desclassificados_Fixo', 'Fixo', 'Qts_Sorteios', 'Datas'], 'Dt. Contemplação', 'Datas_cont_temp', '')
        self.join_key_list(['Lance', 'Desclassificados', 'Desclassificados_Fixo', 'Fixo', 'Qts_Sorteios', 'Datas'], 'Dt. Contemplação', 'Datas_cont_temp')
        self.del_dict_repetition_key_controle()
        self.del_key_from_dict(['Dt. Contemplação', 'Datas_cont_temp', 'Modalidade', key_controle])

        # criar duas colunas  com valor minimo e maximo do valor da carta de cada grupo 
        self.create_key_min_max_find_value(['Lance', 'Desclassificados', 'Desclassificados_Fixo', 'Fixo'], 'Valor_carta_min', 'Valor_carta_max')

        self.get_key_5_dict_prec_dif(['Lance'], 'months')
        self.anbalyze_consortium('months', 'prazo', 'realizadas')
        self.del_key_from_dict(['months'])

        # OBJETIVO 2: COM DICIONÁRIOS ÚNICOS DE CADA GRUPO DIMINUIR OS DICIONÁRIOS INTERNOS PARA ÚNICA LINHA
        # juntar as informaçoes do dicionário das datas de confirmações em modo texto alterando para intervalo em dias comparando com a contemplação        
        self.join_key_dict_date('Datas', 'dias')
        self.join_key_3_dict(['Qts_Sorteios'])
        self.join_key_5_dict_prec_fix(['Desclassificados_Fixo', 'Fixo'], '% -> ')
        self.join_key_5_dict_prec_dif(['Desclassificados', 'Lance'], '%')





        

        salve_arq(self.disc_newcon, path_newcon_json_tratado)


if __name__ == '__main__':
    import main