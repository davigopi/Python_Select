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

funct = Funct()
log = Log()
read_salve = Read_salve()
convert = Convert()

class Conexao:
    def __init__(self, *args, **kwargs):
        self.driver = kwargs.get('driver')
        self.user = kwargs.get('user')
        self.password = kwargs.get('password')
        self.pAL = kwargs.get('pAL')
        self.tpInicSegProg = kwargs.get('tpInicSegProg')
        self.html1Anterior = kwargs.get('html1Anterior')
        self.html2Anterior = kwargs.get('html2Anterior')
        self.ultNIndex360 = kwargs.get('ultNIndex360')
        self.ultNIndex1 = kwargs.get('ultNIndex1')
        self.ultNIndex2 = kwargs.get('ultNIndex2')
        self.ultNIndex3 = kwargs.get('ultNIndex3')
        self.ultNIndex4 = kwargs.get('ultNIndex4')
        self.ap = kwargs.get('ap')
        self.g_newcon = kwargs.get('g_newcon')
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
        
        log.pAL = self.pAL
        

    def zerar_variaveis(self):
        self.extencao = None

    # atalhos para read_salve
    def salve_clickvend(self, write_file, folder_file):
        read_salve.write_file = write_file
        read_salve.folder_file = folder_file
        read_salve.to_write()

    def read_clickvend(self, folder_file):
        read_salve.folder_file = folder_file
        return read_salve.to_read()

    # atalhos para fuct
    def func_key(self, path, keyboard):
        funct.path = path
        funct.digitar = keyboard
        funct.faz = 'keys'
        return funct.funct()
    
    def func_click(self, path):
        funct.path = path
        return funct.funct()
    
    # def func_get_select(self, path, tag):
    #     funct.path = path
    #     funct.tag = tag
    #     funct.faz = 'get_select'
    #     return funct.funct()

    def func_get_select(self, path, tag1=''):
        funct.path = path
        funct.tag1 = tag1
        funct.faz = 'get_select'
        return funct.funct()
    
    def func_select_value(self, path, value):
        funct.path = path
        funct.value = value
        funct.faz = 'select_value'
        return funct.funct()
    
    def func_checkbox(self, path):
        funct.path = path
        funct.faz = 'checkbox'
        if funct.funct():
            return funct.dados
        return False
    
    def func_wait_df_or_empty(self, path):
        funct.path = path
        funct.faz = 'wait_df_or_empty'
        return funct.funct()
    
  
    
    def func_key_single(self, path, key_single, quantity):
        for _ in range(quantity):
            funct.path = path
            funct.key_single = key_single
            funct.faz = 'key_single'
            funct.funct()
        return

    # clickvenda:
    # clickvenda segundo nivel:
    def treat_dados(self, dados):
        dict_dados = [
            {
                "value": dado.get_attribute("value"),
                "text": dado.text.strip()
            }
            for dado in dados
            if dado.get_attribute("value")
        ]
        return dict_dados
    
    def click_get_select(self, path, tag1):
        self.func_click(path_clickvenda[path])
        return self.func_get_select(path_clickvenda[path], tag1)

    def marked_checkbox(self):
        if self.func_checkbox(path_clickvenda['credito_referenciado'])  == 'OK':
            self.func_click(path_clickvenda['credito_referenciado'])    

    # clickvenda primeiro nivel:
    def log_site(self, info_site, path_site):
        funct.driver = self.driver
        funct.pAL = self.pAL
        funct.path_loading = path_site['loading']
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
        planos = self.treat_dados(self.click_get_select('busca_andamento_plano', 'option'))
        for plano in planos:
            if not plano["value"]:
                continue
            self.func_select_value(path_clickvenda['busca_andamento_plano'], plano['value'])
            self.marked_checkbox()
            marcas = self.treat_dados(self.click_get_select('busca_andamento_modelo', 'option'))
            for marca in marcas:
                if not marca["value"]:
                    continue
                self.func_select_value(path_clickvenda['busca_andamento_modelo'], marca['value'])
                self.func_click(path_clickvenda['btn_buscar'])
                self.func_wait_df_or_empty(path_clickvenda['id_divPasso21'])
                convert.html_table = self.func_get_select(path_clickvenda['id_divPasso21_table'], tag_table)
                list_row = convert.table_html_in_json()
                new_row = []
                for row in list_row:
                    row['Plano'] = plano['text']
                    row['Marca'] = marca['text']
                    new_row. append(row)
                rows += new_row
            # break
        self.salve_clickvend(rows, arq_clickvenda)
        return True

    # newcon:
    # newcon primeiro nível
    def info_newcon(self):
        # lista = []
        # tarefa = Tarefa()
        # tarefa.driver = self.driver
        # tarefa.pAL = self.pAL
        # tarefa.g_newcon = self.g_newcon
        # tarefa.xpath_present_secreen = '//*[@id="divLoading"]/img'
        for info in list_info:
            print('inico')
            print(self.func_get_select(path_newcon[info]))
            print('fim')
            time.sleep(2)

        # convert.html_table = self.func_get_select(path_newcon['id_ctl00_Conteudo_grdContemplacoes_Confirmadas'], tag_table, '')
        # list_row = convert.table_html_in_json()
        # self.func_click(path_newcon['id_ui_id_8'])
        # time.sleep(6)
        # convert.html_table = self.func_get_select(path_newcon['id_ctl00_Conteudo_grdContemplacoes_Confirmadas_Canceladas'], tag_table, '')
        # list_row = convert.table_html_in_json()
        time.sleep(66)
        return
        tarefa.url = '//*[@id="ctl00_Conteudo_lblCD_Grupo"]'  # grupo
        inf = tarefa.infoHTML()
        if inf == 'ERROR':
            return 'ERROR'

            # inf = Tarefa(
            #     driver=self.driver,
            #     g_newcon=self.g_newcon,
            #     pAL=self.pAL,
            #     url=url).infoHTML()
        lista.append(inf)
        print('2')
        tarefa.url = '//*[@id="ctl00_Conteudo_lblPZ_Comercializacao"]'
        inf = tarefa.infoHTML()
        if inf == 'ERROR':
            return 'ERROR'
        # inf = Tarefa(
        #     driver=self.driver,
        #     g_newcon=self.g_newcon,
        #     pAL=self.pAL,
        #     url=url).infoHTML()
        lista.append(inf)
        print('3')
        tarefa.url = '//*[@id="ctl00_Conteudo_lblQT_Assembleia_Realizada"]'
        inf = tarefa.infoHTML()
        if inf == 'ERROR':
            return 'ERROR'
        # inf = Tarefa(
        #     driver=self.driver,
        #     g_newcon=self.g_newcon,
        #     pAL=self.pAL,
        #     url=url).infoHTML()
        lista.append(inf)
        print('4')
        tarefa.url = '//*[@id="ctl00_Conteudo_lblQT_Assembleia_ARealizar"]'
        inf = tarefa.infoHTML()
        if inf == 'ERROR':
            return 'ERROR'
        # inf = Tarefa(
        #     driver=self.driver,
        #     g_newcon=self.g_newcon,
        #     pAL=self.pAL,
        #     url=url).infoHTML()
        lista.append(inf)
        print('5')
        tarefa.url = '//*[@id="ctl00_Conteudo_lblDT_Prox_Assembleia"]'
        inf = tarefa.infoHTML()
        if inf == 'ERROR':
            return 'ERROR'
        # inf = Tarefa(
        #     driver=self.driver,
        #     g_newcon=self.g_newcon,
        #     pAL=self.pAL,
        #     url=url).infoHTML()
        lista.append(inf)
        print('6')
        tarefa.url = '//*[@id="ctl00_Conteudo_lblDT_Prox_Vencimento"]'
        inf = tarefa.infoHTML()
        if inf == 'ERROR':
            return 'ERROR'
        # inf = Tarefa(
        #     driver=self.driver,
        #     g_newcon=self.g_newcon,
        #     pAL=self.pAL,
        #     url=url).infoHTML()
        lista.append(inf)
        return lista





    # antigos: 








    def logar360(self):
        funct = Funct()
        funct.driver = self.driver
        # funct.retornar = True
        funct.pAL = self.pAL
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
                # log.pAL = self.pAL
                escreva = 'ERRO CONEXAO LOGAR: SUA CONEXAO NÃO É PARTICULAR'
                log.escreva = escreva
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
        funct.pAL = self.pAL
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
        funct.pAL = self.pAL
        funct.urls = ['//*[@id="busca_andamento_plano"]']
        funct.tempo = 120
        funct.funct()
        # Funct(driver=self.driver, urls=[url], tempo=tempo, pAL=self.pAL).funct()
        print('######################## informar inicio #############################')
        funct.faz = 'inform'
        funct.tag1 = 'select'
        funct.tag2 = 'option'
        html = funct.funct()
        print('######################## informar fim #############################')
        # html = Funct(driver=self.driver, urls=[url], faz=faz, tag1=tag1, pAL=self.pAL).funct()
        dfsite = DfSite()
        dfsite.html = html
        dfsite.tag1 = 'select'
        dfsite.tag2 = 'option'
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
        tarefa.pAL = self.pAL
        tarefa.tag1 = 'select'
        tarefa.tag2 = 'option'
        tarefa.url = '//*[@id="busca_andamento_marca"]'
        tarefa.texto = texto1
        html2 = tarefa.tasks_repeat_360()
        # html2 = Tarefa(
        #     driver=self.driver,
        #     tpInicSegProg=self.tpInicSegProg,
        #     pAL=self.pAL,
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
            tarefa.tag2 = 'option'
            tarefa.url = '//*[@id="busca_andamento_modelo"]'
            tarefa.texto = texto2
            html3 = tarefa.tasks_repeat_360()
            # html3 = Tarefa(
            #     driver=self.driver,
            #     tpInicSegProg=self.tpInicSegProg,
            #     pAL=self.pAL,
            #     url=url,
            #     texto=texto2,
            #     tag1=tag1,
            #     tag2=tag2).tasks_repeat_360()
            for texto3 in html3:
                botao = Botao()
                botao.driver = self.driver
                botao.pAL = self.pAL
                botao.texto = texto3
                botao.url = '//*[@id="busca_andamento_modelo"]'
                botao.botao1()
                # Botao(driver=self.driver, pAL=self.pAL, texto=texto3, url=url).botao1()
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
                #     driver=self.driver, pAL=self.pAL, tpInicSegProg=self.tpInicSegProg,
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
            escreva = 'CONEXAO OBS: Escolher DF em construacao não existir, '
            escreva += f'pois nao existem dfs: {e.__class__.__name__}'
            log.escreva = escreva
            log.escrever()
            # Log(pAL=self.pAL, escreva=escreva).escrever()
            print('CONEXAO OBS:@@@@@@@@@@@@@@@@dfConst@@@@@@@@@@@@@@@@@@@@False@@@@@@@@@@@@@@@')
            return ultimoPlano, self.html1Anterior, self.html2Anterior, ultNIndex, False
        # salvar arq

    def logarNewcon(self):
        funct = Funct()
        funct.driver = self.driver
        funct.pAL = self.pAL

        funct.digitar = self.user
        funct.faz = 'keys'
        funct.urls = ['//*[@id="edtUsuario"]']
        funct.funct()
        # url = '//*[@id="edtUsuario"]'
        # faz = 'keys'
        # Funct(
        #     driver=self.driver,
        #     digitar=self.usuario,
        #     pAL=self.pAL,
        #     urls=[url],
        #     faz=faz).funct()

        funct.digitar = self.password
        funct.faz = 'keys'
        funct.urls = ['//*[@id="edtSenha"]']
        funct.funct()

        # url = '//*[@id="edtSenha"]'
        # faz = 'keys'
        # Funct(driver=self.driver, digitar=self.password, pAL=self.pAL, urls=[url], faz=faz).funct()

        funct.urls = ['//*[@id="btnLogin"]']
        funct.funct()
        # url = '//*[@id="btnLogin"]'
        # Funct(driver=self.driver, pAL=self.pAL, urls=[url]).funct()

    def navegar_newcon_contemplacao(self):
        funct.driver = self.driver
        funct.pAL = self.pAL
        self.func_click(path_newcon['id_CP'])  # contemplacao
        self.func_click(path_newcon['id_subs'] )  # contemplacao
        self.func_click(path_newcon['id_ctl00_Conteudo_ctl00_tvwMenut1'])  # Resultado de Assembleia
        self.func_key(path_newcon['id_ctl00_Conteudo_edtCD_Grupo'], self.g_newcon)  # campo grupo
        self.func_click(path_newcon['id_ctl00_Conteudo_btnOK'])  # botao confirmar

    def navegar_newcon_df(self):
        funct = Funct()
        funct.driver = self.driver
        funct.pAL = self.pAL
        print('1')
        funct.urls = ['//*[@id="tabs"]/ul/li[1]']
        funct.xpath_present_secreen = '//*[@id="divLoading"]/img'
        funct.funct()
        print('2')
        funct.urls = ['//*[@id="ctl00_Conteudo_grdContemplacoes_Confirmadas"]/tbody']  # df
        funct.xpath_present_secreen = '//*[@id="divLoading"]/img'
        funct.faz = 'locate'
        # funct.retornar = self.retornar
        retorno = funct.funct()
        # retorno = Funct(driver=self.driver, pAL=self.pAL, urls=[url], faz=faz, retornar=self.retornar).funct()  # noqa
        if retorno is False:
            print('CONEXAO ERROR: ao localizar df')

    def navegar_newcon_retorna_assembleia(self):
        funct = Funct()
        funct.driver = self.driver
        funct.pAL = self.pAL
        funct.urls = ['//*[@id="ui-id-6"]']  # Confirmadas aba
        funct.funct()
        # Funct(driver=self.driver, pAL=self.pAL, urls=[url]).funct()

        # botao assembeia
        funct.urls = ['//*[@id="ctl00_Conteudo_btnRetornaAssembleia"]']
        funct.funct()
        # Funct(driver=self.driver, pAL=self.pAL, urls=[url]).funct()

    def navegar_newcon_desc(self):
        print('1')
        funct = Funct()
        funct.driver = self.driver
        funct.pAL = self.pAL
        funct.tempo = 3
        funct.urls = ['//*[@id="ui-id-8"]']  # desc aba
        funct.funct()
        print('2')
        # botao desc
        funct.urls = ['//*[@id="ctl00_Conteudo_tabDesclassificadas"]']
        funct.funct()
        # Funct(driver=self.driver, pAL=self.pAL, urls=[url]).funct()

    def navegar_newcon_sequencia_apur(self):
        # url = '//*[@id="ctl00_Conteudo_btnCotasSorteadas"]'
        print('1')
        funct = Funct()
        funct.xpath_present_secreen = '//*[@id="divLoading"]/img'
        # Botao -> Sequência de Apuração
        funct.urls = ['//*[@id="ctl00_Conteudo_btnCotasSorteadas"]']
        funct.driver = self.driver
        funct.pAL = self.pAL
        # funct.retornar = True
        funct.funct()
        # Funct(driver=self.driver, pAL=self.pAL, urls=[url]).funct()
        try:
            print('2')
            funct.xpath_present_secreen = '//*[@id="divLoading"]/img'
            # Botão -> Sequência de Lance
            funct.urls = ['//*[@id="ui-id-2"]']
            funct.repetir = 3
            funct.quantidades_tentativas = 4
            # funct.retornar = True
            funct.g_newcon = self.g_newcon
            existeApuracao = funct.funct()
            # existeApuracao = Funct(
            #     driver=self.driver, pAL=self.pAL, urls=[url],
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
            # Funct(driver=self.driver, pAL=self.pAL, urls=[url],  faz=faz, digitar=digitar, repetir=repetir).funct()
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
    #     Funct(driver=self.driver, pAL=self.pAL, urls=[url], tempo=tempo).funct()
    #     url = '//*[@id="subs"]/ul/li[2]/a'  # contemplacao
    #     Funct(driver=self.driver, pAL=self.pAL, urls=[url]).funct()
    #     url = '//*[@id="ctl00_Conteudo_ctl00_tvwMenut1"]'  # resultado da ultima assembeia
    #     Funct(driver=self.driver, pAL=self.pAL, urls=[url]).funct()
    #     url = '//*[@id="ctl00_Conteudo_edtCD_Grupo"]'  # campo grupo
    #     faz = 'keys'
    #     Funct(driver=self.driver, digitar=self.g_newcon, pAL=self.pAL, urls=[url], faz=faz).funct()  # noqa
    #     url = '//*[@id="ctl00_Conteudo_btnOK"]'  # botao confirmar
    #     Funct(driver=self.driver, pAL=self.pAL, urls=[url]).funct()

    def padrao_escolha_df(self):
        tarefa = Tarefa()
        tarefa.driver = self.driver
        tarefa.pAL = self.pAL
        tarefa.tpInicSegProg = self.tpInicSegProg
        tarefa.g_newcon = self.g_newcon
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
        #     driver=self.driver, url=url, pAL=self.pAL, ultNIndex=ultNIndex,
        #     tpInicSegProg=self.tpInicSegProg, g_newcon=self.g_newcon, ultCel1=ultCel1,
        #     ultCel2=ultCel2, colCel1=colCel1, colCel2=colCel2, indTx1=indTx1, tag1=tag1, tag2=tag2,
        #     tag3=tag3, tagCab=tagCab).df_newcon()
        return htmlNew, ultNIndex

    def escolher_df_newcon_desc(self):
        print('3')
        tarefa = self.padrao_escolha_df()
        # tarefa = Tarefa()
        # tarefa.driver = self.driver
        # tarefa.pAL = self.pAL
        print('4')
        tarefa.url = '//*[@id="ctl00_Conteudo_div_Desclassificadas"]/div[1]'  # df
        # tarefa.url = '//*[@id="ctl00_Conteudo_tabDesclassificadas"]'
        # '//*[@id="ctl00_Conteudo_div_Desclassificadas"]/div[1]'
        # tarefa.ultCel1 = 0  # necessario para saber se df atualizou
        # tarefa.ultCel2 = 0  # necessario para saber se df atualizou
        # tarefa.colCel1 = 1  # coluna de teste 1
        # tarefa.colCel2 = -1  # coluna de teste 1
        # tarefa.indTx1 = 'Grupo'
        # tarefa.tag1 = 'table'
        # tarefa.tag2 = 'tr'
        # tarefa.tag3 = 'td'
        # tarefa.tagCab = 'th'
        tarefa.tempo = 3
        tarefa.ultNIndex = self.ultNIndex2
        # tarefa.tpInicSegProg = self.tpInicSegProg
        # tarefa.g_newcon = self.g_newcon
        htmlNew, ultNIndex, ultCel1, ultCel2 = tarefa.df_newcon()
        # htmlNew, ultNIndex, ultCel1, ultCel2 = Tarefa(
        #     driver=self.driver, url=url, pAL=self.pAL, ultNIndex=ultNIndex,
        #     tpInicSegProg=self.tpInicSegProg, g_newcon=self.g_newcon, tempo=tempo, ultCel1=ultCel1,
        #     ultCel2=ultCel2, colCel1=colCel1, colCel2=colCel2, indTx1=indTx1, tag1=tag1, tag2=tag2,
        #     tag3=tag3, tagCab=tagCab).df_newcon()
        return htmlNew, ultNIndex

    def escolherdf_newcon_apur(self):
        print('3')
        tarefa = self.padrao_escolha_df()
        # tarefa = Tarefa()
        # tarefa.driver = self.driver
        # tarefa.pAL = self.pAL
        print('4')
        tarefa.xpath_present_secreen = '//*[@id="divLoading"]/img'
        tarefa.url = '//*[@id="ctl00_Conteudo_grdCotasSequenciaLance"]'  # df
        # tarefa.ultCel1 = 0  # necessario para saber se df atualizou
        # tarefa.ultCel2 = 0  # necessario para saber se df atualizou
        # tarefa.colCel1 = 1  # coluna dois para teste
        # tarefa.colCel2 = -1  # coluna ultima para teste
        # tarefa.indTx1 = 'Grupo'
        # tarefa.tag1 = 'table'
        # tarefa.tag2 = 'tr'
        # tarefa.tag3 = 'td'
        # tarefa.tagCab = 'th'
        tarefa.tempo = 5
        tarefa.ultNIndex = self.ultNIndex3
        tarefa.fator_repeticao = 3
        # tarefa.tpInicSegProg = self.tpInicSegProg
        # tarefa.g_newcon = self.g_newcon
        htmlNew, ultNIndex, ultCel1, ultCel2 = tarefa.df_newcon()
        # print('PARA 1000 $$$$$$$$$$$$$$$$$$$$$$$$$$')
        # time.sleep(1000)
        # htmlNew, ultNIndex, ultCel1, ultCel2 = Tarefa(
        #     driver=self.driver, url=url, pAL=self.pAL, ultNIndex=ultNIndex,
        #     tpInicSegProg=self.tpInicSegProg, g_newcon=self.g_newcon, tempo=tempo, ultCel1=ultCel1,
        #     ultCel2=ultCel2, colCel1=colCel1, colCel2=colCel2, indTx1=indTx1, tag1=tag1, tag2=tag2,
        #     tag3=tag3, tagCab=tagCab).df_newcon()
        return htmlNew, ultNIndex

    def presentScreen(self):
        funct = Funct()
        funct.driver = self.driver
        funct.xpath_present_secreen = '//*[@id="divLoading"]/img'
        funct.pAL = self.pAL
        funct.g_newcon = self.g_newcon
        funct.tempo = 1
        retorno = funct.funct()
        # retorno = Funct(driver=self.driver, urls=[url], faz=faz, pAL=self.pAL, g_newcon=self.g_newcon).funct()  # noqa
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
        log.pAL = self.pAL
        try:
            if self.extencao is None:
                self.df.to_csv(self.pastaArquivo, index=False, header=True)
            elif self.extencao == '.xlsx':
                # self.df.to_excel(self.pastaArquivo, index=False, header=True, float_format='%.4f', engine='openpyxl')
                self.df.to_csv(self.pastaArquivo, sep='\t', index=False, encoding='latin_1', decimal=',')  # noqa
            else:
                escreva = 'ERRO CONEXAO: Foi digitada uma extencao não especificada'
                log.escreva = escreva
                log.escrever()
                print(escreva)
        except AttributeError as e:
            escreva = f'ERRO CONEXAO: Tabela vazia, pasta: {self.pastaArquivo}. '
            escreva += f'A classe do erro: {e.__class__.__name__} '
            log.escreva = escreva
            log.escrever()
            print(escreva)
        self.zerar_variaveis()

    def dfGrupo(self):
        list_grupo = []
        for dict_df in self.df:
            # print(dict_df)
            list_grupo.append(dict_df['Grupo'])
        list_grupo = sorted(set(list_grupo))    
        return list_grupo
        # print(json.dumps(self.df, indent=4, ensure_ascii=False))

        # tratar.df2 = self.df2

        # listaGrupo, listagrupo360 = tratar.colu naGrupos()
        # # listaGrupo, listagrupo360 = Tratar(df=self.df, df2=self.df2, coluna=coluna, coluna2=coluna2).colunaGrupos()  # noqa
        # return listaGrupo, listagrupo360

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
