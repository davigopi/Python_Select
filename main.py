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
from convert import Convert



# from IPython.display import display

conexao = Conexao()
log = Log()
tempo = Tempo()
renomear = Renomear()
tratar = Tratar()
chromeDriverAuto = ChromeDriverAuto()
convert = Convert()


datahora = tempo.tempo_arq()
path_all_log = p_log + arq_log + datahora + ext_Log

conexao.path_all_log = path_all_log
log.path_all_log = path_all_log
tempo.path_all_log = path_all_log

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
    write_log = time.strftime("%H:%M:%S") + '   ' + str(x)
    log.write_log = write_log
    log.escrever()

def gravar(df, arq):
    conexao.df = df
    conexao.file_arq = arq
    conexao.gravar()

def juntar(json_base, json_novo):
    return json_base + (json_novo or [])

def join_disc_list_and_disc_info(disc_info, list_json):
    new_list_json = []
    for temp_json in list_json:
        new_json = disc_info.copy()
        if isinstance(new_json, list):
            new_json = new_json[0]
        for key, value in temp_json.items():
            if key not in new_json:
                new_json[key] = value
        new_list_json.append(new_json)
    return new_list_json

##################################### clickvenda ###################################




##################################### 360 ###################################

# def logar_360():
#     driver = webdriver.chromeDriverAuto(service=Service(ChromeDriverManager().install()), options=options)
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
#         count_loop_all = 0
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
#                     count_loop_all += 1
#                     if count_loop_all >= 2:
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
#     driver = webdriver.chromeDriverAuto(service=Service(ChromeDriverManager().install()), options=options)
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



# def df_apur(ultNIndex3):
#     existeApuracao = conexao.navegar_newcon_sequencia_apur()
#     self.stop_error = False
#     dfConst3 = pd.DataFrame()
#     if existeApuracao:
#         conexao.tpInicSegProg = tpInicSegProg
#         conexao.ultNIndex3 = ultNIndex3
#         dfConst3, ultNIndex = conexao.escolherdf_newcon_apur()
#         if isinstance(dfConst3, pd.DataFrame):
#             ultNIndex3 = ultNIndex
#         elif dfConst3 == 'VAZIO':
#             dfConst3 = pd.DataFrame()
#         elif dfConst3 == 'ERROR':
#             self.stop_error = True
#     elif existeApuracao == 'ERROR':
#         self.stop_error = True
#     if isinstance(dfConst3, list):
#         dfConst3 = pd.DataFrame(dfConst3)
#     return ultNIndex3, dfConst3, self.stop_error


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
        return getattr(conexao, info_clickvenda['read'])(arq_clickvenda)
    

