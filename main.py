# flake8: noqa
# pyright: reportCallIssue=false
# pyright: reportArgumentType=false
# pyright: # type: ignore

# # erro corrigido com comando:
# # python -m pip install webdriver-manager --upgrade
# # python -m pip install packaging

from ast import Return
from tarfile import DEFAULT_FORMAT
import time
import sys
import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tempo import Tempo
from log import Log
from conexao import Conexao
import pandas as pd
from tratar import Tratar
from renomear import Renomear
from var import *
from chromeDriverauto  import ChromeDriverAuto

# from IPython.display import display

conexao = Conexao()
log = Log()
tempo = Tempo()
renomear = Renomear()
tratar = Tratar()
chrome = ChromeDriverAuto()


datahora = tempo.tempo_arq()
pAL = p_log + arq_log + datahora + ext_Log

conexao.pAL = pAL
log.pAL = pAL
tempo.pAL = pAL

# LER ARQUIVOS
file_arq = p_df + arq_df + 'Select' + ext_CSV
dfSelect = pd.read_csv(file_arq, sep=',', encoding='latin_1', dtype=str)

# file_arq = p_df + 'PRODUCAO' + ext_CSV
# dfSelect = pd.read_csv(file_arq, sep=',', encoding='latin_1', dtype=str)

file_arq = p_df + 'PRODUCAO' + ext_CSV
dfSelect = pd.read_csv(file_arq, sep=',', encoding='latin_1', dtype=str)

################################ SITE ######################################





################################ Funct ######################################

def log_tempo_programa():
    escreva = time.strftime("%H:%M:%S") + '   ' + str(x)
    log.escreva = escreva
    log.escrever()

def gravar(df, arq):
    conexao.df = df
    conexao.file_arq = arq
    conexao.gravar()

##################################### clickvenda ###################################




##################################### 360 ###################################

# def logar_360():
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#     driver.get(site360)
#     conexao.driver = driver
#     conexao.user = user360
#     conexao.password = senha360
#     conexao.logar360()
#     return driver


# def control_remoto_360():
#     df360 = pd.DataFrame()
#     html1Anterior = []
#     html2Anterior = []
#     ultNIndex360 = 0  # o número do index para quando sair do driver nao se perder
#     nTab360 = 1
#     ap = '360'
#     if pular360 is True:
#         df360 = pd.read_csv(arq_360, sep=',', encoding='latin_1', dtype=str)
#     else:
#         logar = True
#         count_loop = 0
#         while True:
#             if logar:
#                 driver = logar_360()
#                 logar = False
#                 conexao.driver = driver
#             navegou = conexao.navegar360()
#             if navegou is True:
#                 conexao.tpInicSegProg = tpInicSegProg
#                 conexao.ultNIndex360 = ultNIndex360
#                 conexao.html1Anterior = html1Anterior
#                 conexao.html2Anterior = html2Anterior
#                 ultimoPlano, html1Anterior, html2Anterior, ultNIndex, dfConst = conexao.escolherDf360()
#                 if isinstance(dfConst, pd.DataFrame):
#                     ultNIndex360 = ultNIndex
#                     df360 = pd.concat([df360, dfConst])
#                 elif dfConst == 'ERROR':
#                     count_loop += 1
#                     if count_loop >= 2:
#                         driver.close()
#                         logar = True
#                         continue
#                     print('MAIN ERROR: Foi tentado 2 vezes pegar tabeal do 360.')
#             driver.close()
#             logar = True
#             if ultimoPlano is True and html2Anterior == []:
#                 break
#             if nTab360Infinuto is not True:  # para pegar apenas algumas dfs iniciais
#                 if nTab360 >= nMaximoTab360:  # ira parar em N números planho vezes
#                     break
#                 nTab360 += 1
#         tratar.df = df360
#         df360 = tratar.dfColunaALterarNome()
#         gravar(df360, arq_360)
#     # é necessario fazer o tratamento do df360 neste momento para pegar os grupos
#     conexao.df = df360
#     df360 = conexao.tratarDf360()
#     gravar(df360, arq_360_tratadas)

