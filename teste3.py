from tratar import Tratar
from renomear import Renomear
import pandas as pd

pasta = ''
tabela = 'Tabelas/'
logs = 'Logs/'
arquivoLog = 'log'
extencaoLog = '.txt'
arquivoTabela = 'tabela'
arquivoTabela360 = 'tabela360'
arquivoTabelaNewcon = 'tabelaNewcon'
extencaoXlsx = '.xlsx'
extencaoCSV = '.csv'
pTabela = pasta+tabela



pastaArquivo = pTabela + 'PRODUCAO' + extencaoCSV
dfSelect = pd.read_csv(pastaArquivo, sep=',', encoding='latin_1', dtype=str)
coluna = 'Grupo'
coluna2 = 'Administradora'
listaGrupo = Tratar(df=dfSelect, coluna=coluna, coluna2=coluna2).colunaGrupoSelect()


print(listaGrupo)