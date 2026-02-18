# flake8: noqa
# pyright: reportCallIssue=false
# pyright: reportArgumentType=false
# pyright: # type: ignore

# # erro corrigido com comando:
# # python -m pip install webdriver-manager --upgrade
# # python -m pip install packaging

# from ast import Return
import copy
# from tarfile import DEFAULT_FORMAT
import time
# from datetime import datetime
import sys
# import json
from tkinter import N
# import re

# from dotenv import set_key
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from decimal import Decimal

from tempo import Tempo
from log import Log
from conexao import Conexao
# import pandas as pd
from tratar import Tratar
from renomear import Renomear
from var import *
from chromeDriverauto  import ChromeDriverAuto
from convert import Convert
from treat import Treat
from read_salve import Read_salve

# from IPython.display import display

conexao = Conexao()
log = Log()
tempo = Tempo()
renomear = Renomear()
tratar = Tratar()
chromeDriverAuto = ChromeDriverAuto()
convert = Convert()
treat = Treat()
read_salve = Read_salve()

datahora = tempo.tempo_arq()
path_all_log = p_log + arq_log + datahora + ext_Log

conexao.path_all_log = path_all_log
log.path_all_log = path_all_log
tempo.path_all_log = path_all_log

# # LER ARQUIVOS
# file_arq = p_df + arq_df + 'Select' + ext_CSV
# dfSelect = pd.read_csv(file_arq, sep=',', encoding='latin_1', dtype=str)

# file_arq = p_df + 'PRODUCAO' + ext_CSV
# dfSelect = pd.read_csv(file_arq, sep=',', encoding='latin_1', dtype=str)

################################ Funct ######################################

# Pegar o tempo qeu foi chamado e escrever no log
def log_tempo_programa():
    write_log = time.strftime("%H:%M:%S") + '   ' + str(x)
    log.write_log = write_log
    log.escrever()

# def gravar(df, arq):
#     conexao.df = df
#     conexao.file_arq = arq
#     conexao.gravar()

def salve_arq(write_file, folder_file):
    read_salve.write_file = write_file
    read_salve.folder_file = folder_file
    read_salve.to_write()

def read_arq(folder_file):
    read_salve.folder_file = folder_file
    return read_salve.to_read()

# def juntar(json_base, json_novo):
#     return json_base + (json_novo or [])

def join_disc_list_and_disc_info(disc_info, list_json):
    new_list_json = []
    for temp_json in list_json:
        new_json = copy.deepcopy(disc_info)
        # if isinstance(new_json, list):
        #     new_json = new_json[0]
        for key, value in temp_json.items():
            new_json[key] = value
        new_list_json.append(new_json)
    return new_list_json  

# def alterar_nome_coluna_gravar(df, arq):
#     # tratar = Tratar()
#     tratar.df = df
#     df = tratar.dfColunaALterarNome()
#     # df = Tratar(df=df).dfColunaALterarNome()
#     gravar(df, arq)
#     return df


# def alterar_dados_info_gravar(df, arq):
#     # tratar = Tratar()
#     tratar.df = df
#     tratar.coluna = 'Grupo'
#     df = tratar.dfColunaStrInt()
#     gravar(df, arq)
#     return df

# def criar_df_atravas_lista_info(list_table):
#     # criar df atraves da lista
#     df_newcon_info = pd.DataFrame()
#     tratar.df = df_newcon_info
#     df = tratar.dfColunaIndexNumeroLinha()
#     # df = Tratar(df=df).dfColunaIndexNumeroLinha()
#     colunas = ['Grupo', 'Prazo', 'Realizada', 'ARealizar', 'Prox_Assembleia', 'VencimentoNew']
#     for coluna in colunas:
#         tratar.df = df
#         tratar.coluna = coluna
#         df = tratar.dfColunaCriarVazia()
#         # df = Tratar(df=df, coluna=coluna).dfColunaCriarVazia()
#     numeroLinha = 0  # reutilizar variavel
#     for lista in list_table:
#         tratar.df = df
#         tratar.colunas = colunas
#         tratar.lista = lista
#         tratar.numeroLinha = numeroLinha
#         df = tratar.dfColunaLinhas()
#         # df = Tratar(df=df, colunas=colunas, lista=lista,
#         #             numeroLinha=numeroLinha).dfColunaLinhas()
#         numeroLinha += 1
#     gravar(df, arq_info)
#     return df