class Newcon:
    def __init__(self, *args, **kwargs):
        self.driver = None
        self.list_info = []
        self.disc_info = {}
        # self.disc_line_equal = {}
        self.list_grupo = []
        self.count_loop_all = 0
        self.count_loop_single = 0
        self.grupo_newcon = 0

    # def control_remoto_newcon(self, df_clickvenda):
    #     # LISTA DE GRUPO
    #     conexao.df = df_clickvenda
    #     # conexao.df2 = dfSelect
    #     if jump_newcon_full:
    #         df_newcon_info = pd.read_csv(arq_info, sep=',', encoding='latin_1', dtype=str)  # noqa
    #         df_newcon_conf = pd.read_csv(arq_conf, sep=',', encoding='latin_1', dtype=str)  # noqa
    #         df_newcon_desc = pd.read_csv(arq_desc, sep=',', encoding='latin_1', dtype=str)  # noqa
    #         df_newcon_apur = pd.read_csv(arq_apur, sep=',', encoding='latin_1', dtype=str)
    #     else:
    #         self.control_remoto_newcon_full()
    #     return conexao.read_clickvend(arq_newcon)
    
    def navegar_newcon_contemplacao_padrao(self):

        conexao.percussion_cont_newcon()  # navega até a df self.grupo_newcon


    # def get_disc_info(self):
    #     self.stop_error = False
    #     conexao.tpInicSegProg = tpInicSegProg
    #     # conexao.ultNIndex4 = ultNIndex4
    #     self.disc_info = conexao.get_info_newcon()
    #     if self.disc_info == 'ERROR':
    #         self.stop_error = True


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
            print(f'⚠️ MAIN: loop single {self.count_loop_single}ª tentativa do grupo {self.grupo_newcon}, já foi.')
        if self.count_loop_single >= 3:
            print(f"❌ MAIN: O programa esta em um loop fatal, o grupo: {self.grupo_newcon}, foi atigido a quantidade {self.count_loop_all}ª.")
            print("❌ MAIN: Passar para o próxima tabela do grupo ou proximo grupo")
            return True
        return False


    # def reverificar_erro_newcon(self, self.grupo_newcon):
        



    # def get_df_conf(self):
    #     df_conf = pd.DataFrame()
    #     df_conf = conexao.get_conf_newcon()
    #     print(f'df_conf: {df_conf}')
    #     # conexao.tpInicSegProg = tpInicSegProg
    #     # # conexao.ultNIndex1 = ultNIndex1
    #     # df_conf, ultNIndex = conexao.escolherDf_newcon()  # copiar df
    #     # if isinstance(df_conf, pd.DataFrame):
    #     #     ultNIndex1 = ultNIndex
    #     # elif df_conf == 'VAZIO':
    #     #     df_conf = pd.DataFrame()
    #     # elif df_conf == 'ERROR':
    #     #     self.stop_error = True
    #     # if isinstance(df_conf, list):
    #     #     df_conf = pd.DataFrame(df_conf)
    #     return df_conf
    # def get_canc_newcon(self):
    #     self.stop_error = False
    #     dfConst2 = pd.DataFrame()
    #     conexao.navegar_newcon_desc()
    #     dfConst2 = pd.DataFrame()
    #     conexao.ultNIndex2 = ultNIndex2
    #     dfConst2, ultNIndex = conexao.get_canc_newcon()
    #     if isinstance(dfConst2, pd.DataFrame):
    #         ultNIndex2 = ultNIndex
    #     elif dfConst2 == 'VAZIO':
    #         dfConst2 = pd.DataFrame()
    #     elif dfConst2 == 'ERROR':
    #         self.stop_error = True
    #     if isinstance(dfConst2, list):
    #         dfConst2 = pd.DataFrame(dfConst2)
    #     return ultNIndex2, dfConst2, self.stop_error

    def control_remoto_newcon_full(self, df_clickvenda):
        if jump_newcon:
            return False
        logar = True
        disc_join_all_newcom = []
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
            get_info = True
            get_conf = True
            get_canc = True
            get_desc = True
            get_apur = True
            stop_error = False
            disc_grupo = {}
            while True:
                print(f'\n⛏️  MAIN: Início o grupo: {self.grupo_newcon}')
                if 'grupo' not in disc_grupo:
                    disc_grupo['grupo'] = self.grupo_newcon
                
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

                if get_info:
                    if self.loop_single():  # desistir de baixa df
                        break
                    else:
                        for _ in range(3):
                            conexao.percussion_cont_newcon() 
                            disc_info = conexao.get_info_newcon()
                            if not disc_info:
                                continue
                            disc_grupo.update(disc_info)
                            self.count_loop_single = 0
                            get_info = False
                            break
                        else:
                            print(f'⁉️  MAIN: O discionario de informações do grupo: {self.grupo_newcon} esta retornando vazio, já mais é para não ter as informações')
                            stop_error = True
                            continue
         
                if get_conf:
                    if self.loop_single():
                        get_conf = False
                    else:
                        list_disc_join_conf = [{'tabela': 'confirmada'}]
                        list_disc_join_conf = join_disc_list_and_disc_info(disc_grupo, list_disc_join_conf)
                        for _ in range(3):
                            conexao.percussion_cont_newcon() 
                            disc_conf = conexao.get_conf_newcon()
                            if not disc_conf:
                                continue
                            list_disc_join_conf = join_disc_list_and_disc_info(list_disc_join_conf, disc_conf)
                            self.count_loop_single = 0
                            get_conf = False
                            break
                        else:
                            print(f'⁉️  MAIN: O discionario de confirmadas do grupo: {self.grupo_newcon} esta retornando vazio, pode acontecer em poucos casos. Entrao continui.')

                if get_canc:
                    if self.loop_single():
                        get_canc = False
                    else:
                        list_disc_join_canc = [{'tabela': 'cancelada'}]
                        list_disc_join_canc = join_disc_list_and_disc_info(disc_grupo, list_disc_join_canc)
                        for _ in range(3):
                            conexao.percussion_cont_newcon() 
                            disc_canc = conexao.get_canc_newcon()
                            if not disc_canc:
                                continue
                            list_disc_join_canc = join_disc_list_and_disc_info(list_disc_join_canc, disc_canc)
                            self.count_loop_single = 0
                            get_canc = False
                            break
                        else:
                            print(f'⁉️  MAIN: O discionario de desclassificados do grupo: {self.grupo_newcon} esta retornando vazio, pode acontecer. Entrao continui.')
                            self.count_loop_single = 0
                            get_canc = False

                if get_desc:
                    if self.loop_single():
                        get_desc = False
                    else:
                        list_disc_join_desc = [{'tabela': 'desclassificada'}]
                        list_disc_join_desc = join_disc_list_and_disc_info(disc_grupo, list_disc_join_desc)
                        for _ in range(3):
                            conexao.percussion_cont_newcon() 
                            disc_desc = conexao.get_desc_newcon()
                            if not disc_desc:
                                continue
                            list_disc_join_desc = join_disc_list_and_disc_info(list_disc_join_desc, disc_desc)
                            self.count_loop_single = 0
                            get_desc = False
                            break
                        else:
                            print(f'⁉️  MAIN: O discionario de desclassificados do grupo: {self.grupo_newcon} esta retornando vazio, pode acontecer. Entrao continui.')
                            self.count_loop_single = 0
                            get_desc = False

                if get_apur:
                    if self.loop_single():
                        get_apur = False
                    else:
                        list_disc_join_apur = [{'tabela': 'apurada'}]
                        list_disc_join_apur = join_disc_list_and_disc_info(disc_grupo, list_disc_join_apur)
                        for _ in range(3):
                            conexao.percussion_cont_newcon() 
                            disc_apur = conexao.get_apur_newcon()
                            if not disc_apur:
                                continue
                            list_disc_join_apur = join_disc_list_and_disc_info(list_disc_join_apur, disc_apur)
                            self.count_loop_single = 0
                            get_apur = False
                            break
                        else:
                            print(f'⁉️  MAIN: O discionario de apurações do grupo: {self.grupo_newcon} esta retornando vazio, pode acontecer. Entrao continui.')
                            self.count_loop_single = 0
                            get_apur = False
  
                disc_join_all_newcom = disc_join_all_newcom + list_disc_join_conf + list_disc_join_canc + list_disc_join_desc + list_disc_join_apur

                if not get_info and not get_conf and not get_canc and not get_apur:  # noqa
                    break

        chromeDriverAuto.close_driver(self.driver)
        conexao.salve_clickvend(disc_join_all_newcom, arq_newcon)
        return True


    def get_arq_clickvend(self):
        try:
            disc_join_all_newcom = conexao.read_clickvend(arq_newcon)
            if isinstance(disc_join_all_newcom, list):
                print("É uma lista")
                return disc_join_all_newcom
            else:
                print(f'O arquivo {disc_join_all_newcom} que esta sendo lido não é lista, é: {type(disc_join_all_newcom)}.')
                sys.exit()
        except Exception as e:
            print(f'O arquivo {disc_join_all_newcom} não dá pra converter: {e}.')
            sys.exit()

    def organizar_newcon_full(self):
        disc_join_all_newcom = self.get_arq_clickvend()
        list_disc_no_repetition = []
        for disc in disc_join_all_newcom:
            if disc in list_disc_no_repetition:
                continue
            quantity = 1
            for disc_test_quantity in disc_join_all_newcom:
                if disc == disc_test_quantity:
                    quantity += 1
            disc['quantidades_iguais'] = str(quantity)
            list_disc_no_repetition.append(disc)
        conexao.salve_clickvend(arq_newcon_tratado, arq_newcon)


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
    newcon.control_remoto_newcon_full(df_clickvenda) 
    sys.exit()
    newcon.organizar_newcon_full()
    sys.exit()



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
    write_log = 'fim'  # informação do log
    tempo.tpInicSeg = tpInicSegProg
    tempo.tpInicSegProg = tpInicSegProg
    tempo.write_log = write_log
    tempo.tempo_execucao()
    # Tempo(tpInicSeg=tpInicSegProg, tpInicSegProg=tpInicSegProg, write_log=write_log).tempo_execucao()  # noqa
    write_log = time.strftime("%H:%M:%S")
    log.write_log = write_log
    log.escrever()
