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
from xmlrpc.client import Boolean
# import re

# from dotenv import set_key
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from decimal import Decimal

# import import_firestore
from src.tempo import Tempo
from src.log import Log
from src.conexao import Conexao
# import pandas as pd
# from tratar import Tratar
from src.renomear import Renomear
from src.var import *
from src.chromeDriverauto  import ChromeDriverAuto
# from convert import Convert
from src.treat import Treat
from src.read_salve import Read_salve

from src.import_firestore import Import_firestore
from src.exceptions import BlockExecution

# from IPython.display import display

conexao = Conexao()
log = Log()
tempo = Tempo()
renomear = Renomear()
# tratar = Tratar()
chromeDriverAuto = ChromeDriverAuto()
# convert = Convert()
treat = Treat()
read_salve = Read_salve()
# import_firestore = Import_firestore()

datahora = tempo.tempo_arq()
path_all_log = p_log + arq_log + datahora + ext_Log

conexao.path_all_log = path_all_log
log.path_all_log = path_all_log
tempo.path_all_log = path_all_log


################################ Funct ######################################

# Pegar o tempo qeu foi chamado e escrever no log
def log_tempo_programa():
    write_log = time.strftime("%H:%M:%S") + '   ' + str(x)
    log.write_log = write_log
    log.escrever()

def salve_arq(write_file, path_file):
    read_salve.write_file = write_file
    read_salve.path_file = path_file
    read_salve.to_write()

def read_arq(path_file):
    read_salve.path_file = path_file
    return read_salve.to_read()

def join_disc_list_and_disc_info(disc_info, list_json):
    new_list_json = []
    for temp_json in list_json:
        new_json = copy.deepcopy(disc_info)
        for key, value in temp_json.items():
            new_json[key] = value
        new_list_json.append(new_json)
    return new_list_json  

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
        print(f'path_clickvenda_json : {path_clickvenda_json} """"""""""""""""""""')
        return globals()[info_clickvenda['read']](path_clickvenda_json)
    
