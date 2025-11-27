import time
# import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tempo import Tempo
# from log import Log
from conexao import Conexao
import pandas as pd
# from tratar import Tratar
# from IPython.display import display

usuario360 = 70514852372
senha360 = '2022disal'
site360 = "https://www.disal360.com.br/Acesso/Entrar"

usuarioNewcon = '0000930798'
senhaNewcon = 'N1-a8.,t22'
siteNewcon = "https://web.disalconsorcio.com.br/"


pasta = 'Select/DISAL/'
tabela = 'Tabelas/'
logs = 'Logs/'
arquivoLog = 'log'
extencaoLog = '.txt'
arquivoTabela = 'tabela'
arquivoTabela360 = 'tabela360'
arquivoTabelaNewcon = 'tabelaNewcon'
extencaoTabela = '.xlsx'
datahora = Tempo().tempo_arquivo()
pTabela = pasta+tabela
plog = pasta+logs
pAL = plog + arquivoLog + datahora + extencaoLog
pAT360 = pTabela + arquivoTabela360 + extencaoTabela
pATNewcon = pTabela + arquivoTabelaNewcon + extencaoTabela

df360 = pd.DataFrame()
dfNewcon = pd.DataFrame()

conectar = 'newcon'  # 360 ou newcon

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
if conectar == '360':
    driver.get(site360)
    Conexao(driver=driver, usuario=usuario360, senha=senha360).logar360()
    navegou = Conexao(driver=driver).navegar360()
    # print(navegou)
elif conectar == 'newcon':
    gNewcon = '3162'
    driver.get(siteNewcon)
    Conexao(driver=driver, usuario=usuarioNewcon, senha=senhaNewcon).logarNewcon()
    Conexao(driver=driver, gNewcon=gNewcon).navegarNewcon()

time.sleep(1000)


driver.close()