#     return df360

############################# newcon #########################################


# def logar_newcon():
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#     driver.get(site_newcon)
#     conexao.driver = driver
#     conexao.user = usuario_newcon
#     conexao.password = senha_newcon
#     conexao.logar_newcon()
#     return driver


def alterar_nome_coluna_gravar(df, arq):
    # tratar = Tratar()
    tratar.df = df
    df = tratar.dfColunaALterarNome()
    # df = Tratar(df=df).dfColunaALterarNome()
    gravar(df, arq)
    return df


def alterar_dados_info_gravar(df, arq):
    # tratar = Tratar()
    tratar.df = df
    tratar.coluna = 'Grupo'
    df = tratar.dfColunaStrInt()
    gravar(df, arq)
    return df


def reverificar_erro_newcon(driver, logar, count_loop, g_newcon):
    stop_loop = False
    if logar is False:
        text = f'MAIN OBS: {count_loop}ª tentativa do grupo {g_newcon}, já foi. \n'
        print(text)
        driver.close()
        logar = True
        if count_loop >= 10:
            stop_loop = True
    return logar, stop_loop





def criar_df_atravas_lista_info(list_table):
    # criar df atraves da lista
    df_newcon_info = pd.DataFrame()
    tratar.df = df_newcon_info
    df = tratar.dfColunaIndexNumeroLinha()
    # df = Tratar(df=df).dfColunaIndexNumeroLinha()
    colunas = ['Grupo', 'Prazo', 'Realizada', 'ARealizar', 'Prox_Assembleia', 'VencimentoNew']
    for coluna in colunas:
        tratar.df = df
        tratar.coluna = coluna
        df = tratar.dfColunaCriarVazia()
        # df = Tratar(df=df, coluna=coluna).dfColunaCriarVazia()
    numeroLinha = 0  # reutilizar variavel
    for lista in list_table:
        tratar.df = df
        tratar.colunas = colunas
        tratar.lista = lista
        tratar.numeroLinha = numeroLinha
        df = tratar.dfColunaLinhas()
        # df = Tratar(df=df, colunas=colunas, lista=lista,
        #             numeroLinha=numeroLinha).dfColunaLinhas()
        numeroLinha += 1
    gravar(df, arq_info)
    return df


def df_conf(ultNIndex1):
    self.stop_error = False
    dfConst1 = pd.DataFrame()
    conexao.navegar_newcon_df()
    conexao.tpInicSegProg = tpInicSegProg
    conexao.ultNIndex1 = ultNIndex1
    dfConst1, ultNIndex = conexao.escolherDf_newcon()  # copiar df
    if isinstance(dfConst1, pd.DataFrame):
        ultNIndex1 = ultNIndex
    elif dfConst1 == 'VAZIO':
        dfConst1 = pd.DataFrame()
    elif dfConst1 == 'ERROR':
        self.stop_error = True
    if isinstance(dfConst1, list):
        dfConst1 = pd.DataFrame(dfConst1)
    return ultNIndex1, dfConst1, self.stop_error


def df_desc(ultNIndex2):
    self.stop_error = False
    dfConst2 = pd.DataFrame()
    conexao.navegar_newcon_desc()
    dfConst2 = pd.DataFrame()
    conexao.ultNIndex2 = ultNIndex2
    dfConst2, ultNIndex = conexao.escolher_df_newcon_desc()
    if isinstance(dfConst2, pd.DataFrame):
        ultNIndex2 = ultNIndex
    elif dfConst2 == 'VAZIO':
        dfConst2 = pd.DataFrame()
    elif dfConst2 == 'ERROR':
        self.stop_error = True
    if isinstance(dfConst2, list):
        dfConst2 = pd.DataFrame(dfConst2)
    return ultNIndex2, dfConst2, self.stop_error