class Newcon:
    def __init__(self, *args, **kwargs):
        self.driver = None
        self.list_info = []
        # self.dict_info = {}
        self.list_grupo = []
        self.count_loop_all = 0
        self.count_loop_single = 0
        self.count_bolock_execution = 0
        self.grupo_newcon = 0
        self.dict_newcon = []
        self.logar = True
        self.stop_error = False
        self.disc_get_newcon_start = {}
        self.disc_get_newcon = {}
        self.disc_grupo = {}
        self.list_dict_newcon_join = {}
        self.list_dict_running = []
    
    def loop_all(self):
        self.count_loop_all += 1
        if self.count_loop_all > 1:
            print(f'⚠️ MAIN: grupo {self.grupo_newcon}, nº de tentativa {self.count_loop_all}.')
        if self.count_loop_all >= 10:
            print(f"❌ MAIN: Loop do grupo: {self.grupo_newcon}, nº de tentativa {self.count_loop_all}, Proximo grupo...")
            raise BlockExecution("loop detectado")
        return False

    def loop_single(self, key) -> Boolean:
        self.count_loop_single += 1
        if self.count_loop_single > 1:
            print(f'⚠️  MAIN: processo {key}, do grupo: {self.grupo_newcon}, nº de tentativa {self.count_loop_single}.')
        if self.count_loop_single >= 3:
            print(f"❌ MAIN: Loop do processo {key}, do grupo: {self.grupo_newcon}, nº de tentativa {self.count_loop_single}º. Proximo processo...")
            self.disc_get_newcon[key] = False
            return True
        return False
    
    def loop_bolock_execution(self, e, key) -> None:
        self.stop_error = True
        self.count_bolock_execution += 1
        print(f"⚠️ MAIN: bolock: {e}, do processo {key}, do grupo: {self.grupo_newcon}, nº de tentativa {self.count_bolock_execution}.")
        if self.count_bolock_execution >= 3:
            print(f"❌ MAIN: Loop bolock: {e}, do processo {key}, do grupo: {self.grupo_newcon}, nº de tentativa {self.count_bolock_execution}. Proximo processo ou grupo...")
            self.disc_get_newcon_start[key] = False
            self.count_bolock_execution = 0

    def get_df_grupo(self, df) -> None:
        self.list_grupo = []
        for dict_df in df:
            self.list_grupo.append(dict_df['Grupo'])
        self.list_grupo = sorted(set(self.list_grupo))    

    def reset_var_1(self) -> None:
        self.logar = True
        self.dict_newcon = []

    def reset_var_2(self) -> Boolean:
        self.grupo_newcon = str(self.grupo_newcon)
        conexao.grupo_newcon = self.grupo_newcon
        g_newcon_int = int(self.grupo_newcon)
        renomear.inf = self.grupo_newcon
        if g_newcon_int < menor_g_newcon or g_newcon_int > maior_g_newcon or not renomear.vazio():
            return True
        self.stop_error = False
        self.disc_get_newcon_start = {
            info: True,
            conf: True, 
            canc: True,
            desc: True, 
            apur: False 
        }
        self.count_bolock_execution = 0
        return False

    def reset_var_3(self) -> None:
        self.count_loop_single = 0
        self.count_loop_all = 0
        self.disc_get_newcon = copy.deepcopy(self.disc_get_newcon_start)
        self.disc_grupo = {}

    def add_grupo_list(self) -> None:
        print(f'\n⛏️  MAIN: Início o grupo: {self.grupo_newcon}')
        if grupo not in self.disc_grupo:
            self.disc_grupo[grupo] = self.grupo_newcon

    def proc_stop_erro(self) -> None:
        self.driver.close()
        self.logar = True
        self.stop_error = False 

    def proc_logar(self) -> None:
        self.driver = chromeDriverAuto.open_site(info_newcon)
        conexao.driver = self.driver
        getattr(conexao, info_newcon['log'])(info_newcon, path_newcon)
        self.logar = False

    def reset_var_4(self, key) -> None:
        print(f'⛏️  MAIN: grupo: {self.grupo_newcon} tabela {key}')
        self.list_dict_newcon_join = {}
        self.list_dict_running = []

    def reset_var_5(self, key) -> None:
        self.count_loop_single = 0
        self.disc_get_newcon[key] = False

    # def add_values_sorteios(self, dict_sorteio_inf) -> None:
    #     if dict_sorteio_inf == {}:
    #         return
    #     for key_sorteio, value_sorteio in dict_sorteio_inf.items():
    #         renomear.inf = value_sorteio
    #         if ocorrencia in key_sorteio:
    #             column_key  = ocorrencia
    #             value_sorteio = renomear.get_num_string()
    #         elif dt_ex_assembleia in key_sorteio:
    #             column_key = dt_ex_assembleia
    #             value_sorteio = renomear.get_date_string()
    #         if column_key not in self.dict_sorteio:
    #             self.dict_sorteio[column_key] = [value_sorteio]
    #         elif value_sorteio not in self.dict_sorteio[column_key]:
    #             self.dict_sorteio[column_key].append(value_sorteio)


    def step_important(self, key) -> None:
        for _ in range(3):  # vai tentar 3 vezes 
            self.reset_var_5(key)
            conexao.percussion_cont_newcon() # precionar botões e digitar 
            self.list_dict_newcon_join = conexao.get_newcon(key)
            if not self.list_dict_newcon_join:  # se não existir discionário tentar novamente , menso se for apuracao
                if key == apur: 
                    break
                continue
            if key == info:  # se for informação fixa colocar no discionário disc grupo só um dicionario na lista
                self.disc_grupo.update(self.list_dict_newcon_join[0])
                break
            self.list_dict_running = join_disc_list_and_disc_info(self.disc_grupo, [disc_tabela_newcon[key]])
            self.list_dict_running = join_disc_list_and_disc_info(self.list_dict_running[0], self.list_dict_newcon_join)
            self.dict_newcon += self.list_dict_running
            break
        else:
            print(f'{disc_msn_newcon[key]} {self.grupo_newcon} e list_dict_newcon_join: {self.list_dict_newcon_join}')
            if key == info:
                self.stop_error = True
                # break  

    def have_disc_get_newxon(self) -> Boolean:
        for get_value in self.disc_get_newcon.values():
            if get_value:
                return True
        return False
        
    def control_remoto_newcon_full(self, df_clickvenda):
        if jump_newcon:
            return False
        self.reset_var_1()
        self.get_df_grupo(df_clickvenda)
        for self.grupo_newcon in self.list_grupo:
            if self.reset_var_2():
                continue
            while True:
                self.reset_var_3()
                try:
                    while True:
                        self.loop_all()
                        self.add_grupo_list()
                        if self.stop_error:
                            self.proc_stop_erro()
                        if self.logar:
                            self.proc_logar()
                        for key, get_value in self.disc_get_newcon.items():
                            if not get_value:
                                continue
                            self.reset_var_4(key)
                            if self.loop_single(key):
                                break
                            self.step_important(key)
                        if not self.have_disc_get_newxon():
                            break
                    break  
                except BlockExecution as e:
                    self.loop_bolock_execution(e, key or info)              
        chromeDriverAuto.close_driver(self.driver)
        # print(f'dict_sorteio: {}')
        salve_arq(self.dict_newcon, path_newcon_json)
        salve_arq(conexao.dict_sorteio, path_newcon_sorteio_json)
        return True

##################### TRATAR E JUNTAR DE TABELAS #############################
# INICIO DO PROGRAMA:
clickvenda = Clickvenda()
newcon = Newcon()

for x in range(1):
    log_tempo_programa()
    tpInicSegProg = tempo.tempo_execucao()
    df_clickvenda = clickvenda.control_remote_clickvenda() 
    newcon.control_remoto_newcon_full(df_clickvenda)
    treat.organizar_newcon_full()
    Import_firestore(path_newcon_tratado_json)
    sys.exit()
