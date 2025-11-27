import time
# import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tempo import Tempo
from log import Log
from conexao import Conexao
import pandas as pd
from tratar import Tratar
# from IPython.display import display
usuario360 = 70514852372
senha360 = '2022disal'
site360 = "https://www.disal360.com.br/Acesso/Entrar"
usuarioNewcon = '0000930798'
senhaNewcon = 'NaT@!2i-'
siteNewcon = "https://web.disalconsorcio.com.br/"
pasta = 'Select/DISAL/'
tabela = 'Tabelas/'
logs = 'Logs/'
arquivoLog = 'log'
extencaoLog = '.txt'
arquivoTabela = 'tabela'
arquivoTabela360 = 'tabela360'
arquivoTabelaNewcon = 'tabelaNewcon'
extencaoXlsx = '.xlsx'
extencaoCSV = '.csv'
datahora = Tempo().tempo_arquivo()
pTabela = pasta+tabela
plog = pasta+logs
pAL = plog + arquivoLog + datahora + extencaoLog
df360 = pd.DataFrame()
dfNewcon = pd.DataFrame()
dfNewconDesistente = pd.DataFrame()
pular360 = False
pularNewcon = False
pular360 = True
pularNewcon = True
for x in range(1):
    escreva = time.strftime("%H:%M:%S") + '   ' + str(x)
    Log(escreva=escreva, pAL=pAL).escrever()
    tpInicSegProg = Tempo().tempo_execucao()
    txt = 'inicio'  # saber qual o texto selecionar no primeiro for
    ultNIndex = 0  # o número do index para quando sair do drivr nao se perder
    tab360 = 1
    quantTab360 = 1
    quantTab360 = 1000000000
    ap = '360'
    if pular360 is True:
        pastaArquivo = pTabela + arquivoTabela + ap + 'Bruto' + extencaoCSV
        df360 = pd.read_csv(pastaArquivo, sep=',', encoding='latin_1', dtype=str)
    else:
        while True:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver.get(site360)
            Conexao(driver=driver, usuario=usuario360, senha=senha360).logar360()
            navegou = Conexao(driver=driver).navegar360()
            if navegou is True:
                txt, html, ultNIndex, dfConst = Conexao(driver=driver, tpInicSegProg=tpInicSegProg, pAL=pAL, txt=txt, ultNIndex=ultNIndex).escolherDf360()
                if dfConst is not False:
                    df360 = pd.concat([df360, dfConst])
            driver.close()
            if txt == html:
                break
            if tab360 == quantTab360:  # ira parar em N números planho vezes
                break
            tab360 += 1
        df = df360
        df = Tratar(df=df).dfColunaALterarNome()
        pastaArquivo = pTabela + arquivoTabela + ap + 'Bruto' + extencaoCSV
        Conexao(df=df, pastaArquivo=pastaArquivo).gravar()
        df360 = df
    df = df360
    df = Conexao(df=df).tratarDf360()
    pastaArquivo = pTabela + arquivoTabela + ap + 'Tratar' + extencaoCSV
    Conexao(df=df, pastaArquivo=pastaArquivo).gravar()
    df360 = df
    ap = 'Newcon'
    desistente = 'Desistente'
    if pularNewcon is True:
        pastaArquivo = pTabela + arquivoTabela + ap + 'Bruto' + extencaoCSV
        dfNewcon = pd.read_csv(pastaArquivo, sep=',', encoding='latin_1', dtype=str)
        pastaArquivo = pTabela + arquivoTabela + ap + desistente + 'Bruto' + extencaoCSV
        dfNewconDesistente = pd.read_csv(pastaArquivo, sep=',', encoding='latin_1', dtype=str)
    else:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(siteNewcon)
        Conexao(driver=driver, usuario=usuarioNewcon, senha=senhaNewcon).logarNewcon()
        ultNIndex = 0
        ultNIndex2 = 0
        coluna = 'Grupo'
        listaGrupo365 = Tratar(df=df360, coluna=coluna).dfColunaExcluirRepetida()
        for gNewcon in listaGrupo365:
            gNewcon = str(gNewcon)
            Conexao(driver=driver, gNewcon=gNewcon, pAL=pAL).navegarNewcon()  # até a primeira tabela
            for x in range(3):
                dfConst, ultNIndex = Conexao(driver=driver, gNewcon=gNewcon, tpInicSegProg=tpInicSegProg, ultNIndex=ultNIndex, pAL=pAL).escolherDfNewcon()
                if dfConst is not False:
                    dfNewcon = pd.concat([dfNewcon, dfConst])
                Conexao(driver=driver).navegarNewcon2()  # até a segunda tabela quem deu lances apos 
                dfConst2, ultNIndex2 = Conexao(driver=driver, gNewcon=gNewcon, tpInicSegProg=tpInicSegProg, ultNIndex2=ultNIndex2, pAL=pAL).escolherdfNewconDesistente()
                if dfConst2 is not False:
                    dfNewconDesistente = pd.concat([dfNewconDesistente, dfConst2])
                Conexao(driver=driver).navegarNewcon1()  # retorna par primeira e pegar mes anterior 
        driver.close()
        df = dfNewcon
        df = Tratar(df=df).dfColunaALterarNome()
        pastaArquivo = pTabela + arquivoTabela + ap + 'Bruto' + extencaoCSV
        Conexao(df=df, pastaArquivo=pastaArquivo).gravar()
        dfNewcon = df
        df = dfNewconDesistente
        df = Tratar(df=df).dfColunaALterarNome()
        pastaArquivo = pTabela + arquivoTabela + ap + desistente + 'Bruto' + extencaoCSV
        Conexao(df=df, pastaArquivo=pastaArquivo).gravar()
        dfNewconDesistente = df
    df = dfNewcon
    df = Conexao(df=df).tratarDfNewcon()
    pastaArquivo = pTabela + arquivoTabela + ap + 'Tratar' + extencaoCSV
    Conexao(df=df, pastaArquivo=pastaArquivo).gravar()
    df = dfNewconDesistente
    # df = Conexao(df=df).dfNewconDesistente()
    pastaArquivo = pTabela + arquivoTabela + ap + desistente + 'Tratar' + extencaoCSV
    Conexao(df=df, pastaArquivo=pastaArquivo).gravar()
    df = pd.merge(dfNewcon, df360, on='Grupo')
    pastaArquivo = pTabela + arquivoTabela + extencaoXlsx
    Conexao(df=df, pastaArquivo=pastaArquivo, extencao=extencaoXlsx).gravar()
    escreva = 'todo programa.'  # informação do log
    Tempo(tpInicSeg=tpInicSegProg, tpInicSegProg=tpInicSegProg, escreva=escreva,  pAL=pAL).tempo_execucao()
    escreva = time.strftime("%H:%M:%S")
    Log(escreva=escreva, pAL=pAL).escrever()