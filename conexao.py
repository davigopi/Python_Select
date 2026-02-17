# flake8: noqa
# pyright: # type: ignore
# pyright: # noqa
# pyright: reportOptionalSubscript=false
# pyright: reportArgumentType=false
# pyright: reportOptionalIterable=false
# pyright: reportOptionalCall=false
# pyright: reportCallIssue=false
# pyright: reportOptionalMemberAccess=false
# pyright: reportAttributeAccessIssue=false
# pyright: reportAttributeAccessIssue=false

# # Para executar o if __name__ == '__main__':
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# from re import I
# from socket import EAI_SERVICE

from var import *
from log import Log
from read_salve import Read_salve
from funct import Funct
from dfSite import DfSite
from tarefa import Tarefa
from botao import Botao
from tratar import Tratar
from convert import Convert


import pandas as pd
import os
import sys
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import json

import pyautogui


log = Log()
read_salve = Read_salve()
convert = Convert()

def wait_and_exit(msn):
    print(msn)
    time.sleep(120)
    sys.exit()

class Conexao:
    def __init__(self, *args, **kwargs):
        self.driver = kwargs.get('driver')
        self.user = kwargs.get('user')
        self.password = kwargs.get('password')
        self.path_all_log = kwargs.get('path_all_log')
        self.tpInicSegProg = kwargs.get('tpInicSegProg')
        self.html1Anterior = kwargs.get('html1Anterior')
        self.html2Anterior = kwargs.get('html2Anterior')
        self.ultNIndex360 = kwargs.get('ultNIndex360')
        self.ultNIndex1 = kwargs.get('ultNIndex1')
        self.ultNIndex2 = kwargs.get('ultNIndex2')
        self.ultNIndex3 = kwargs.get('ultNIndex3')
        self.ultNIndex4 = kwargs.get('ultNIndex4')
        self.ap = kwargs.get('ap')
        self.grupo_newcon = kwargs.get('grupo_newcon')
        self.df = kwargs.get('df')
        self.df2 = kwargs.get('df2')
        self.df_newcon = kwargs.get('df_newcon')
        self.df360 = kwargs.get('df360')
        self.df_newcon_info = kwargs.get('df_newcon_info')
        self.nUrl = kwargs.get('nUrl')
        self.pastaArquivo = kwargs.get('pastaArquivo')
        self.extencao = kwargs.get('extencao')
        self.listaGrupo360 = kwargs.get('listaGrupo360')
        self.tempo = 1
        # self.plano = {}
        # self.marca = {}
        self.plano_marca = {}

        # self.retornar = True
        
        log.path_all_log = self.path_all_log

        self.funct = Funct(driver = self.driver, path_all_log = self.path_all_log)
        

    def zerar_variaveis(self):
        self.extencao = None

    def salve_arq(self, write_file, folder_file):
        read_salve.write_file = write_file
        read_salve.folder_file = folder_file
        read_salve.to_write()

    def read_arq(self, folder_file):
        read_salve.folder_file = folder_file
        return read_salve.to_read()

    def func_key(self, path, keyboard):
        self.funct.path = path
        self.funct.digitar = keyboard
        self.funct.faz = 'keys'
        return self.funct.funct()
    
    def func_click(self, path):
        self.funct.path = path
        return self.funct.funct()

    def func_get_select(self, path, tag=''):
        self.funct.path = path
        self.funct.tag = tag
        self.funct.faz = 'get_select'
        return self.funct.funct()
    
    def func_select_value(self, path, value):
        self.funct.path = path
        self.funct.value = value
        self.funct.faz = 'select_value'
        return self.funct.funct()
    
    def func_checkbox(self, path):
        self.funct.path = path
        self.funct.faz = 'checkbox'
        if self.funct.funct():
            return self.funct.dados
        return False
    
    def func_wait_df_or_empty(self, path):
        self.funct.path = path
        self.funct.faz = 'wait_df_or_empty'
        return self.funct.funct() 
    
    def func_key_single(self, path, key_single, quantity):
        for _ in range(quantity):
            self.funct.path = path
            self.funct.key_single = key_single
            self.funct.faz = 'key_single'
            self.funct.funct()
        return

    # clickvenda:
    # clickvenda segundo nivel:
    def treat_dados(self, dados, tag1):
        # print(f'dados: {dados}')
        dict_dados = []
        # Como dados é BeautifulSoup: <select>
        options = dados.find_all(tag1)
        for option in options:
            value = option.get(tag_value)
            if value and value.strip():
                dict_dados.append({
                    tag_value: value.strip(),
                    tag_text: option.text.strip()
                })
        # print(f'dict_dados: {dict_dados}')
        return dict_dados


    # def treat_dados(self, dados):
    #     print(f'dados: {dados}')
    #     options = dados.find_all(tag_option)
    #     dict_dados = []
    #     for dado in options:
    #         print(dado)
    #         value = dado.get_attribute(tag_value)
    #         if value:
    #             dict_dados.append({
    #                 tag_value: value,
    #                 tag_text: dado.text.strip()
    #             })
    #     print(f'dict_dados:{ dict_dados}')
    #     # dict_dados = [
    #     #     {
    #     #         tag_value: dado.get_attribute(tag_value),
    #     #         tag_text: dado.text.strip()
    #     #     }
    #     #     for dado in dados
    #     #     if dado.get_attribute(tag_value)
    #     # ]
    #     return dict_dados
    
    def click_get_select(self, path, tag):
        self.func_click(path_clickvenda[path])
        return self.func_get_select(path_clickvenda[path], tag)

    def marked_checkbox(self):
        if self.func_checkbox(path_clickvenda['credito_referenciado'])  == 'OK':
            self.func_click(path_clickvenda['credito_referenciado'])    

    # clickvenda primeiro nivel:
    def log_site(self, info_site, path_site):
        self.funct.driver = self.driver
        self.funct.path_all_log = self.path_all_log
        if 'loading' in path_site:
            self.funct.path_loading = path_site['loading']
        if 'modal' in path_site and 'modal_btn' in path_site:
            self.funct.path_modal = path_site['modal']
            self.funct.path_modal_btn = path_site['modal_btn']
        self.func_key(path_site['user'], info_site['user'])
        self.func_key(path_site['password'], info_site['password'])
        self.func_click(path_site['btn_open'])

    def navegate_start_clickvend(self):
        self.func_click(path_clickvenda['btn_nova_venda'])
        self.func_click(path_clickvenda['btn_automovel'])
        self.func_click(path_clickvenda['btn_selecionar'])
        self.func_click(path_clickvenda['btn_parcela'])
        self.func_click(path_clickvenda['id_divPasso1'])
        self.func_key_single(path_clickvenda['id_divPasso1'], Keys.PAGE_UP, 5)

    def navegate_clickvend(self):
        rows = []
        planos = self.treat_dados(self.click_get_select('busca_andamento_plano', tag_option), tag_option)
        for plano in planos:
            # print(plano)
            # if 'PLANO 100%  36M TX 16' not in plano['text']:
            #     continue
            # print(f'plano: {plano}')
            if not plano[tag_value]:
                continue
            self.func_select_value(path_clickvenda['busca_andamento_plano'], plano[tag_value])
            self.marked_checkbox()
            marcas = self.treat_dados(self.click_get_select('busca_andamento_modelo', tag_option), tag_option)
            for marca in marcas:
                # print(f'marca: {marca}')
                # if 'CRED REF 990009 - 78.000,00' not in marca["text"]:
                #     continue
                # time.sleep(100)
                if not marca[tag_value]:
                    continue
                self.func_select_value(path_clickvenda['busca_andamento_modelo'], marca[tag_value])
                self.func_click(path_clickvenda['btn_buscar'])
                self.func_wait_df_or_empty(path_clickvenda['id_divPasso21'])
                convert.table = self.func_get_select(path_clickvenda['id_divPasso21_table'], tag_table)
                list_row = convert.table_list_in_disc()
                new_row = []
                for row in list_row:
                    row['Plano'] = plano[tag_text]
                    row['Marca'] = marca[tag_text]
                    new_row. append(row)
                rows += new_row
            # break
        self.salve_arq(rows, path_clickvenda_json)
        return True

    # newcom 


    # clickvenda primeiro nivel:
    def get_df_grupo(self):
        list_grupo = []
        for dict_df in self.df:
            list_grupo.append(dict_df['Grupo'])
        list_grupo = sorted(set(list_grupo))    
        return list_grupo
    
    def percussion_cont_newcon(self):
        # self.funct.driver = self.driver
        # self.funct.path_all_log = self.path_all_log
        self.func_click(path_newcon['id_CP'])  # contemplacao
        self.func_click(path_newcon['id_subs'] )  # contemplacao
        self.func_click(path_newcon['id_ctl00_Conteudo_ctl00_tvwMenut1'])  # Resultado de Assembleia
        self.func_key(path_newcon['id_ctl00_Conteudo_edtCD_Grupo'], self.grupo_newcon)  # campo grupo
        self.func_click(path_newcon['id_ctl00_Conteudo_btnOK'])  # botao confirmar


    # def get_info_newcon(self):
    #     disc_info = {}
    #     for key, info in disc_path_info.items():
    #         disc_info[key] = self.func_get_select(path_newcon[info], tag_text)
    #     return disc_info



    def get_newcon(self, table_newcon):
        if table_newcon == info:
            disc_info = {}
            for key, inf in disc_path_info.items():
                disc_info[key] = self.func_get_select(path_newcon[inf], tag_text)
            return disc_info

        disc_all = []
        if table_newcon == apur:
            number_times = 1
        else:
            number_times = mesQuantidade
        for _ in range(number_times):
            if table_click_newcon[table_newcon]:
                self.funct.time_total_set = 3
                if not self.func_click(path_newcon[table_click_newcon[table_newcon]]):
                    break 
            for _ in range(10):
                convert.table = self.func_get_select(path_newcon[table_get_newcon[table_newcon]], tag_table)
                disc_new = convert.table_list_in_disc()
                if disc_new in disc_all:
                    time.sleep(0.5)
                    continue
                break
            else:
                wait_and_exit('A tabela anterior é a mesma da posterior. programa sera fechado em 2 minutos.')
            disc_all += disc_new
            self.func_click(path_newcon['id_ctl00_Conteudo_btnRetornaAssembleia'])
        return disc_all
    

    # def get_conf_newcon(self):
    #     # self.funct = Funct()
    #     # self.funct.driver = self.driver
    #     # self.funct.path_all_log = self.path_all_log
    #     disc_all = []
    #     for _ in range(mesQuantidade):
    #         convert.table = self.func_get_select(path_newcon['id_ctl00_Conteudo_div_Confirmadas'], tag_table)
    #         disc_all += convert.table_list_in_disc()
    #         self.func_click(path_newcon['id_ctl00_Conteudo_btnRetornaAssembleia'])
    #     return disc_all

    # def get_canc_newcon(self):
    #     # self.funct = Funct()
    #     # self.funct.driver = self.driver
    #     # self.funct.path_all_log = self.path_all_log
    #     disc_all = []
    #     for _ in range(mesQuantidade):
    #         self.func_click(path_newcon['id_ui_id_8'])    
    #         convert.table = self.func_get_select(path_newcon['id_ctl00_Conteudo_grdContemplacoes_Confirmadas_Canceladas'], tag_table)
    #         disc_all += convert.table_list_in_disc()
    #         self.func_click(path_newcon['id_ctl00_Conteudo_btnRetornaAssembleia'])
    #     return disc_all

    # def get_desc_newcon(self):
    #     # self.funct = Funct()
    #     # self.funct.driver = self.driver
    #     # self.funct.path_all_log = self.path_all_log
    #     disc_all = []
    #     for _ in range(mesQuantidade):
    #         self.func_click(path_newcon['id_ui_id_9'])
    #         convert.table = self.func_get_select(path_newcon['id_ctl00_Conteudo_div_Desclassificadas'], tag_table)
    #         disc_all += convert.table_list_in_disc()
    #         self.func_click(path_newcon['id_ctl00_Conteudo_btnRetornaAssembleia'])
    #     return disc_all
        
    # def get_apur_newcon(self):
    #     # self.funct = Funct()
    #     # self.funct.driver = self.driver
    #     # self.funct.path_all_log = self.path_all_log
    #     self.funct.time_total_set = 3
    #     disc_all = []
    #     for _ in range(mesQuantidade):
    #         if not self.func_click(path_newcon['id_ctl00_Conteudo_btnCotasSorteadas']):
    #             break
    #         print(f'⁉️  CONEXAO: O grupo {self.grupo_newcon} tem apuração')
    #         time.sleep(99)   
    #         convert.table = self.func_get_select(path_newcon['id_ctl00_Conteudo_grdContemplacoes_Confirmadas_Canceladas'], tag_table)
    #         disc_all += convert.table_list_in_disc()
    #         self.func_click(path_newcon['id_ctl00_Conteudo_btnRetornaAssembleia'])
    #     return disc_all
    
        # print('3')
        # tarefa = self.padrao_escolha_df()
        # # tarefa = Tarefa()
        # # tarefa.driver = self.driver
        # # tarefa.path_all_log = self.path_all_log
        # print('4')
        # tarefa.xpath_present_secreen = '//*[@id="divLoading"]/img'
        # tarefa.url = '//*[@id="ctl00_Conteudo_grdCotasSequenciaLance"]'  # df
        # # tarefa.ultCel1 = 0  # necessario para saber se df atualizou
        # # tarefa.ultCel2 = 0  # necessario para saber se df atualizou
        # # tarefa.colCel1 = 1  # coluna dois para teste
        # # tarefa.colCel2 = -1  # coluna ultima para teste
        # # tarefa.indTx1 = 'Grupo'
        # # tarefa.tag1 = 'table'
        # # tarefa.tag2 = 'tr'
        # # tarefa.tag3 = 'td'
        # # tarefa.tagCab = 'th'
        # tarefa.tempo = 5
        # tarefa.ultNIndex = self.ultNIndex3
        # tarefa.fator_repeticao = 3
        # # tarefa.tpInicSegProg = self.tpInicSegProg
        # # tarefa.grupo_newcon = self.grupo_newcon
        # htmlNew, ultNIndex, ultCel1, ultCel2 = tarefa.df_newcon()
        # # print('PARA 1000 $$$$$$$$$$$$$$$$$$$$$$$$$$')
        # # time.sleep(1000)
        # # htmlNew, ultNIndex, ultCel1, ultCel2 = Tarefa(
        # #     driver=self.driver, url=url, path_all_log=self.path_all_log, ultNIndex=ultNIndex,
        # #     tpInicSegProg=self.tpInicSegProg, grupo_newcon=self.grupo_newcon, tempo=tempo, ultCel1=ultCel1,
        # #     ultCel2=ultCel2, colCel1=colCel1, colCel2=colCel2, indTx1=indTx1, tag1=tag1, tag2=tag2,
        # #     tag3=tag3, tagCab=tagCab).df_newcon()
        # return htmlNew, ultNIndex


    # newcon:
    # newcon primeiro nível
    # def get_info_newcon(self):
    #     # lista = []
    #     # tarefa = Tarefa()
    #     # tarefa.driver = self.driver
    #     # tarefa.path_all_log = self.path_all_log
    #     # tarefa.grupo_newcon = self.grupo_newcon
    #     # tarefa.xpath_present_secreen = '//*[@id="divLoading"]/img'
    #     disc_info = {}
    #     for key, info in disc_path_info.items():
    #         disc_info[key] = self.func_get_select(path_newcon[info], tag_text)
    #     # print(disc_info)
            

    #     # convert.table = self.func_get_select(path_newcon['id_ctl00_Conteudo_grdContemplacoes_Confirmadas'], tag_table, '')
    #     # list_row = convert.table_html_in_disc()
    #     # self.func_click(path_newcon['id_ui_id_8'])
    #     # time.sleep(6)
    #     # convert.table = self.func_get_select(path_newcon['id_ctl00_Conteudo_grdContemplacoes_Confirmadas_Canceladas'], tag_table, '')
    #     # list_row = convert.table_html_in_disc()
    #     # time.sleep(66)
    #     return disc_info
    #     tarefa.url = '//*[@id="ctl00_Conteudo_lblCD_Grupo"]'  # grupo
    #     inf = tarefa.infoHTML()
    #     if inf == 'ERROR':
    #         return 'ERROR'

    #         # inf = Tarefa(
    #         #     driver=self.driver,
    #         #     grupo_newcon=self.grupo_newcon,
    #         #     path_all_log=self.path_all_log,
    #         #     url=url).infoHTML()
    #     lista.append(inf)
    #     print('2')
    #     tarefa.url = '//*[@id="ctl00_Conteudo_lblPZ_Comercializacao"]'
    #     inf = tarefa.infoHTML()
    #     if inf == 'ERROR':
    #         return 'ERROR'
    #     # inf = Tarefa(
    #     #     driver=self.driver,
    #     #     grupo_newcon=self.grupo_newcon,
    #     #     path_all_log=self.path_all_log,
    #     #     url=url).infoHTML()
    #     lista.append(inf)
    #     print('3')
    #     tarefa.url = '//*[@id="ctl00_Conteudo_lblQT_Assembleia_Realizada"]'
    #     inf = tarefa.infoHTML()
    #     if inf == 'ERROR':
    #         return 'ERROR'
    #     # inf = Tarefa(
    #     #     driver=self.driver,
    #     #     grupo_newcon=self.grupo_newcon,
    #     #     path_all_log=self.path_all_log,
    #     #     url=url).infoHTML()
    #     lista.append(inf)
    #     print('4')
    #     tarefa.url = '//*[@id="ctl00_Conteudo_lblQT_Assembleia_ARealizar"]'
    #     inf = tarefa.infoHTML()
    #     if inf == 'ERROR':
    #         return 'ERROR'
    #     # inf = Tarefa(
    #     #     driver=self.driver,
    #     #     grupo_newcon=self.grupo_newcon,
    #     #     path_all_log=self.path_all_log,
    #     #     url=url).infoHTML()
    #     lista.append(inf)
    #     print('5')
    #     tarefa.url = '//*[@id="ctl00_Conteudo_lblDT_Prox_Assembleia"]'
    #     inf = tarefa.infoHTML()
    #     if inf == 'ERROR':
    #         return 'ERROR'
    #     # inf = Tarefa(
    #     #     driver=self.driver,
    #     #     grupo_newcon=self.grupo_newcon,
    #     #     path_all_log=self.path_all_log,
    #     #     url=url).infoHTML()
    #     lista.append(inf)
    #     print('6')
    #     tarefa.url = '//*[@id="ctl00_Conteudo_lblDT_Prox_Vencimento"]'
    #     inf = tarefa.infoHTML()
    #     if inf == 'ERROR':
    #         return 'ERROR'
    #     # inf = Tarefa(
    #     #     driver=self.driver,
    #     #     grupo_newcon=self.grupo_newcon,
    #     #     path_all_log=self.path_all_log,
    #     #     url=url).infoHTML()
    #     lista.append(inf)
    #     return lista





    # antigos: 