class Clickvenda:
    def __init__(self, *args, **kwargs):
        pass

    def control_remote_clickvenda(self):
        if not jump_clickvenda:
            for _ in range(5):
                conexao.driver = chromeDriverAuto.open_site(info_clickvenda)
                getattr(conexao, info_clickvenda['log'])(info_clickvenda, path_clickvenda)
                getattr(conexao, info_clickvenda['navegate_start'])()
                if getattr(conexao, info_clickvenda['navegate'])():
                    break
        return globals()[info_clickvenda['read']](path_clickvenda_json)
    
class Newcon:
    def __init__(self, *args, **kwargs):
        self.driver = None
        self.list_info = []
        self.disc_info = {}
        self.list_grupo = []
        self.count_loop_all = 0
        self.count_loop_single = 0
        self.grupo_newcon = 0
        self.disc_newcon = None
    
    def navegar_newcon_contemplacao_padrao(self):
        conexao.percussion_cont_newcon()  # navega até a df self.grupo_newcon

    def loop_all(self):
        self.count_loop_all += 1
        if self.count_loop_all > 1:
            print(f'⚠️ MAIN: loop all {self.count_loop_all}ª tentativa do grupo {self.grupo_newcon}, já foi.')
        if self.count_loop_all >= 10:
            print(f"❌ MAIN: O programa esta em um loop fatal, o grupo: {self.grupo_newcon}, foi atigido a quantidade {self.count_loop_all}ª.")
            print("❌ MAIN: Passar para o próximo grupo.")
            return True
        return False

    def loop_single(self):
        self.count_loop_single += 1
        if self.count_loop_single > 1:
            print(f'⚠️  MAIN: loop single {self.count_loop_single}ª tentativa do grupo {self.grupo_newcon}, já foi.')
        if self.count_loop_single >= 3:
            print(f"❌ MAIN: O programa esta em um loop fatal, o grupo: {self.grupo_newcon}, foi atigido a quantidade {self.count_loop_all}ª.")
            print("❌ MAIN: Passar para o próxima tabela do grupo ou proximo grupo")
            return True
        return False

    def control_remoto_newcon_full(self, df_clickvenda):
        if jump_newcon:
            return False
        logar = True
        self.disc_newcon = []
        conexao.df = df_clickvenda
        self.list_grupo = conexao.get_df_grupo()
        for self.grupo_newcon in self.list_grupo:
            self.grupo_newcon = str(self.grupo_newcon)
            g_newcon_int = int(self.grupo_newcon)
            renomear.inf = self.grupo_newcon
            if g_newcon_int <= menor_g_newcon or g_newcon_int >= maior_g_newcon or not renomear.vazio():
                continue
            self.count_loop_single = 0
            self.count_loop_all = 0
            conexao.grupo_newcon = self.grupo_newcon
            disc_get_newcon = {
                info: True,
                conf: True, 
                canc: True,
                desc: True, 
                apur: True 
            }
            stop_error = False
            disc_grupo = {}
            while True:
                print(f'\n⛏️  MAIN: Início o grupo: {self.grupo_newcon}')
                if grupo not in disc_grupo:
                    disc_grupo[grupo] = self.grupo_newcon
                if stop_error:
                    self.driver.close()
                    if self.loop_all():
                        logar = True
                        stop_error = False
                    else:
                        break  
                if logar:
                    self.driver = chromeDriverAuto.open_site(info_newcon)
                    conexao.driver = self.driver
                    getattr(conexao, info_newcon['log'])(info_newcon, path_newcon)
                    logar = False
                
                for key, get_value in disc_get_newcon.items():
                    if not get_value:
                        continue
                    print(f'⛏️  MAIN: grupo: {self.grupo_newcon} tabela {key}')
                    disc_newcon_join = {}
                    list_dict_running = []
                    if self.loop_single():
                        disc_get_newcon[key] = False
                        break
                    else:
                        for _ in range(3):
                            conexao.percussion_cont_newcon() 
                            disc_newcon_join = conexao.get_newcon(key)
                            if not disc_newcon_join:
                                if key == apur:
                                    self.count_loop_single = 0
                                    disc_get_newcon[key] = False
                                    break
                                continue
                            if key == info:
                                disc_grupo.update(disc_newcon_join)
                            else: 
                                list_dict_running = join_disc_list_and_disc_info(disc_grupo, [disc_tabela_newcon[key]])
                                list_dict_running = join_disc_list_and_disc_info(list_dict_running[0], disc_newcon_join)
                                self.disc_newcon += list_dict_running
                            self.count_loop_single = 0
                            disc_get_newcon[key] = False
                            break
                        else:
                            print(disc_msn_newcon[key], self.grupo_newcon)
                            if key == info:
                                stop_error = True
                                break                 
                out_while = True
                for key, get_value in disc_get_newcon.items():
                    if get_value:
                        out_while = False
                        break
                if out_while:
                    break        
        chromeDriverAuto.close_driver(self.driver)
        conexao.salve_arq(self.disc_newcon, path_newcon_json)
        return True

   

