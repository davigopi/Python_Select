# flake8: noqa
# pyright: # type: ignore

# # Para executar o if __name__ == '__main__':
from IPython.display import display
import pandas as pd
from bs4 import BeautifulSoup  # Analisar documentos HTML e XML
import urllib.request  # importar a biblioteca que usamos para abrir URLs
import re
# import unicodedata
import sys
# from tratar import Tratar
from renomear import Renomear
# from Select.DISAL import renomear


class DfSite:
    def __init__(self, *args, _zero=0, _semValor=None, **kwargs):
        self.html = kwargs.get('html')
        self.colunaIndex = kwargs.get('colunaIndex')
        self.ultNIndex = kwargs.get('ultNIndex')
        self.numColuna = _zero
        self.numLinha = _zero
        self.url = kwargs.get('url')
        self.celula = _semValor
        self.inf = _semValor
        self.tabelaNew = _semValor
        self.celulaNumero = _zero
        self.cont = _zero
        self.texto1 = kwargs.get('texto1')
        self.texto2 = kwargs.get('texto2')
        self.texto3 = kwargs.get('texto3')
        self.indTx1 = kwargs.get('indTx1')
        self.indTx2 = kwargs.get('indTx2')
        self.indTx3 = kwargs.get('indTx3')
        self.indTx4 = kwargs.get('indTx4')
        self.tag1 = kwargs.get('tag1')
        self.tag2 = kwargs.get('tag2')
        self.tag3 = kwargs.get('tag3')
        self.tagCab = kwargs.get('tagCab')
        self.tratarModelo = kwargs.get('tratarModelo')
        self.dfInf = False
        self.erro = ''

    def zera_variaveis(self):
        self.tag2 = None
        self.tag3 = None
        self.tagCab = None
        self.ultNIndex = None
        self.html = None
        self.url = None
        self.texto1 = None
        self.texto2 = None
        self.texto3 = None
        self.tratarModelo = None

    def tabela(self):
        def informacaoCelula(*args, **kwargs):
            try:
                self.inf = self.celula[self.cont].find(text=True)
                az[self.cont].append(self.inf)
                self.dfInf = True
            except (IndexError, AttributeError) as e:
                self.numColuna = self.cont
                self.cont = 25
                self.erro = e.__class__.__name__

        A = []
        B = []
        C = []
        D = []
        E = []
        F = []
        G = []
        H = []
        # I = []
        J = []
        K = []
        L = []
        M = []
        N = []
        # O = []
        P = []
        Q = []
        R = []
        S = []
        T = []
        U = []
        V = []
        W = []
        X = []
        Y = []
        Z = []
        az = [A, B, C, D, E, F, G, H, J, K, L, M, N, P, Q, R, S, T, U,
              V, W, X, Y, Z]  # 24 letras o I e O fica acusando duplicidade
        lista = []

        if self.ultNIndex is None:
            self.ultNIndex = 0
        else:
            self.ultNIndex = int(self.ultNIndex)

        try:  # se foi definido html ou url e der erro, o valor não foi carregaod
            # definir se foi enviado uma pagui html ou apenas uma URL
            if self.html is not None:  # se for por HTML
                tabela_simples = BeautifulSoup(self.html, "lxml").find(self.tag1)
            elif self.url is not None:  # se for por URL
                # tabela_todas = BeautifulSoup(urllib.request.urlopen(self.url), "lxml").find_all(self.tag1)
                tabela_simples = BeautifulSoup(urllib.request.urlopen(self.url), "lxml").find('table', class_='wikitable sortable')  # noqa
            else:
                print(f'DFSITE OBS: HTML: ({self.html}) | URL: ({self.url})')
                sys.exit()
        except (ValueError, TypeError) as e:
            return 'ERROR'

        # descobrir a quantidade de celulas colunas
        if self.tagCab is not None:
            # para tudo que estiver em <th>
            for nomeColuna in tabela_simples.findAll(self.tagCab):
                self.celulaNumero += 1

        if self.tag2 is not None:
            # para tudo que estiver em <tr>
            for linha in tabela_simples.findAll(self.tag2):
                self.numLinha += 1
                if self.tag3 is not None:
                    # variável para encontrar <td>
                    self.celula = linha.findAll(self.tag3)
                    if len(self.celula) == self.celulaNumero:  # número de colunas
                        self.cont = 0
                        while True:
                            informacaoCelula()
                            if self.cont >= 25:
                                break
                            self.cont += 1
                else:
                    self.inf = linha.find(text=True)
                    lista.append(self.inf)
                    self.dfInf = True

        if self.dfInf is True:
            if self.tag3 is not None:
                if self.tagCab is not None:
                    # print(f"self.numLinha: {self.numLinha}, type: {type(self.numLinha)}")
                    # print(f"self.ultNIndex: {self.ultNIndex}, type: {type(self.ultNIndex)}")
                    if self.ultNIndex is None:
                        self.ultNIndex = 0
                    else:
                        self.ultNIndex = int(self.ultNIndex)
                    self.numLinha += self.ultNIndex
                    self.ultNIndex += 1
                    while self.numLinha > self.ultNIndex:  # Inserir uma coluna de INDEX + OUTRAS
                        az[self.numColuna].append(self.ultNIndex)
                        self.ultNIndex += 1
                        if self.texto1 is not None:
                            az[(self.numColuna + 1)].append(self.texto1)
                        if self.texto2 is not None:
                            az[(self.numColuna + 2)].append(self.texto2)
                        if self.texto3 is not None and self.tratarModelo is not True:
                            self.texto3 = Renomear(inf=self.texto3).modelo()
                            az[(self.numColuna + 3)].append(self.texto3)
                        if self.tratarModelo is True:
                            self.texto3 = Renomear(inf=self.texto3).modelo()
                            text3, text4 = Renomear(inf=self.texto3).edit_Texto3()
                            az[(self.numColuna + 3)].append(text3)  # nome do modelo
                            az[(self.numColuna + 4)].append(text4)  # valor apresentado apos -

                    nomeColuna = 'Index'
                    self.tabelaNew = pd.DataFrame(index=az[self.numColuna], columns=[nomeColuna])
                    self.tabelaNew[nomeColuna] = az[self.numColuna]
                    if self.texto1 is not None:
                        self.tabelaNew[self.indTx1] = az[(self.numColuna + 1)]

                    if self.texto2 is not None:
                        self.tabelaNew[self.indTx2] = az[(self.numColuna + 2)]

                    if self.texto3 is not None:
                        self.tabelaNew[self.indTx3] = az[(self.numColuna + 3)]

                    if self.tratarModelo is not None:
                        self.tabelaNew[self.indTx4] = az[(self.numColuna + 4)]

                    # Colocar nome das colunas na tabela
                    # para tudo que estiver em <th>
                    cont = 0
                    for nomeColuna in tabela_simples.findAll(self.tagCab):
                        nomeColuna = re.sub('\n', '', re.sub('  ', '', nomeColuna.find(text=True)))
                        try:
                            self.tabelaNew[nomeColuna] = az[cont]

                        except ValueError as e:
                            self.erro = e.__class__.__name__
                        cont += 1

            elif self.tag2 is not None:
                del (lista[0:1])  # remver cabeçalho
                self.tabelaNew = lista
            else:
                self.tabelaNew = tabela_simples
        else:
            self.tabelaNew = pd.DataFrame()

        self.zera_variaveis()
        return self.tabelaNew


if __name__ == '__main__':
    url = 'https://pt.wikipedia.org/wiki/Lista_de_capitais_do_Brasil_por_%C3%A1rea'
    tag1 = 'table'
    tag2 = 'tr'
    tag3 = 'td'
    tagCab = 'th'
    ultNIndex = 1000
    tabela_fim = DfSite(
        url=url,
        colunaIndex=2,
        tag1=tag1,
        tag2=tag2,
        tag3=tag3,
        tagCab=tagCab,
        ultNIndex=ultNIndex).tabela()
    display(tabela_fim)