class Antiga:
    def __init__(self, *args, **kwargs):
        self.driver = kwargs.get('driver')


    def logar360(self):
        funct = Funct()
        funct.driver = self.driver
        # funct.retornar = True
        funct.path_all_log = self.path_all_log
        while True:
            funct.urls = ['//*[@id="CPF"]']
            funct.faz = 'keys'
            funct.digitar = self.user
            retorno = funct.funct()
            if retorno:
                break
            else:  # sua conexao não é particular
                funct.urls = ['//*[@id="details-button"]']
                retorno = funct().funct()
                if retorno:
                    funct.urls = ['//*[@id="proceed-link"]']
                    retorno = funct().funct()
                    if retorno:
                        funct.urls = ['//*[@id="CPF"]']
                        funct.faz = 'keys'
                        retorno = funct().funct()
            if retorno is False:
                # log = Log()
                # log.path_all_log = self.path_all_log
                write_log = 'ERRO CONEXAO LOGAR: SUA CONEXAO NÃO É PARTICULAR'
                log.write_log = write_log
                log.escrever()
                sys.exit()
        funct.urls = ['//*[@id="Senha"]']
        funct.faz = 'keys'
        funct.digitar = self.password
        funct.funct()
        funct.urls = ['//*[@id="btn-entrar"]']
        funct.funct()

    def navegar360(self):
        funct = Funct()
        funct.driver = self.driver
        funct.path_all_log = self.path_all_log
        funct.urls = ['//*[@id="btn-confirmar-aviso"]']
        funct.funct()
        funct.tempo = 120
        funct.urls = ['/html/body/div[4]/div/div/div/div/div/div/div/div[1]/a']
        funct.funct()
        funct.urls = ['//*[@id="conteudo"]/div[1]/a[2]']
        funct.funct()
        funct.urls = ['//*[@id="divPasso1"]/div/div[1]/div/label[2]/div']
        funct.faz = 'locate'
        funct.funct()  # localiza
        funct.funct()  # preciona
        funct.urls = ['//*[@id="divPasso1"]/div/div[2]/div/div[1]/div/input']
        funct.faz = 'locate'
        funct.funct()  # localiza
        funct.funct()  # preciona
        funct.faz = 'keys'
        funct.digitar = Keys.PAGE_UP
        funct.repetir = 5
        # funct.retornar = True
        navegou = funct.funct()  # digitar
        return navegou

    def escolherDf360(self):
        ultCel1 = 0  # necessario para saber se df atualizou
        ultCel2 = 0  # necessario para saber se df atualizou
        dfConst = pd.DataFrame()

        # Plano
        funct = Funct()
        funct.driver = self.driver
        funct.path_all_log = self.path_all_log
        funct.urls = ['//*[@id="busca_andamento_plano"]']
        funct.tempo = 120
        funct.funct()
        # Funct(driver=self.driver, urls=[url], tempo=tempo, path_all_log=self.path_all_log).funct()
        print('######################## informar inicio #############################')
        funct.faz = 'inform'
        funct.tag1 = 'select'
        funct.tag2 = tag_option
        html = funct.funct()
        print('######################## informar fim #############################')
        # html = Funct(driver=self.driver, urls=[url], faz=faz, tag1=tag1, path_all_log=self.path_all_log).funct()
        dfsite = DfSite()
        dfsite.html = html
        dfsite.tag1 = 'select'
        dfsite.tag2 = tag_option
        html1 = dfsite.df()
        # html1 = DfSite(html=html, tag1=tag1, tag2=tag2).df()
        if html1 == 'ERROR':
            return False, self.html1Anterior, self.html2Anterior, self.ultNIndex360, 'ERROR'
        for planoOk in self.html1Anterior:
            try:
                html1.remove(planoOk)
            except ValueError:
                print(f'CONEXAO OBS: O item não existe mais na lista planoOk: {planoOk}')
                pass
        texto1 = html1[0]
        tarefa = Tarefa()
        tarefa.driver = self.driver
        tarefa.tpInicSegProg = self.tpInicSegProg
        tarefa.path_all_log = self.path_all_log
        tarefa.tag1 = 'select'
        tarefa.tag2 = tag_option
        tarefa.url = '//*[@id="busca_andamento_marca"]'
        tarefa.texto = texto1
        html2 = tarefa.tasks_repeat_360()
        # html2 = Tarefa(
        #     driver=self.driver,
        #     tpInicSegProg=self.tpInicSegProg,
        #     path_all_log=self.path_all_log,
        #     url=url,
        #     texto=texto1,
        #     tag1=tag1,
        #     tag2=tag2).tasks_repeat_360()
        for marcaOk in self.html2Anterior:
            try:
                html2.remove(marcaOk)
            except ValueError:
                print(f'CONEXAO OBS:o item nao existe mais na lista planoOk {marcaOk}')
                pass

        for indexMarca in range(4):
            try:  # não existe mas nada na lista
                texto2 = html2[indexMarca]
            except IndexError:
                indexMarca -= 1
                break
            self.html2Anterior.append(texto2)
            tarefa.tag1 = 'select'
            tarefa.tag2 = tag_option
            tarefa.url = '//*[@id="busca_andamento_modelo"]'
            tarefa.texto = texto2
            html3 = tarefa.tasks_repeat_360()
            # html3 = Tarefa(
            #     driver=self.driver,
            #     tpInicSegProg=self.tpInicSegProg,
            #     path_all_log=self.path_all_log,
            #     url=url,
            #     texto=texto2,
            #     tag1=tag1,
            #     tag2=tag2).tasks_repeat_360()
            for texto3 in html3:
                botao = Botao()
                botao.driver = self.driver
                botao.path_all_log = self.path_all_log
                botao.texto = texto3
                botao.url = '//*[@id="busca_andamento_modelo"]'
                botao.botao1()
                # Botao(driver=self.driver, path_all_log=self.path_all_log, texto=texto3, url=url).botao1()
                tarefa.url = '//*[@id="conteudo"]'
                tarefa.texto1 = texto1
                tarefa.texto2 = texto2
                tarefa.texto3 = texto3
                tarefa.indTx1 = 'Plano'
                tarefa.indTx2 = 'Marca'
                tarefa.indTx3 = 'Modelo'
                tarefa.indTx4 = 'Valor do Bem'
                tarefa.ultCel1 = ultCel1
                tarefa.ultCel2 = ultCel2
                tarefa.colCel1 = 1
                tarefa.colCel2 = -1
                tarefa.tratarModelo = True
                tarefa.tag1 = 'table'
                tarefa.tag2 = 'tr'
                tarefa.tag3 = 'td'
                tarefa.tagCab = 'th'
                tarefa.tempo = 10
                tarefa.ultNIndex = self.ultNIndex360
                htmlNew, ultNIndex, ultCel1, ultCel2 = tarefa.df_newcon()
                # htmlNew, ultNIndex, ultCel1, ultCel2 = Tarefa(
                #     driver=self.driver, path_all_log=self.path_all_log, tpInicSegProg=self.tpInicSegProg,
                #     ultNIndex=ultNIndex, url=url, texto1=texto1, texto2=texto2, texto3=texto3,
                #     indTx1=indTx1, indTx2=indTx2, indTx3=indTx3, indTx4=indTx4, ultCel1=ultCel1,
                #     ultCel2=ultCel2, colCel1=colCel1, colCel2=colCel2, tratarModelo=tratarModelo,
                #     tag1=tag1, tag2=tag2, tag3=tag3, tagCab=tagCab).df_newcon()
                if isinstance(htmlNew, pd.DataFrame):
                    dfConst = pd.concat([dfConst, htmlNew])
                elif htmlNew == 'ERROR':
                    return False, self.html1Anterior, self.html2Anterior, self.ultNIndex360, 'ERROR'

        if texto1 == html1[-1]:
            ultimoPlano = True
        else:
            ultimoPlano = False
        if html2 != []:
            if html2[indexMarca] == html2[-1]:
                self.html2Anterior = []
                self.html1Anterior.append(texto1)
        else:
            print('CONEXAO OBS: Sem info na Marca, ou seja, não existe df.')
            self.html1Anterior.append(texto1)
            return ultimoPlano, self.html1Anterior, self.html2Anterior, self.ultNIndex360, False
        try:
            print(f'CONEXAO OBS:##############texto1##############{texto1}##############')
            print(f'CONEXAO OBS:##############dfConst##############{dfConst}##############')
            return ultimoPlano, self.html1Anterior, self.html2Anterior, ultNIndex, dfConst
        except ValueError as e:
            write_log = 'CONEXAO OBS: Escolher DF em construacao não existir, '
            write_log += f'pois nao existem dfs: {e.__class__.__name__}'
            log.write_log = write_log
            log.escrever()
            # Log(path_all_log=self.path_all_log, write_log=write_log).escrever()
            print('CONEXAO OBS:@@@@@@@@@@@@@@@@dfConst@@@@@@@@@@@@@@@@@@@@False@@@@@@@@@@@@@@@')
            return ultimoPlano, self.html1Anterior, self.html2Anterior, ultNIndex, False
        # salvar arq

    def logarNewcon(self):
        funct = Funct()
        funct.driver = self.driver
        funct.path_all_log = self.path_all_log

        funct.digitar = self.user
        funct.faz = 'keys'
        funct.urls = ['//*[@id="edtUsuario"]']
        funct.funct()
        # url = '//*[@id="edtUsuario"]'
        # faz = 'keys'
        # Funct(
        #     driver=self.driver,
        #     digitar=self.usuario,
        #     path_all_log=self.path_all_log,
        #     urls=[url],
        #     faz=faz).funct()

        funct.digitar = self.password
        funct.faz = 'keys'
        funct.urls = ['//*[@id="edtSenha"]']
        funct.funct()

        # url = '//*[@id="edtSenha"]'
        # faz = 'keys'
        # Funct(driver=self.driver, digitar=self.password, path_all_log=self.path_all_log, urls=[url], faz=faz).funct()

        funct.urls = ['//*[@id="btnLogin"]']
        funct.funct()
        # url = '//*[@id="btnLogin"]'
        # Funct(driver=self.driver, path_all_log=self.path_all_log, urls=[url]).funct()



    def navegar_newcon_retorna_assembleia(self):
        funct = Funct()
        funct.driver = self.driver
        funct.path_all_log = self.path_all_log
        funct.urls = ['//*[@id="ui-id-6"]']  # Confirmadas aba
        funct.funct()
        # Funct(driver=self.driver, path_all_log=self.path_all_log, urls=[url]).funct()

        # botao assembeia
        funct.urls = ['//*[@id="ctl00_Conteudo_btnRetornaAssembleia"]']
        funct.funct()
        # Funct(driver=self.driver, path_all_log=self.path_all_log, urls=[url]).funct()

    def navegar_newcon_desc(self):
        print('1')
        funct = Funct()
        funct.driver = self.driver
        funct.path_all_log = self.path_all_log
        funct.tempo = 3
        funct.urls = ['//*[@id="ui-id-8"]']  # desc aba
        funct.funct()
        print('2')
        # botao desc
        funct.urls = ['//*[@id="ctl00_Conteudo_tabDesclassificadas"]']
        funct.funct()
        # Funct(driver=self.driver, path_all_log=self.path_all_log, urls=[url]).funct()

    def navegar_newcon_sequencia_apur(self):
        # url = '//*[@id="ctl00_Conteudo_btnCotasSorteadas"]'
        print('1')
        funct = Funct()
        funct.xpath_present_secreen = '//*[@id="divLoading"]/img'
        # Botao -> Sequência de Apuração
        funct.urls = ['//*[@id="ctl00_Conteudo_btnCotasSorteadas"]']
        funct.driver = self.driver
        funct.path_all_log = self.path_all_log
        # funct.retornar = True
        funct.funct()
        # Funct(driver=self.driver, path_all_log=self.path_all_log, urls=[url]).funct()
        try:
            print('2')
            funct.xpath_present_secreen = '//*[@id="divLoading"]/img'
            # Botão -> Sequência de Lance
            funct.urls = ['//*[@id="ui-id-2"]']
            funct.repetir = 3
            funct.quantidades_tentativas = 4
            # funct.retornar = True
            funct.grupo_newcon = self.grupo_newcon
            existeApuracao = funct.funct()
            # existeApuracao = Funct(
            #     driver=self.driver, path_all_log=self.path_all_log, urls=[url],
            #     repetir=2, retornar=retornar).funct()
        except UnexpectedAlertPresentException as e:
            print('CONEXAO OBS:[!] Error: ' + str(e))
            existeApuracao = False
            print('CONEXAO OBS:tentar pricionar f5')
            # err.append(url)
            # url = '//*[@id="divLoading"]'
            # url = '//*[@id="formulario"]/div[1]/div/div[2]'
            # faz = 'keys'
            # digitar = Keys.F5
            # repetir = 10
            # Funct(driver=self.driver, path_all_log=self.path_all_log, urls=[url],  faz=faz, digitar=digitar, repetir=repetir).funct()
            self.driver.refresh()
            print('CONEXAO OBS:Não existe aputacao funcao deu erro')
            time.sleep(10)
        except TimeoutException as t:
            # err.append(url)
            existeApuracao = False
            print('CONEXAO OBS:[!] Timeout: ' + str(t))
            print('CONEXAO OBS:Não existe aputacao tempo expirou')
            time.sleep(10)
        return existeApuracao

    # def navegar_newcon4(self):
    #     tempo = 10
    #     url = '//*[@id="CP"]'  # contemplacao
    #     Funct(driver=self.driver, path_all_log=self.path_all_log, urls=[url], tempo=tempo).funct()
    #     url = '//*[@id="subs"]/ul/li[2]/a'  # contemplacao
    #     Funct(driver=self.driver, path_all_log=self.path_all_log, urls=[url]).funct()
    #     url = '//*[@id="ctl00_Conteudo_ctl00_tvwMenut1"]'  # resultado da ultima assembeia
    #     Funct(driver=self.driver, path_all_log=self.path_all_log, urls=[url]).funct()
    #     url = '//*[@id="ctl00_Conteudo_edtCD_Grupo"]'  # campo grupo
    #     faz = 'keys'
    #     Funct(driver=self.driver, digitar=self.grupo_newcon, path_all_log=self.path_all_log, urls=[url], faz=faz).funct()  # noqa
    #     url = '//*[@id="ctl00_Conteudo_btnOK"]'  # botao confirmar
    #     Funct(driver=self.driver, path_all_log=self.path_all_log, urls=[url]).funct()

    def padrao_escolha_df(self):
        tarefa = Tarefa()
        tarefa.driver = self.driver
        tarefa.path_all_log = self.path_all_log
        tarefa.tpInicSegProg = self.tpInicSegProg
        tarefa.grupo_newcon = self.grupo_newcon
        tarefa.ultCel1 = 0  # necessario para saber se df atualizou
        tarefa.ultCel2 = 0  # necessario para saber se df atualizou
        tarefa.colCel1 = 1
        tarefa.colCel2 = -1
        tarefa.indTx1 = 'Grupo'
        tarefa.tag1 = 'table'
        tarefa.tag2 = 'tr'
        tarefa.tag3 = 'td'
        tarefa.tagCab = 'th'
        return tarefa

    def escolherDfNewcon(self):
        print('3')
        tarefa = self.padrao_escolha_df()
        print('4')
        tarefa.url = '//*[@id="ctl00_Conteudo_div_Confirmadas"]'  # df
        tarefa.colCel1 = 4
        tarefa.ultNIndex = self.ultNIndex1
        htmlNew, ultNIndex, ultCel1, ultCel2 = tarefa.df_newcon()
        # htmlNew, ultNIndex, ultCel1, ultCel2 = Tarefa(
        #     driver=self.driver, url=url, path_all_log=self.path_all_log, ultNIndex=ultNIndex,
        #     tpInicSegProg=self.tpInicSegProg, grupo_newcon=self.grupo_newcon, ultCel1=ultCel1,
        #     ultCel2=ultCel2, colCel1=colCel1, colCel2=colCel2, indTx1=indTx1, tag1=tag1, tag2=tag2,
        #     tag3=tag3, tagCab=tagCab).df_newcon()
        return htmlNew, ultNIndex

    


    def presentScreen(self):
        funct = Funct()
        funct.driver = self.driver
        funct.xpath_present_secreen = '//*[@id="divLoading"]/img'
        funct.path_all_log = self.path_all_log
        funct.grupo_newcon = self.grupo_newcon
        funct.tempo = 1
        retorno = funct.funct()
        # retorno = Funct(driver=self.driver, urls=[url], faz=faz, path_all_log=self.path_all_log, grupo_newcon=self.grupo_newcon).funct()  # noqa
        return retorno

    

    def tratarDf360(self):
        colunaGrupo = 'Grupo'
        textoVazio = ['=']
        colunaExcluir = ['Ind.correcao', 'Parcelasapagar']
        for coluna in colunaExcluir:
            self.df = Tratar(df=self.df, coluna=coluna).dfColunaExcluir()  # excluir coluna
        coluna2 = 'Valor'
        self.df = Tratar(df=self.df, coluna=colunaGrupo, coluna2=coluna2).dfColunaOrdenar()
        self.df = Tratar(df=self.df).dfColunaIndex()
        self.df = Tratar(df=self.df, coluna=colunaGrupo).dfLinhaRepetida()
        coluna2 = 'Plano'
        self.df = Tratar(df=self.df, coluna=colunaGrupo, coluna2=coluna2).dfLinhaJuntarSemRepetir()
        coluna2 = 'Marca'
        self.df = Tratar(df=self.df, coluna=colunaGrupo, coluna2=coluna2).dfLinhaJuntarSemRepetir()
        coluna2 = 'Modelo'
        self.df = Tratar(df=self.df, coluna=colunaGrupo, coluna2=coluna2).dfLinhaJuntarSemRepetir()
        coluna2 = 'Valor'
        self.df = Tratar(df=self.df, coluna=colunaGrupo, coluna2=coluna2).dfLinhaJuntarMenorMaior()
        coluna2 = 'Parcela1'
        self.df = Tratar(df=self.df, coluna=colunaGrupo, coluna2=coluna2).dfLinhaJuntarMenorMaior()
        self.df = Tratar(df=self.df, coluna=colunaGrupo, textoLinha=textoVazio).dfLinhaExcluir()
        self.df = Tratar(df=self.df).dfColunaIndex()
        colunaPontoVirgula = ['Parcela1', 'Medialance', 'TA']
        for coluna in colunaPontoVirgula:
            self.df = Tratar(df=self.df, coluna=coluna).dfColunaPontaVirgula()
        return self.df

    def tratarDfNewcon(self):
        colunaGrupo = 'Grupo'
        colunaLance = 'Lance'
        colunaModalidade = 'Modalidade'
        colunaJuncao = 'Juncao'
        colunaX = ['X']
        listaColLinha = [colunaGrupo, colunaX[0] + '1']
        listaColCriarMover = []
        colunaDtContp = 'Dt.contp'
        colunaData = ['Dt.contp', 'Dt.confir']
        colunaDataDesclassificado = 'Dt.descla'
        colunaDataInvertida = ['DataInvertida1', 'DataInvertida2']
        mesmaLinha = True
        # textoVazio = ['']
        # colunaExcluir1 = ['Cota', 'Modalidade', 'Bem', 'Filial', 'Lance', 'Juncao']
        colunaExcluir = ['Cota', 'Modalidade', 'Bem', 'Filial', 'Lance', 'Juncao', 'X']
        self.df = Tratar(df=self.df, coluna=colunaModalidade).dfLinhaCaracterEspecial()
        textoLinha = ['Sorteio', '']
        # excluir linhas Sorteio da coluna modalidade
        self.df = Tratar(df=self.df, coluna=colunaModalidade, textoLinha=textoLinha).dfLinhaExcluir()  # noqa
        self.df = Tratar(df=self.df).dfColunaIndex()  # irar criar uma nova coluna index
        # excluir linhas Sorteio da coluna modalidade
        self.df = Tratar(df=self.df, coluna=colunaDtContp).dfLinhaExcluir2()
        self.df = Tratar(df=self.df).dfColunaIndex()  # irar criar uma nova coluna index
        self.df = Tratar(df=self.df).dfColunaALterarNome()  # altera o nome da coluna
        self.df, existir = Tratar(df=self.df, coluna=colunaDataDesclassificado).dfColunaExiste()
        if existir is True:
            colunaData.append('Dt.descla')
            colunaDataInvertida.append('DataInvertida3')
        colunaExcluir.extend(colunaData)
        colunaExcluir.extend(colunaDataInvertida)
        listaColLinha.extend(colunaData)
        listaColCriarMover.extend(colunaData)
        listaColCriarMover.append(colunaLance)
        listaColCriarMover.extend(colunaX)
        # inverter a data e salvar em outro local
        self.df = Tratar(df=self.df, coluna=colunaData, coluna2=colunaDataInvertida).dfColunaData()
        colunaDataInvertida.insert(0, colunaGrupo)  # ira inserir no inico a coluna grupo
        # juntar duas colunas e criando uma nova
        self.df = Tratar(df=self.df, coluna=colunaDataInvertida, coluna2=colunaJuncao).dfColunaJuntar()  # noqa
        del (colunaDataInvertida[0])
        self.df = Tratar(df=self.df, coluna=colunaLance).dfColunaConverterFloat()
        # ordenar primeiro coluna
        self.df = Tratar(df=self.df, coluna=colunaJuncao).dfColunaOrdenar()
        self.df = Tratar(df=self.df).dfColunaIndex()  # irar criar uma nova coluna index
        # exluir linhas repetidas
        self.df = Tratar(df=self.df, coluna=colunaJuncao).dfLinhaRepetida()
        # juntar linha com '-
        self.df, listaLinha = Tratar(df=self.df, coluna=colunaJuncao, coluna2=colunaLance).dfLinhaJuntar()  # noqa'
        # excluirar todas as linhas que tiver na lista
        self.df = Tratar(df=self.df, lista=listaLinha).dfLinhaVaziaExcluir()
        self.df = Tratar(df=self.df).dfColunaIndex()
        # substituir campo repetidos na linha
        self.df = Tratar(df=self.df, coluna=colunaGrupo).dfLinhaRepetida()
        # mover para coluna nova a partir '-'
        self.df = Tratar(df=self.df, coluna=colunaLance, coluna2=colunaX, ap=self.ap).dfColunaMover()  # noqa
        # define os ultimos de cada campo
        self.df, nUltColX = Tratar(df=self.df, coluna=listaColCriarMover).dfColunaNUlt()
        self.df = Tratar(
            df=self.df,
            coluna=listaColCriarMover,
            nUltColX=nUltColX).dfColunaRenomearNUlt()  # define os ultimos de cada campo
        # self.df = Tratar(df=self.df, coluna=colunaData).dfDataIgual()  # compar
        # as datas de Dt com Dt2 e apaga dt2 se igual
        self.df = Tratar(
            df=self.df,
            coluna=colunaData,
            coluna2=colunaGrupo).dfLinhaRepetida2Col()  # substituir linhas repetidas
        self.df, listaMes = Tratar(
            df=self.df, coluna=colunaData).dfColunaDataMes()  # meses existentes
        if listaMes != []:
            for mes in listaMes:
                nUltColConfm = 1
                # codicao para linha com grupo visivel e com mes
                self.df, listaLinha = Tratar(
                    df=self.df, coluna=listaColLinha, mes=mes).dfLinhaCodicaoColComGrupo()
                self.df = Tratar(
                    df=self.df,
                    coluna=listaColCriarMover,
                    nUltColConfm=nUltColConfm,
                    listaLinha=listaLinha,
                    mesmaLinha=mesmaLinha,
                    mes=mes).dfColCriarMover()  # move coluna dtcontp 1ª vez linha grupo
                while True:
                    while True:
                        # cod. p/ linha sem grupo visivel e sem mes
                        self.df, listaLinha = Tratar(
                            df=self.df, coluna=listaColLinha).dfLinhaCodicaoColSemGrupoSemContp()
                        if listaLinha == []:
                            break
                        nUltColConfm += 1
                        self.df = Tratar(
                            df=self.df,
                            coluna=listaColCriarMover,
                            coluna2=colunaGrupo,
                            nUltColX=nUltColX,
                            nUltColConfm=nUltColConfm,
                            listaLinha=listaLinha,
                            mes=mes).dfColCriarMover()
                        # excluirar todas as linhas que tiver na lista
                        self.df = Tratar(df=self.df, lista=listaLinha).dfLinhaVaziaExcluir()
                        self.df = Tratar(df=self.df).dfColunaIndex()
                    self.df, listaLinha = Tratar(
                        df=self.df, coluna=listaColLinha, mes=mes).dfLinhaCodicaoColSemGrupoComContp()
                    if listaLinha == []:
                        break
                    nUltColConfm = 1
                    self.df = Tratar(
                        df=self.df,
                        coluna=listaColCriarMover,
                        coluna2=colunaGrupo,
                        nUltColX=nUltColX,
                        nUltColConfm=nUltColConfm,
                        listaLinha=listaLinha,
                        mes=mes).dfColCriarMover()
                    # excluirar todas as linhas que tiver na lista
                    self.df = Tratar(df=self.df, lista=listaLinha).dfLinhaVaziaExcluir()
                    self.df = Tratar(df=self.df).dfColunaIndex()
            # self.df, listaNUltCol = Tratar(df=self.df,
            # coluna=listaColCriarMover).dfColunaNUlt()  # ultimo da oluna X que é o
            # lance
            self.df, listaColuna = Tratar(
                df=self.df, coluna=listaColLinha, mes=mes).dfColunaCodicaoVazia()
            colunaExcluir.extend(listaColuna)
            # for coluna in colunaExcluir:
            # self.df = Tratar(df=self.df, coluna=coluna,
            # nUltCol=nUltColX).dfColunaExcluir()  # excluir coluna
        else:
            nUltColConfm = 1
            # codicao para linha com grupo visivel e com mes
            self.df, listaLinha = Tratar(
                df=self.df, coluna=listaColLinha).dfLinhaCodicaoColSoGrupo()
            self.df = Tratar(
                df=self.df,
                coluna=listaColCriarMover,
                nUltColConfm=nUltColConfm,
                listaLinha=listaLinha,
                mesmaLinha=mesmaLinha).dfColCriarMover()  # mvColGp
            colunaExcluir2 = ['Sequencia', 'Ocorrencia', 'Parcela']
            colunaExcluir.extend(colunaExcluir2)
        for coluna in colunaExcluir:
            self.df = Tratar(
                df=self.df,
                coluna=coluna,
            )
        return self.df

    def tratarDfFixar(self):
        colunaConfir = 'Dt.confir'
        colunaDescla = 'Dt.descla'
        colunaContp = 'Dt.contp'
        colunas = self.df.columns.to_list()
        self.df = Tratar(df=self.df, colunas=colunas, coluna=colunaConfir).dfColunaExcluirFixar()
        colunas = self.df.columns.to_list()
        self.df = Tratar(df=self.df, colunas=colunas, coluna=colunaDescla).dfColunaExcluirFixar()
        colunas = self.df.columns.to_list()
        listaGrupoContp = Tratar(
            df=self.df,
            colunas=colunas,
            coluna=colunaContp).colunaGrupoDtContp()
        numeroMes = Tratar(listaGrupoContp=listaGrupoContp).colunaDtContpContar()
        listaGrupoLanceFixar = Tratar(
            df=self.df,
            coluna=colunaContp,
            numeroMes=numeroMes).colunaDtContpLance()
        listaGrupoLanceCompleto = Tratar(
            df=self.df,
            listaGrupoContp=listaGrupoContp,
            listaGrupoLanceFixar=listaGrupoLanceFixar).colunaGrupoLanceFixar()

        # criar as colunas vazias
        self.df = Tratar(df=self.df, numeroMes=numeroMes).dfColunaVariasCriarVazia()
        # move a coluna contp
        self.df = Tratar(
            df=self.df,
            numeroMes=numeroMes,
            listaGrupoContp=listaGrupoContp).dfColunaMoverContpFixar()
        # return self.df
        # move a coluna lance
        self.df = Tratar(
            df=self.df,
            numeroMes=numeroMes,
            listaGrupoLanceCompleto=listaGrupoLanceCompleto).dfColunaMoverLanceFixar()
        self.df = Tratar(df=self.df).dfColunaOrdenarSequencia2()
        return self.df

    def dfMesclaOrganizar(self):
        tratar = Tratar()
        colunaGrupo = 'Grupo'
        colunaComtp = 'Dt.contp'
        colunaConfir = 'Dt.confir'
        colunaTA = 'TA'
        # self.df = Tratar(df=self.df, coluna=colunaGrupo, coluna2=colunaTA).dfColunaOrdenar()  # ordenar primeiro coluna
        # self.df = Tratar(df=self.df).dfColunaIndex()  # irar criar uma nova coluna index
        colunas = self.df.columns.to_list()
        # lanceCondicao = False
        #  inf das tres ultimos meses
        tratar.df = self.df
        tratar.colunas = colunas
        colunaLista = tratar.dfCabecalhoMes()
        # colunaLista = Tratar(df=self.df, colunas=colunas).dfCabecalhoMes()
        # criar coluna ordenar baseado nos tres meses e formata informacoes
        tratar.coluna = 'Ordenar'
        tratar.colunaLista = colunaLista
        self.df = tratar.dfColunaCriarBaseOutraColuna()
        # self.df = Tratar(
        #     df=self.df,
        #     coluna='Ordenar',
        #     colunaLista=colunaLista).dfColunaCriarBaseOutraColuna()
        # ira salvar o numero do grupo na lina da coluna 'ordenar' que não tem info coluna TA
        tratar.df = self.df
        tratar.coluna = 'Ordenar'
        tratar.coluna2 = colunaTA
        tratar.coluna3 = colunaGrupo
        self.df = tratar.dfColunaDesclassificadaOrdenar()
        # self.df = Tratar(df=self.df, coluna='Ordenar', coluna2=colunaTA,
        #                  coluna3=colunaGrupo).dfColunaDesclassificadaOrdenar()
        tratar.df = self.df
        tratar.coluna = 'Ordenar'
        tratar.coluna2 = colunaTA
        self.df = tratar.dfColunaOrdenar()  # ordenar primeiro coluna
        # self.df = Tratar(
        #     df=self.df,
        #     coluna='Ordenar',
        #     coluna2=colunaTA).dfColunaOrdenar()
        tratar.df = self.df
        self.df = tratar.dfColunaIndex()  # irar criar uma nova coluna index
        # self.df = Tratar(df=self.df).dfColunaIndex()
        tratar.df = self.df
        tratar.coluna = colunaComtp
        tratar.coluna2 = colunaConfir
        self.df = tratar.dfValorExcluirRepetida()  # ordenar primeiro coluna
        # self.df = Tratar(
        #     df=self.df,
        #     coluna=colunaComtp,
        #     coluna2=colunaConfir).dfValorExcluirRepetida()
        tratar.colunas = colunas
        colunaCorreta, listaColunaDeslocadaConfm, listaColunaDeslocadaDescl, listaColunaDeslocadaLance = tratar.colunaForaDeOrdem()
        # colunaCorreta, listaColunaDeslocadaConfm, listaColunaDeslocadaDescl, listaColunaDeslocadaLance = Tratar(
        #     colunas=colunas).colunaForaDeOrdem()
        # ira informar o numero do mes a sequencia
        tratar.campoLista = listaColunaDeslocadaConfm
        listaColunaDeslocadaConfm = tratar.dfCamposNumero()
        # listaColunaDeslocadaConfm = Tratar(campoLista=listaColunaDeslocadaConfm).dfCamposNumero()
        # ira informar o numero do mes a sequencia
        tratar.campoLista = listaColunaDeslocadaLance
        listaColunaDeslocadaLance = tratar.dfCamposNumero()
        # listaColunaDeslocadaLance = Tratar(campoLista=listaColunaDeslocadaLance).dfCamposNumero()
        # ira colocar a coluna no local correto
        tratar.colunaCorreta = colunaCorreta
        tratar.listaColunaDeslocadaConfm = listaColunaDeslocadaConfm
        colunaCorreta = tratar.colunaLocalCorreto()
        # colunaCorreta = Tratar(
        #     colunaCorreta=colunaCorreta,
        #     listaColunaDeslocadaConfm=listaColunaDeslocadaConfm).colunaLocalCorreto()
        # ira colocar a coluna no local correto2
        tratar.colunaCorreta = colunaCorreta
        tratar.listaColunaDeslocadaDescl = listaColunaDeslocadaDescl
        colunaCorreta = tratar.colocarLocalCorreto2()
        # colunaCorreta = Tratar(
        #     colunaCorreta=colunaCorreta,
        #     listaColunaDeslocadaDescl=listaColunaDeslocadaDescl).colocarLocalCorreto2()
        # ira colocar a coluna no local correto3
        tratar.colunaCorreta = colunaCorreta
        tratar.listaColunaDeslocadaLance = listaColunaDeslocadaLance
        colunaCorreta = tratar.colocarLocalCorreto3()
        # colunaCorreta = Tratar(
        #     colunaCorreta=colunaCorreta,
        #     listaColunaDeslocadaLance=listaColunaDeslocadaLance).colocarLocalCorreto3()
        # alterar ordem das colunas colocando mes mais recente primeiro e
        # excluindo algumas colunas nao necessaria

        tratar.df = self.df
        tratar.colunaCorreta = colunaCorreta
        tratar.colunas = colunas
        self.df = tratar.dfColunaOrdenarSequencia()
        # self.df = Tratar(df=self.df, colunaCorreta=colunaCorreta,
        #                  colunas=colunas).dfColunaOrdenarSequencia()
        tratar.df = self.df
        tratar.listaGrupo360 = self.listaGrupo360
        self.df = tratar.dfColunaMoverLanceNaoContemplado()
        # self.df = Tratar(
        #     df=self.df,
        #     listaGrupo360=self.listaGrupo360).dfColunaMoverLanceNaoContemplado()
        tratar.df = self.df
        self.df = tratar.dfColunaSepararMenorMaior()
        # self.df = Tratar(df=self.df).dfColunaSepararMenorMaior()
        tratar.df = self.df
        self.df = tratar.dfColunaSituacao()
        # self.df = Tratar(df=self.df).dfColunaSituacao()
        tratar.df = self.df
        self.df = tratar.colunaOrganizar2()
        # self.df = Tratar(df=self.df).colunaOrganizar2()
        return self.df

    def gravar(self):
        log = Log()
        log.path_all_log = self.path_all_log
        try:
            if self.extencao is None:
                self.df.to_csv(self.pastaArquivo, index=False, header=True)
            elif self.extencao == '.xlsx':
                # self.df.to_excel(self.pastaArquivo, index=False, header=True, float_format='%.4f', engine='openpyxl')
                self.df.to_csv(self.pastaArquivo, sep='\t', index=False, encoding='latin_1', decimal=',')  # noqa
            else:
                write_log = 'ERRO CONEXAO: Foi digitada uma extencao não especificada'
                log.write_log = write_log
                log.escrever()
                print(write_log)
        except AttributeError as e:
            write_log = f'ERRO CONEXAO: Tabela vazia, pasta: {self.pastaArquivo}. '
            write_log += f'A classe do erro: {e.__class__.__name__} '
            log.write_log = write_log
            log.escrever()
            print(write_log)
        self.zerar_variaveis()



    def gravarDf360(self):
        tratar = Tratar()
        tratar.df = self.df
        self.df = tratar.dfColunaIndexNumeroLinha()  # criar o index da nova df
        # self.df = Tratar(df=self.df).dfColunaIndexNumeroLinha()
        colunas = self.df360.columns.to_list()
        for coluna in colunas:  # criar coluna
            tratar.df = self.df
            tratar.coluna = coluna
            self.df = tratar.dfColunaCriarVazia()
            # self.df = Tratar(df=self.df, coluna=coluna).dfColunaCriarVazia()
        tratar.df = self.df
        tratar.df2 = self.df_newcon_info
        self.df = tratar.dfDf2()
        # self.df = Tratar(df=self.df, df2=self.df_newcon_info).dfDf2()
        tratar.df = self.df
        tratar.df2 = self.df360
        tratar.coluna = 'Grupo'
        self.df = tratar.dfDf2RemoverRepetido360()
        # self.df = Tratar(df=self.df, df2=self.df360, coluna='Grupo').dfDf2RemoverRepetido360()
        return self.df

    def dfConverterStr(self):
        coluna = 'Grupo'
        self.df = Tratar(df=self.df, coluna=coluna).colunaGruposStr()
        return self.df


if __name__ == '__main__':
    import main
    # main()