##################### TRATAR E JUNTAR DE TABELAS #############################

# def tratar_gravar(df, arq, ap):
#     conexao.ap = ap
#     conexao.df = df
#     df = conexao.tratarDf_newcon()
#     gravar(df, arq)
#     return df

# def editar_dados_360(df, df_newcon_info):
#     df360New = pd.DataFrame()
#     conexao.df = df360New
#     conexao.df360 = df
#     conexao.df_newcon_info = df_newcon_info
#     df = conexao.gravarDf360()
#     return df

# INICIO DO PROGRAMA:

clickvenda = Clickvenda()
newcon = Newcon()

for x in range(1):
    log_tempo_programa()
    tpInicSegProg = tempo.tempo_execucao()
    df_clickvenda = clickvenda.control_remote_clickvenda() 
    newcon.control_remoto_newcon_full(df_clickvenda)
    treat.organizar_newcon_full()
    sys.exit()


    # conexao.df = df
    # conexao.listaGrupo360 = listaGrupo360
    # df = conexao.dfMesclaOrganizar()

    # df2 = df
    # df = pd.merge(df, df_newcon_info, on='Grupo')

    # tratar.df = df
    # df = tratar.dfColunaOrganizar()

    # conexao.ext_ = ext_Xlsx
    # gravar(df, arq_df_xlsx)

    # gravar(df, arq_df_csv)

    # conexao.df = df2
    # df = conexao.tratarDfFixar()
    # df = pd.merge(df, df_newcon_info, on='Grupo')
    # tratar.df = df
    # df = tratar.dfColunaOrganizar()

    # conexao.ext_ = ext_Xlsx
    # gravar(df, arq_df_2_xlsx)

    # gravar(df, arq_df_2_csv)

    # ###########################
    # write_log = 'fim'  # informação do log
    # tempo.tpInicSeg = tpInicSegProg
    # tempo.tpInicSegProg = tpInicSegProg
    # tempo.write_log = write_log
    # tempo.tempo_execucao()
    # # Tempo(tpInicSeg=tpInicSegProg, tpInicSegProg=tpInicSegProg, write_log=write_log).tempo_execucao()  # noqa
    # write_log = time.strftime("%H:%M:%S")
    # log.write_log = write_log
    # log.escrever()