def df_apur(ultNIndex3):
    existeApuracao = conexao.navegar_newcon_sequencia_apur()
    self.stop_error = False
    dfConst3 = pd.DataFrame()
    if existeApuracao:
        conexao.tpInicSegProg = tpInicSegProg
        conexao.ultNIndex3 = ultNIndex3
        dfConst3, ultNIndex = conexao.escolherdf_newcon_apur()
        if isinstance(dfConst3, pd.DataFrame):
            ultNIndex3 = ultNIndex
        elif dfConst3 == 'VAZIO':
            dfConst3 = pd.DataFrame()
        elif dfConst3 == 'ERROR':
            self.stop_error = True
    elif existeApuracao == 'ERROR':
        self.stop_error = True
    if isinstance(dfConst3, list):
        dfConst3 = pd.DataFrame(dfConst3)
    return ultNIndex3, dfConst3, self.stop_error


class Clickvenda:
    def __init__(self, *args, **kwargs):
        pass

    def control_remote_clickvenda(self):
        if not jump_clickvenda:
            for _ in range(5):
                conexao.driver = chrome.site_open(info_clickvenda)
                getattr(conexao, info_clickvenda['log'])(info_clickvenda, path_clickvenda)
                getattr(conexao, info_clickvenda['navegate_start'])()
                if getattr(conexao, info_clickvenda['navegate'])():
                    break
        return getattr(conexao, info_clickvenda['read'])(arq_clickvenda)
    

class Newcon:
    def __init__(self, *args, **kwargs):
        self.driver = None
        self.stop_error = False
        self.list_table = []
        self.list_grupo = []


    def control_remoto_newcon(self, df_clickvenda):
        # LISTA DE GRUPO
        conexao.df = df_clickvenda
        # conexao.df2 = dfSelect
        if jump_newcon_full:
            df_newcon_info = pd.read_csv(arq_info, sep=',', encoding='latin_1', dtype=str)  # noqa
            df_newcon_conf = pd.read_csv(arq_conf, sep=',', encoding='latin_1', dtype=str)  # noqa
            df_newcon_desc = pd.read_csv(arq_desc, sep=',', encoding='latin_1', dtype=str)  # noqa
            df_newcon_apur = pd.read_csv(arq_apur, sep=',', encoding='latin_1', dtype=str)
        else:
            self.list_grupo = conexao.dfGrupo()
            df_newcon_info, df_newcon_conf, df_newcon_desc, df_newcon_apur = self.control_remoto_newcon_full()  # noqa
        sys.exit()
        if jump_newcon_info:
            df_newcon_info = pd.read_csv(arq_info, sep=',', encoding='latin_1', dtype=str)  # noqa
        if jump_newcon_conf:
            df_newcon_conf = pd.read_csv(arq_conf, sep=',', encoding='latin_1', dtype=str)  # noqa
        if jump_newcon_desc:
            df_newcon_desc = pd.read_csv(arq_desc, sep=',', encoding='latin_1', dtype=str)  # noqa
        if jump_newcon_apur:
            df_newcon_apur = pd.read_csv(arq_apur, sep=',', encoding='latin_1', dtype=str)

        df_newcon_conf = alterar_nome_coluna_gravar(df_newcon_conf, arq_conf)
        df_newcon_desc = alterar_nome_coluna_gravar(df_newcon_desc, arq_desc)  # noqa
        df_newcon_apur = alterar_nome_coluna_gravar(df_newcon_apur, arq_apur)

        return df_newcon_conf, df_newcon_desc, df_newcon_apur, df_newcon_info, listaGrupo360
    
    def navegar_newcon_contemplacao_padrao(self, g_newcon):
        conexao.driver = self.driver
        conexao.g_newcon = g_newcon
        conexao.navegar_newcon_contemplacao()  # navega até a df g_newcon


    def list_info(self):
        self.stop_error = False
        conexao.tpInicSegProg = tpInicSegProg
        # conexao.ultNIndex4 = ultNIndex4
        lista = conexao.info_newcon()
        if lista == 'ERROR':
            self.stop_error = True
        self.list_table.append(lista)
        return


    def control_remoto_newcon_full(self):
        df_newcon_conf = pd.DataFrame()
        df_newcon_desc = pd.DataFrame()
        df_newcon_apur: pd.DataFrame = pd.DataFrame()
        ultNIndex1 = 0
        ultNIndex2 = 0
        ultNIndex3 = 0
        ultNIndex4 = 0
        self.list_table = []
        logar = True
        self.stop_error = False
        # driver = logar_newcon()
        for g_newcon in self.list_grupo:
            g_newcon = str(g_newcon)
            g_newcon_int = int(g_newcon)
            if g_newcon_int <= 2953:
                continue 
            if g_newcon_int <= menor_g_newcon or g_newcon_int >= maior_g_newcon:
                continue
            renomear.inf = g_newcon
            inf = renomear.vazio()
            # inf = Renomear(inf=g_newcon).vazio()
            if inf == '':
                continue
            stopError_full = False

            get_info = not jump_newcon_info
            get_conf = not jump_newcon_conf
            get_desc = not jump_newcon_desc
            get_apur = not jump_newcon_apur

            count_loop_full = 0
            loop = 0

            
            while True:
                print(f'inicio: {g_newcon}')
                
                if stopError_full:
                    logar, stop_loop = reverificar_erro_newcon(driver, logar, count_loop_full, g_newcon)  # noqa
                    if stop_loop:
                        break
                    stopError_full = False
                # else:
                #     self.stop_error = conexao.presentScreen()


                count_loop_full += 1
                if logar:
                    self.driver = chrome.site_open(info_newcon)
                    conexao.driver = self.driver
                    getattr(conexao, info_newcon['log'])(info_newcon, path_newcon)
                    logar = False


                if get_info:
                    if loop >= 2:  # desistir de baixa df
                        get_info = False
                    else:
                        loop += 1
                        self.navegar_newcon_contemplacao_padrao(g_newcon)
                        self.list_info()
                        # time.sleep(10)
                        sys.exit()

                        if self.stop_error:  # error tela travada
                            stopError_full = True
                            continue
                        else:  # df baixada
                            get_info = False

                if get_conf:
                    print(conf)
                    if loop_conf >= 2:  # desistir de baixa df
                        get_conf = False
                    else:
                        loop_conf += 1
                        self.navegar_newcon_contemplacao_padrao(driver, g_newcon)
                        for x in range(mesQuantidade):  # quantidade de meses anteriores
                            ultNIndex1, dfConst1, self.stop_error = df_conf(ultNIndex1)  # noqa
                            if self.stop_error:
                                break
                            if not dfConst1.empty:
                                df_newcon_conf = pd.concat([df_newcon_conf, dfConst1])  # noqa
                            conexao.navegar_newcon_retorna_assembleia()  # mes anaterior
                        if self.stop_error:  # error tela travada
                            stopError_full = True
                            continue
                        else:  # df baixada
                            get_conf = False

                if get_desc:
                    print(desc)
                    if loop_desc >= 2:  # desistir de baixa df
                        get_desc = False
                    else:
                        loop_desc += 1
                        self.navegar_newcon_contemplacao_padrao(driver, g_newcon)
                        for x in range(mesQuantidade):  # quantidade de meses anteriores
                            ultNIndex2, dfConst2, self.stop_error = df_desc(ultNIndex2)  # noqa
                            if self.stop_error:
                                break
                            if not dfConst2.empty:
                                df_newcon_desc = pd.concat([df_newcon_desc, dfConst2])  # noqa
                            conexao.navegar_newcon_retorna_assembleia()  # mes anaterior
                        if self.stop_error:
                            stopError_full = True
                            continue
                        else:  # df baixada
                            get_desc = False

                if get_apur:
                    print(apur)
                    if loop_apur >= 2:  # desistir de baixa df
                        get_apur = False
                    else:
                        loop_apur += 1
                        self.navegar_newcon_contemplacao_padrao(driver, g_newcon)
                        ultNIndex3, dfConst3, self.stop_error = df_apur(ultNIndex3)
                        if self.stop_error:  # error tela travada
                            stopError_full = True
                            continue
                        else:  # df baixada
                            if not dfConst3.empty:
                                df_newcon_apur = pd.concat([df_newcon_apur, dfConst3])
                            get_apur = False

                if count_loop_full >= 2:
                    text = f'A {count_loop_full}º tentativa foi bem sucedida:   '
                    text += f'{stopError_full}. \n Comprovando que existe sentido na '
                    text += f'segunda tentativa. grupo: {g_newcon}'
                    print(text)
                    break
                    # sys.exit()

                if not get_info and not get_conf and not get_desc and not get_apur:  # noqa
                    print(f'fim: {g_newcon} \n')
                    break

        if not logar:
            driver.close()
        df_newcon_info = criar_df_atravas_lista_info(self.list_table)
        return df_newcon_info, df_newcon_conf, df_newcon_desc, df_newcon_apur

##################### TRATAR E JUNTAR DE TABELAS #############################


def tratar_gravar(df, arq, ap):
    conexao.ap = ap
    conexao.df = df
    df = conexao.tratarDf_newcon()
    gravar(df, arq)
    return df


def editar_dados_360(df, df_newcon_info):
    df360New = pd.DataFrame()
    conexao.df = df360New
    conexao.df360 = df
    conexao.df_newcon_info = df_newcon_info
    df = conexao.gravarDf360()
    return df


# INICIO DO PROGRAMA:

clickvenda = Clickvenda()
newcon = Newcon()

for x in range(1):
    log_tempo_programa()
    tpInicSegProg = tempo.tempo_execucao()
    df_clickvenda = clickvenda.control_remote_clickvenda() 
    df_newcon_conf, df_newcon_desc, df_newcon_apur, df_newcon_info, listaGrupo360 = newcon.control_remoto_newcon(df_clickvenda)  # noqa
    sys.exit()
###########################
    df_newcon_conf = tratar_gravar(df_newcon_conf, arq_conf_tratadas, conf)  # noqa

    df_newcon_desc = tratar_gravar(df_newcon_desc, arq_desc_tratadas, desc)  # noqa

    df_newcon_apur = tratar_gravar(df_newcon_apur, arq_apur_tratadas, apur)

    df_newcon_info = alterar_dados_info_gravar(df_newcon_info, arq_info_tratadas)  # noqa

    df360New = editar_dados_360(df360, df_newcon_info)

    df = pd.merge(df360, df360New, how='outer')

    conexao.df = df
    df = conexao.dfConverterStr()

    df = pd.merge(df_newcon_conf, df, on='Grupo')

    df = pd.merge(df, df_newcon_desc, how='outer')

    df = pd.merge(df, df_newcon_apur, how='outer')

    conexao.df = df
    conexao.listaGrupo360 = listaGrupo360
    df = conexao.dfMesclaOrganizar()

    df2 = df
    df = pd.merge(df, df_newcon_info, on='Grupo')

    tratar.df = df
    df = tratar.dfColunaOrganizar()

    conexao.ext_ = ext_Xlsx
    gravar(df, arq_df_xlsx)

    gravar(df, arq_df_csv)

    conexao.df = df2
    df = conexao.tratarDfFixar()
    df = pd.merge(df, df_newcon_info, on='Grupo')
    tratar.df = df
    df = tratar.dfColunaOrganizar()

    conexao.ext_ = ext_Xlsx
    gravar(df, arq_df_2_xlsx)

    gravar(df, arq_df_2_csv)

    ###########################
    escreva = 'fim'  # informação do log
    tempo.tpInicSeg = tpInicSegProg
    tempo.tpInicSegProg = tpInicSegProg
    tempo.escreva = escreva
    tempo.tempo_execucao()
    # Tempo(tpInicSeg=tpInicSegProg, tpInicSegProg=tpInicSegProg, escreva=escreva).tempo_execucao()  # noqa
    escreva = time.strftime("%H:%M:%S")
    log.escreva = escreva
    log.escrever()
