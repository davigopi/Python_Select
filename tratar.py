# flake8: noqa
# pyright: # type: ignore

# from email.utils import collapse_rfc2231_value
# from openpyxl import NaN
import pandas as pd
from datetime import datetime
# from pkg_resources import NullProvider
from renomear import Renomear
import warnings
from datetime import date, timedelta

# import re
# import sys
# from IPython.display import display
# from traitlets import Float, Int
# import time
# import math   # math.trunc
# from bs4 import BeautifulSoup
# import bs4
# from operator import index
# from cmath import infj
# from datetime import date
# from math import nan
# import numpy as np


warnings.simplefilter(action='ignore', category=(FutureWarning, pd.errors.PerformanceWarning))

# warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)


class Tratar:
    def __init__(self, *args, **kwargs):
        self.pAT = kwargs.get('pAT')
        self.df = kwargs.get('df')
        self.df2 = kwargs.get('df2')
        self.colunas = kwargs.get('colunas')
        self.coluna = kwargs.get('coluna')
        self.coluna2 = kwargs.get('coluna2')
        self.coluna3 = kwargs.get('coluna3')
        self.coluna4 = kwargs.get('coluna4')
        self.colunaLista = kwargs.get('colunaLista')
        self.colunaNova = kwargs.get('colunaNova')
        self.colunaDtNova = kwargs.get('colunaDtNova')
        self.textoLinha = kwargs.get('textoLinha')
        self.nXRept = kwargs.get('nXRept')
        self.texto = kwargs.get('texto')
        self.nUltCol = kwargs.get('nUltCol')
        self.nUltCol2 = kwargs.get('nUltCol2')
        self.nUltCol3 = kwargs.get('nUltCol3')
        self.nUltColX = kwargs.get('nUltColX')
        self.nUltColConfm = kwargs.get('nUltColConfm')
        self.nReptMaior = kwargs.get('nReptMaior')
        self.lista = kwargs.get('lista')
        self.listaLinha = kwargs.get('listaLinha')
        self.decendente = kwargs.get('decendente')
        self.mes = kwargs.get('mes')
        self.mesmaLinha = kwargs.get('mesmaLinha')
        self.campoLista = kwargs.get('campoLista')
        self.ap = kwargs.get('ap')
        self.colunaLista = kwargs.get('colunaLista')
        self.colunaCorreta = kwargs.get('colunaCorreta')
        self.listaColunaDeslocadaConfm = kwargs.get('listaColunaDeslocadaConfm')
        self.listaColunaDeslocadaDescl = kwargs.get('listaColunaDeslocadaDescl')
        self.listaColunaDeslocadaLance = kwargs.get('listaColunaDeslocadaLance')
        self.listaGrupoContp = kwargs.get('listaGrupoContp')
        self.listaGrupoLanceFixar = kwargs.get('listaGrupoLanceFixar')
        self.numeroMes = kwargs.get('numeroMes')
        self.listaGrupoLanceCompleto = kwargs.get('listaGrupoLanceCompleto')
        self.numeroLinha = kwargs.get('numeroLinha')
        self.listaGrupo360 = kwargs.get('listaGrupo360')
        # self.e = ''
        if self.pAT is not None:
            self.df = pd.read_excel(self.pAT)

# Extra
    def dfDataIgual(self):
        nLinha = self.df[self.df.columns[0]].count()
        col2 = None
        for col in reversed(self.coluna):
            if col2 is None:
                col2 = col
            else:
                for cont in range(nLinha):
                    if self.df.at[cont, col] == self.df.at[cont, col2]:
                        self.df.at[cont, col2] = ''
                col2 = col
        return self.df

    def dfCabecalhoMes(self):
        colunaLance = 'Lance'
        colunaPlano = 'Plano'
        # colunas = self.df.columns.to_list()
        lanceCondicao = False
        for coluna in reversed(self.colunas):
            #  ira descarta todos lances sem contemplcao e comeca no "plano"
            if coluna == colunaPlano:
                lanceCondicao = True
            if lanceCondicao is False:
                continue
            palavra = ''
            mes = ''
            mesCondicao = False
            cont = 0
            for letra in coluna:
                palavra += letra
                if cont >= 1:
                    mes += letra
                    cont -= 1
                if palavra == colunaLance:
                    mesCondicao = True
                    cont = 2
            if mesCondicao is True:
                break
        mesPassado = str(int(mes) - 1)
        mesPassado = mesPassado.rjust(3 - len(mesPassado), '0')
        if mesPassado == '0':
            mesPassado = '12'
        mesRetrasado = str(int(mesPassado) - 1)
        mesRetrasado = mesRetrasado.rjust(3 - len(mesRetrasado), '0')
        if mesRetrasado == '0':
            mesRetrasado = '12'
        self.colunaLista = [
            colunaLance + mes + '-1-1',
            colunaLance + mesPassado + '-1-1',
            colunaLance + mesRetrasado + '-1-1']
        return self.colunaLista

    def colunaForaDeOrdem(self):
        colunaConfir = 'Dt.confir'
        colunaDescla = 'Dt.descla'
        colunaLance = 'Lance'
        colunaNumLance = 'Num Lance'
        listaColunaDeslocada = []
        colunaCorreta = []
        colunaDeslocada = False
        for coluna in self.colunas:
            if colunaDeslocada is False:
                colunaCorreta.append(coluna)
            if colunaDeslocada is True:
                listaColunaDeslocada.append(coluna)
            if coluna == 'Parcela1':
                colunaDeslocada = True
        listaColunaDeslocadaConfm = []
        listaColunaDeslocadaDescl = []
        listaColunaDeslocadaLance = []

        for coluna in listaColunaDeslocada:
            if coluna == colunaNumLance:
                break
            palavra = ''
            for letra in coluna:
                palavra += letra
                if palavra == colunaConfir:
                    listaColunaDeslocadaConfm.append(coluna)
                if palavra == colunaDescla:
                    listaColunaDeslocadaDescl.append(coluna)
                if palavra == colunaLance:
                    listaColunaDeslocadaLance.append(coluna)

        return colunaCorreta, listaColunaDeslocadaConfm, listaColunaDeslocadaDescl, listaColunaDeslocadaLance

    def colunaLocalCorreto(self):
        colunaComtp = 'Dt.contp'
        colunaPlano = 'Plano'
        colunaCorretaNova = []
        colunaPlanoCondicao = False
        numeroUltimo = 0
        for coluna in self.colunaCorreta:
            #  a coluna plano indica que chegou no fim dos lances
            if coluna == colunaPlano:
                coluna = colunaComtp + str(numeroUltimo + 1)
                colunaPlanoCondicao = True
            palavra = ''
            numero = ''
            numeroCondicao = False
            # pegar o primeiro numero da coluna condicao que é op mes
            for letra in coluna:
                palavra += letra
                if numeroCondicao is True:
                    numero += letra
                if palavra == colunaComtp:
                    numeroCondicao = True
            #  se for coluna comteplado ele aprecerar um numero
            if numero != '':
                numero = int(numero)
                numeroUltimo = numero  # o numero da campo contemplado
                for coluna2 in self.listaColunaDeslocadaConfm:
                    # nome da coluna correta da coluna esta no campo pares
                    if ((self.listaColunaDeslocadaConfm.index(coluna2) + 2) % 2) == 0:
                        colunaNome = coluna2
                    else:
                        numero2 = coluna2[0]
                        if numero2 == 12:
                            numero2 = 0
                        # essa condicao ira indicar que o numero da coluna contp é posterio ao
                        # numero da coluna confir
                        if numero2 + 1 == numero:
                            colunaCorretaNova.append(colunaNome)
            if colunaPlanoCondicao is True:
                colunaCorretaNova.append(colunaPlano)
                colunaPlanoCondicao = False
            else:
                colunaCorretaNova.append(coluna)
        return colunaCorretaNova

    def colocarLocalCorreto2(self):
        colunaConfir = 'Dt.confir'
        colunaCorretaNova = []
        for coluna in self.colunaCorreta:
            colunaCorretaNova.append(coluna)
            palavra = ''
            numero = ''
            numeroCondicao = False
            for letra in coluna:
                palavra += letra
                if numeroCondicao is True:
                    numero += letra
                if palavra == colunaConfir:
                    numeroCondicao = True
            if numero != '':
                for coluna2 in self.listaColunaDeslocadaDescl:
                    numero2 = ''
                    numeroCondicao2 = False
                    for letra2 in coluna2:
                        if letra2 == '0' or letra2 == '1':
                            numeroCondicao2 = True
                        if numeroCondicao2 is True:
                            numero2 += letra2
                    if numero == numero2:
                        colunaCorretaNova.append(coluna2)
        return colunaCorretaNova

    def colocarLocalCorreto3(self):
        colunaDescla = 'Dt.descla'
        colunaLance = 'Lance'
        colunaCorretaNova = []
        for coluna in self.listaColunaDeslocadaLance:
            #  pega o nome da coluna
            if ((self.listaColunaDeslocadaLance.index(coluna) + 2) % 2) == 0:
                nomeColuna = coluna
            else:
                # informa que tem que procurar  o DT.descla se for um e lance outros numeros
                if coluna[-1] == 1:
                    nomeAProcurar = colunaDescla
                else:
                    nomeAProcurar = colunaLance

                inseridoComSucesso = False
                colunaCorretaNova = []
                for coluna2 in self.colunaCorreta:
                    # inserir todas as colunas da coluna correta
                    colunaCorretaNova.append(coluna2)
                    if inseridoComSucesso is True:
                        continue
                    palavra = ''
                    condicaoNomeAProcurar = False
                    for letra in coluna2:
                        if letra == '0' or letra == '-':
                            continue
                        palavra += letra
                        if palavra == nomeAProcurar:
                            condicaoNomeAProcurar = True
                            palavra = ''
                    if condicaoNomeAProcurar is True:
                        if nomeAProcurar == colunaDescla:
                            # compara a palavra que é os numeros do descal com os numeros do lance
                            if palavra == str(coluna[0]) + str(coluna[1]):
                                colunaCorretaNova.append(nomeColuna)
                                inseridoComSucesso = True
                        else:
                            # compara a palavra que é os numeros do lance com os numeros do lance a
                            # inserir
                            if palavra == str(coluna[0]) + str(coluna[1]) + str(coluna[-1] - 1):
                                colunaCorretaNova.append(nomeColuna)
                                inseridoComSucesso = True
                self.colunaCorreta = colunaCorretaNova
        return self.colunaCorreta

    def dfColunaOrdenarSequencia(self):
        colunaPlano = 'Plano'
        colunaComtp = 'Dt.contp'
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
        #  todas as colunas de contemplado
        for coluna in self.colunaCorreta:
            palavra = ''
            for letra in coluna:
                palavra += letra
                if palavra == colunaComtp:
                    az[0].append(coluna)
        cont = 0
        for coluna in self.colunaCorreta:
            if coluna == colunaPlano:  # terminas os lances
                break
            for col in az[0]:
                if coluna == col:  # altera a lista de salvar
                    cont += 1
            if cont >= 1:  # não garda o grupo e salva em lista diferente separando os meses
                az[cont].append(coluna)
        lista = ['Grupo', 'TA', 'Valor', 'Parcela1', 'Prazoplano', 'Prox.assembleia', 'Num Lance']
        for num in range(cont + 1, 0, -1):  # inverte as datas colocando o ultimo primeiro
            lista.extend(az[num])
        lista2 = ['Vencimento', 'Medialance']
        lista.extend(lista2)
        for coluna in lista:
            try:
                self.colunas.remove(coluna)
            except ValueError:
                pass
        lista.extend(self.colunas)
        # lista.append('Ordenar')
        self.df = self.df[lista]
        return self.df

    def dfColunaOrdenarSequencia2(self):
        colunas = self.df.columns.to_list()
        lista = []
        listaExcluir = ['Dt.contp', 'Lance']
        listaFim = ['Vencimento', 'Medialance', 'Plano', 'Marca', 'Modelo']
        listaExcluir.extend(listaFim)
        for coluna in colunas:
            palavra = ''
            naoGravar = False
            for letra in coluna:
                palavra += letra
                for col in listaExcluir:
                    if palavra == col:
                        naoGravar = True
            if naoGravar is not True:
                lista.append(coluna)
        lista.extend(listaFim)
        self.df = self.df[lista]

        colunas = self.df.columns.to_list()
        return self.df

# Colunas
    def dfColunaExiste(self):
        try:
            nLinha = self.df[self.df.columns[0]].count()
            for cont in range(nLinha):
                pd.isna(self.df.at[cont, self.coluna])
            return self.df, True
        except KeyError:
            return self.df, False

    def dfColunaPontaVirgula(self):
        nLinha = self.df[self.df.columns[0]].count()
        for cont in range(nLinha):
            inf = str(self.df.at[cont, self.coluna])
            inf = Renomear(inf=inf).pontoVirgula()
            self.df.at[cont, self.coluna] = inf
        return self.df

    def dfColunaStrInt(self):
        nLinha = self.df[self.df.columns[0]].count()
        for cont in range(nLinha):
            self.df.at[cont, self.coluna] = str(int(self.df.at[cont, self.coluna]))
        return self.df

    def dfColunaExcluir(self):
        if self.coluna == 'X':
            for cont in range(self.nUltCol + 1):
                if cont == 0:
                    continue
                self.df = self.df.drop(columns=[self.coluna + str(cont)])
        else:
            try:
                self.df = self.df.drop(columns=[self.coluna])
            except KeyError:
                pass
        return self.df

    def dfColunaExcluirFixar(self):
        for col in self.colunas:
            palavra = ''
            for letra in col:
                palavra += letra
                if palavra == self.coluna:
                    self.df = self.df.drop(columns=[col])
        return self.df

    def colunaGrupoDtContp(self):
        # testecontar = 0
        listaContp = []
        listaGrupo = []
        self.listaGrupoContp = []
        nLinha = self.df[self.df.columns[0]].count()
        for col in self.colunas:
            palavra = ''
            condicaoFixar = False
            for letra in col:
                palavra += letra
                # igual a colunaContp
                if palavra == self.coluna:  # 'Dt.contp'
                    # palavra = ''
                    condicaoFixar = True
            if condicaoFixar is True:
                ultimoGrupoSalvo = '0'
                for cont in range(nLinha):
                    inf = Renomear(inf=self.df.at[cont, col]).vazio()
                    if inf != '' and ultimoGrupoSalvo != self.df.at[cont, 'Grupo']:
                        # vai salvar o numero do grupo e a coluna contp [grupo, contp]
                        listaContp.append([self.df.at[cont, 'Grupo'], col])
                        ultimoGrupoSalvo = self.df.at[cont, 'Grupo']
        for cont in range(nLinha):
            if self.df.at[cont, 'Situacao'] == 'Contempl':
                listaGrupo.append(self.df.at[cont, 'Grupo'])
        for grupo in listaGrupo:
            listaDtContp = [grupo]
            for grupo2, dtContp in listaContp:
                if grupo == grupo2:
                    # sera salvo o grupo e todas suas dt.contp
                    listaDtContp.append(dtContp)
            self.listaGrupoContp.append(listaDtContp)
        return self.listaGrupoContp

    def colunaDtContpLance(self):
        colunas = self.df.columns.to_list()
        self.listaGrupoLanceFixar = []
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
        cont = 0
        listaCont = []
        terminar = False
        for col in colunas:
            palavra = ''
            for letra in col:
                palavra += letra
                if palavra == self.coluna:
                    cont += 1
                    listaCont.append(cont)
                if palavra == 'Vencimento':
                    terminar = True
            if terminar is True:
                break
            if cont >= 1:
                az[cont].append(col)
        for n in listaCont:
            self.listaGrupoLanceFixar.append(az[n])
        return self.listaGrupoLanceFixar

    def colunaDtContpContar(self):
        quantidade = 0
        for grupoDtContp in self.listaGrupoContp:
            if len(grupoDtContp) > quantidade:
                quantidade = len(grupoDtContp)
        quantidade -= 1
        return quantidade

    def dfColunaIndex(self):
        self.coluna = "Index"
        index = []
        nLinha = self.df[self.df.columns[0]].count()
        for cont in range(nLinha):
            index.append(cont)
        self.df.loc[:, self.coluna] = index
        self.df.set_index(self.coluna, inplace=True)
        self.df.index.name = None
        return self.df

    def dfColunaIndexNumeroLinha(self):
        self.coluna = "Index"
        index = []
        # nLinha = self.numeroLinha
        # for cont in range(nLinha):
        index.append(0)
        self.df.loc[:, self.coluna] = index
        self.df.set_index(self.coluna, inplace=True)
        self.df.index.name = None
        return self.df

    def dfColunaALterarNome(self):
        for col in self.df.columns:
            novoNome = Renomear(inf=col).coluna()
            self.df = self.df.rename(columns={col: novoNome})
        return self.df

    def dfColunaDataConfirmacao(self):
        nLinha = self.df[self.df.columns[0]].count()
        try:
            for cont in range(nLinha):
                if self.df.at[cont, self.coluna[0]] != self.df.at[cont, self.coluna[1]]:
                    self.df.at[cont, self.coluna[1]] = self.df.at[cont, self.coluna[0]]
                # pass
                # self.df.at[cont, self.coluna2[n]] = (datetime.strptime((self.df.at[cont, col]), '%d/%m/%Y')).strftime('%Y-%m-%d')
                # self.df.at[cont, col] = (datetime.strptime((self.df.at[cont, col]), '%d/%m/%Y')).strftime('%d/%m/%y')
        except KeyError:
            pass  # ocorre se não existir coluna
        return self.df

    def dfColunaData(self):
        nLinha = self.df[self.df.columns[0]].count()
        n = 0
        try:
            for col in self.coluna:
                for cont in range(nLinha):
                    self.df.at[cont, self.coluna2[n]] = (datetime.strptime(
                        (self.df.at[cont, col]), '%d/%m/%Y')).strftime('%Y-%m-%d')
                    self.df.at[cont, col] = (datetime.strptime(
                        (self.df.at[cont, col]),
                        '%d/%m/%Y')).strftime('%d/%m/%y')
                n += 1
        except KeyError:
            pass  # ocorre se não existir coluna
        return self.df

    def dfColunaDataMes(self):
        nLinha = self.df[self.df.columns[0]].count()
        listaTodos = []
        lista = []
        mesAnterior = 0
        try:
            for cont in range(nLinha):
                if self.df.at[cont, self.coluna[0]] != '=':
                    listaTodos.append((datetime.strptime(
                        (self.df.at[cont, self.coluna[0]]),
                        '%d/%m/%y')).strftime('%m'))
            # listaTodos = sorted(listaTodos, reverse=True)  # inverter
            listaTodos = sorted(listaTodos)
            for mes in listaTodos:
                if mes != mesAnterior:
                    lista.append(mes)
                mesAnterior = mes
        except Exception:
            pass  # coluna nao existe
        return self.df, lista

    def dfColunaJuntar(self):
        self.df.loc[:, self.coluna2] = ''
        nLinha = self.df[self.df.columns[0]].count()
        try:
            for col in self.coluna:
                for cont in range(nLinha):
                    self.df.at[cont, self.coluna2] += str(self.df.at[cont, col]) + ' '
        except KeyError:
            pass  # ocorre se não existir coluna
        return self.df

    def dfColunaConverterFloat(self):
        nLinha = self.df[self.df.columns[0]].count()
        for cont in range(nLinha):
            try:
                self.df.at[cont, self.coluna] = round(float(self.df.at[cont, self.coluna]), 2)
            except ValueError:
                self.df.at[cont, self.coluna] = round(
                    float(Renomear(inf=self.df.at[cont, self.coluna]).virgulaPonto()), 2)
        return self.df

    def dfColunaOrdenar(self):
        if self.decendente is True:  # organizar descendente (ascending=False)
            if self.coluna3 is not None:
                self.df = self.df.sort_values(
                    by=[self.coluna, self.coluna2, self.coluna3],
                    ascending=False)
            elif self.coluna2 is not None:
                self.df = self.df.sort_values(by=[self.coluna, self.coluna2], ascending=False)
            else:
                self.df = self.df.sort_values(by=[self.coluna], ascending=False)

        else:
            if self.coluna3 is not None:   # organizar acendente (ascending=True) padrao
                self.df = self.df.sort_values(by=[self.coluna, self.coluna2, self.coluna3])
            elif self.coluna2 is not None:
                self.df = self.df.sort_values(by=[self.coluna, self.coluna2])
            else:
                self.df = self.df.sort_values(by=[self.coluna])  # organizar
        return self.df

    # def dfColunaOrganizar(self):
    #     nLinha = self.df[self.df.columns[0]].count()
    #     colunas = self.df.columns.to_list()
    #     lista = []
    #     colunaExcluir = [
    #         'Prazoplano',
    #         'Vencimento',
    #         'VencimentoNew',
    #         'Prox.assembleia',
    #         'Realizada']
    #     for coluna in colunaExcluir:
    #         self.df = self.df.drop(columns=[coluna])
    #     colunas = self.df.columns.to_list()
    #     for coluna in colunas:
    #         if coluna == 'Prazo':
    #             break
    #         lista.append(coluna)
    #         if coluna == 'Situacao':
    #             lista.append('ARealizar')
    #             lista.append('Prox_Assembleia')
    #             lista.append('Prazo')
    #     lista2 = []
    #     for coluna in lista:
    #         if coluna == 'Prox_Assembleia':
    #             continue
    #         if coluna == 'Menor Valor':
    #             lista2.append('Prox_Assembleia')
    #         lista2.append(coluna)
    #     self.df = self.df[lista2]
    #     listaContempl = []
    #     listaCancelad = []
    #     listaNaoCont = []
    #     listaNaoCont2 = []
    #     for cont in range(nLinha):
    #         if self.df.at[cont, 'Situacao'] == 'Contempl':
    #             listaContempl.append(self.df.at[cont, 'Grupo'])
    #         elif self.df.at[cont, 'Situacao'] == 'Cancelad':
    #             listaCancelad.append(self.df.at[cont, 'Grupo'])
    #         elif self.df.at[cont, 'Situacao'] == 'Nao Cont':  # obs o espaço só depos é excluido
    #             listaNaoCont.append([self.df.at[cont, 'Grupo'], self.df.at[cont, 'Num Lance']])
    #             listaNaoCont2.append([self.df.at[cont, 'Grupo'], self.df.at[cont, 'Num 25%']])
    #         else:
    #             print(self.df.at[cont, 'Situacao'])
    #     colunaCompletar = ['TA', 'Menor Valor', 'Maior Valor', 'Menor Parcela1', 'Maior Parcela1']
    #     for coluna in colunaCompletar:  # ira pegar colunas pre definida
    #         for cont in range(nLinha):
    #             inf = self.df.at[cont, coluna]
    #             inf = Renomear(inf=inf).vazio()
    #             if inf == '':  # verifica se celula esta vazia
    #                 # if coluna == 'Maior Valor':
    #                 #     print(f'[[[{inf}]]]')
    #                 for contempl in listaContempl:
    #                     # Vai tratar apenas se o grupo for o mesos do grupo de contemplados
    #                     if self.df.at[cont, 'Grupo'] == contempl:
    #                         if self.df.at[cont, 'Situacao'] == 'Contempl':
    #                             self.df.at[cont, coluna] = '0'
    #                         else:
    #                             self.df.at[cont, coluna] = self.df.at[(cont - 1), coluna]
    #                             # print(f'nuca vou passar aqui, mas se sim  colçuan situacao:(({self.df.at[cont, "Situacao"]}))')
    #     for cont in range(nLinha):
    #         if self.df.at[cont, 'Situacao'] == 'Contempl' or self.df.at[cont, 'Situacao'] == 'Cancelad':  # noqa
    #             for grupo, quantidade in listaNaoCont:
    #                 if self.df.at[cont, 'Grupo'] == grupo:
    #                     self.df.at[cont, 'Num Lance'] = quantidade
    #                     break
    #     # ira preencher a coluna Num 25% com valro 0 se existir NaoCont mais não otiver valoe
    #     for cont in range(nLinha):
    #         for (grupo, nLance25) in listaNaoCont2:
    #             if self.df.at[cont, 'Grupo'] == grupo:
    #                 if 'NaoCont' == self.df.at[cont, 'Situacao']:
    #                     inf = self.df.at[cont, 'Num 25%']
    #                     inf = Renomear(inf=inf).vazio()
    #                     if inf == '':
    #                         self.df.at[cont, 'Num 25%'] = 0
    #                 # else:
    #                 #     self.df.at[cont, 'Num 25%'] = nLance25
    #     # colunaCompletar.append('Num 25%')
    #     colunas = self.df.columns.to_list()
    #     inicioColunaLance = False
    #     primeiro = False
    #     for coluna in colunas:
    #         palavra = ''
    #         numero = ''
    #         for letra in coluna:
    #             if letra == '.':
    #                 break
    #             if letra == '-':
    #                 if primeiro is True:
    #                     break
    #                 primeiro = True
    #             if inicioColunaLance is True:
    #                 numero += letra
    #                 continue
    #             palavra += letra
    #             if palavra == 'Lance' or palavra == '%Lance':
    #                 inicioColunaLance = True
    #         if inicioColunaLance is True:
    #             break
    #     nomeColuna = palavra + numero
    #     listaColunaLance = []
    #     for coluna in colunas:
    #         palavra = ''
    #         for letra in coluna:
    #             palavra += letra
    #             if palavra == nomeColuna:
    #                 listaColunaLance.append(coluna)

    #     # print(f'############# a listaColunaLance é (({listaColunaLance}))')

    #     for cont in range(nLinha):
    #         listaColunaLanceOrdemCrecente = []
    #         # listaColunaLanceOrdemDecrecente = []
    #         for coluna in listaColunaLance:
    #             inf = self.df.at[cont, coluna]
    #             inf = Renomear(inf=inf).vazio()
    #             if inf != '':
    #                 listaColunaLanceOrdemCrecente.append(inf)
    #         listaColunaLanceOrdemDecrecente = list(reversed(listaColunaLanceOrdemCrecente))
    #         # print(f'## self.df.at[cont, "Situacao"] {self.df.at[cont, "Situacao"]} ')
    #         if self.df.at[cont, 'Situacao'] == 'Nao Cont':
    #             contar = 0
    #             for coluna in listaColunaLance:
    #                 try:
    #                     inf = listaColunaLanceOrdemDecrecente[contar]
    #                 except IndexError:
    #                     inf = ''
    #                 self.df.at[cont, coluna] = inf
    #                 contar += 1

    #             # print(f'## listaColunaLanceOrdemCrecente (({listaColunaLanceOrdemCrecente}))')
    #             # print(f'## listaColunaLanceOrdemDecrecente (({listaColunaLanceOrdemDecrecente}))')
    #         else:
    #             contar = 0
    #             contar25 = 0
    #             for coluna in listaColunaLance:
    #                 while True:
    #                     try:
    #                         inf = listaColunaLanceOrdemCrecente[contar]
    #                     except IndexError:
    #                         inf = ''
    #                     if inf == '25,0':
    #                         contar25 += 1
    #                         contar += 1
    #                         continue
    #                     break
    #                 self.df.at[cont, coluna] = inf
    #                 contar += 1
    #             self.df.at[cont, 'Num 25%'] = contar25

    #     colunaCompletar.append('Num Lance')
    #     for cont in range(nLinha):
    #         for coluna in colunaCompletar:
    #             inf = self.df.at[cont, coluna]
    #             inf = Renomear(inf=inf).vazio()
    #             if inf == '':
    #                 self.df.at[cont, coluna] = '-1'
    #     for coluna in colunas:
    #         for cont in range(nLinha):
    #             inf = self.df.at[cont, coluna]
    #             inf = Renomear(inf=inf).vazio()
    #             inf = Renomear(inf=inf).virgulaPontoInt()
    #             if inf == '0,001':
    #                 inf = '0'
    #             self.df.at[cont, coluna] = inf

    #     return self.df

    def colunaOrganizar2(self):
        colunas = self.df.columns.to_list()
        lista = []
        for coluna in colunas:
            if coluna == 'Grupo':
                lista.append(coluna)
                lista.append('Situacao')
                continue
            if coluna == 'Valor' or coluna == 'Parcela1':
                lista.append('Menor ' + coluna)
                lista.append('Maior ' + coluna)
                continue
            if coluna == 'Num Lance':
                lista.append('Num 25%')
                lista.append(coluna)
                continue
            if coluna == 'Lance-1-1':
                break
            lista.append(coluna)
        self.df = self.df[lista]
        return self.df

    def dfColunaMover(self):
        editInf = '-'
        nLinha = self.df[self.df.columns[0]].count()
        for cont in range(nLinha):
            nCol = 1
            inf = self.df.at[cont, self.coluna]
            while True:
                inf1, inf = Renomear(inf=inf, editInf=editInf).editTextoColuna()
                self.df.at[cont, self.coluna2[0] + str(nCol)] = inf1
                nCol += 1
                if inf == '':
                    self.df.at[cont, self.coluna2[0] + str(nCol)] = 'X'
                    break
            if self.ap == 'Apuradas':
                self.df.at[cont, 'Num Lance'] = str(nCol - 1)
                self.df.at[cont, 'Prazoplano'] = ' '
        return self.df

    def dfColunaMoverContpFixar(self):
        for cont in range(self.numeroMes):
            for grupoContp in self.listaGrupoContp:
                indiceGrupo = self.df.index[self.df['Grupo'] == grupoContp[0]].tolist()
                for indiceLinha in indiceGrupo:
                    try:
                        self.df.at[indiceLinha,
                                   'Contp' + str(cont)] = self.df.at[indiceLinha,
                                                                     grupoContp[cont + 1]]
                        self.df.at[indiceLinha, grupoContp[cont + 1]] = 'X'
                    except IndexError:
                        pass
        return self.df

    def dfColunaMoverLanceFixar(self):
        for grupoLance in self.listaGrupoLanceCompleto:
            indiceGrupo = self.df.index[self.df['Grupo'] == grupoLance[0]].tolist()
            for indiceLinha in indiceGrupo:
                for lance in grupoLance:
                    if lance == grupoLance[0]:
                        cont = -1
                        continue
                    cont += 1
                    listaTemporaria = []
                    for coluna in lance:
                        inf = Renomear(inf=self.df.at[indiceLinha, coluna]).vazio()
                        inf = Renomear(inf=inf).virgulaPonto()
                        if inf != '':
                            listaTemporaria.append(inf)
                        self.df.at[indiceLinha, coluna] = 'X'
                    listaTemporaria = sorted(listaTemporaria)
                    cont2 = 0
                    for valor in listaTemporaria:
                        cont2 += 1
                        if cont2 == 21:
                            break
                        inf = Renomear(inf=valor).pontoVirgula()
                        self.df.at[indiceLinha, '%Lance' + str(cont) + '.' + str(cont2)] = inf
        return self.df

    def colunaGrupoLanceFixar(self):
        self.listaGrupoLanceCompleto = []
        for grupoContp in self.listaGrupoContp:
            listaTemporaria = []
            listaTemporaria.append(grupoContp[0])
            for contp in grupoContp:
                if contp == grupoContp[0]:
                    continue
                listaTemporaria2 = []
                for GrupoLanceFixar in self.listaGrupoLanceFixar:
                    if contp == GrupoLanceFixar[0]:
                        for lanceFixar in GrupoLanceFixar:
                            if lanceFixar == GrupoLanceFixar[0]:
                                continue
                            listaTemporaria2.append(lanceFixar)
                listaTemporaria.append(listaTemporaria2)
            self.listaGrupoLanceCompleto.append(listaTemporaria)
        return self.listaGrupoLanceCompleto

    def colunaGrupos(self):
        lista = []
        listaGrupo = []
        nLinha = self.df[self.df.columns[0]].count()
        for cont in range(nLinha):
            lista.append(str(int(self.df.at[cont, self.coluna])))
        listagrupo360 = lista
        listagrupo360 = sorted(listagrupo360)

        nLinha = self.df2[self.df2.columns[0]].count()
        for cont in range(nLinha):
            #                   'Administradora'
            if self.df2.at[cont, self.coluna2] == 'DISAL' or self.df2.at[cont, self.coluna2] == 'DISAL PARCEIROS':  # noqa
                #                       'Grupo'
                inf = self.df2.at[cont, self.coluna]
                inf = Renomear(inf=inf).vazio()
                if inf != '':
                    inf = int(inf)
                    if inf > 1000:
                        inf = str(inf)
                        lista.append(inf)

        lista = sorted(lista)
        grupoAnterior = ''

        for grupo in lista:
            if grupo != grupoAnterior:
                listaGrupo.append(grupo)
                grupoAnterior = grupo
        return listaGrupo, listagrupo360

    def colunaGruposStr(self):
        nLinha = self.df[self.df.columns[0]].count()
        for cont in range(nLinha):
            self.df.at[cont, self.coluna] = str(int(self.df.at[cont, self.coluna]))
        return self.df

    def dfColunaSepararMenorMaior(self):
        #  irar separas os valores maior e menor do valor do bem e das parcelas
        colunas = self.df.columns.to_list()
        nLinha = self.df[self.df.columns[0]].count()
        for coluna in colunas:
            if coluna == 'Valor' or coluna == 'Parcela1':
                for cont in range(nLinha):
                    inf = Renomear(inf=self.df.at[cont, coluna]).vazio()
                    inf = Renomear(inf=inf).pontoVirgula()
                    if inf != '':
                        palavra1 = ''
                        palavra2 = ''
                        trocar = False
                        for letra in inf:
                            if letra == ' ':
                                continue
                            if letra == '-':
                                trocar = True
                                continue
                            if trocar is False:
                                palavra1 += letra
                            else:
                                palavra2 += letra
                        self.df.at[cont, ('Menor ' + coluna)] = palavra1
                        self.df.at[cont, ('Maior ' + coluna)] = palavra2
        return self.df

    def dfColunaSituacao(self):
        # Criar uma coluna situacao e colocar os valores 'Contempl, nao Cont, Cancelad'
        nLinha = self.df[self.df.columns[0]].count()
        for cont in range(nLinha):
            inf = Renomear(inf=self.df.at[cont, 'TA']).vazio()
            inf2 = Renomear(inf=self.df.at[cont, 'Num Lance']).vazio()
            if inf != '':
                self.df.at[cont, 'Situacao'] = 'Contempl'
            elif inf2 != '':
                self.df.at[cont, 'Situacao'] = 'Nao Cont'
            else:
                self.df.at[cont, 'Situacao'] = 'Cancelad'
        return self.df

    def dfColunaMoverLanceNaoContemplado(self):
        colunas = self.df.columns.to_list()
        colunasInvertida = self.df.columns[::-1]
        nLinha = self.df[self.df.columns[0]].count()
        listaColunasLance1 = []
        # listaColunasLance2 = []
        listaColunasLanceNaoConteplado1 = []
        listaColunasContp1 = []
        # primeiroLance = False
        # terminar1 = False
        # terminar2 = False
        lista = []
        listaColunasLance1

        # Criar uma lista com nome das colnas Dt.contp
        # listaColunasContp1 ['09', '08', '07', '06']
        for coluna in colunas:
            condicaoNumero = False
            palavra = ''
            numero = ''
            for letra in coluna:
                palavra += letra
                if condicaoNumero is True:
                    numero += letra
                if palavra == 'Dt.contp':
                    condicaoNumero = True
            if condicaoNumero is True:
                listaColunasContp1.append(numero)

        #  Criar uma lista de todas coluna lance nao contemplado ate o lance especificado:
        # listaColunasLanceNaoConteplado1 = ['Lance-1-555', 'Lance-1-554',
        # 'Lance-1-553',...., 'Lance-1-3', 'Lance-1-2', 'Lance-1-1']
        for coluna in colunasInvertida:
            palavra = ''
            for letra in coluna:
                palavra += letra
                if palavra == 'Lance':
                    listaColunasLanceNaoConteplado1.append(coluna)
            if coluna == 'Lance-1-1':
                break

        # Criar lista sem repetir de todos os grupo e ordenar crecente
        # listaGrupoTodosSemrepetir ['2875', '2878', '2884', '2892', '2894', '2903', ..., '4100', '4101', '4102', '4103']
        listaGrupoTodos = []
        listaGrupoTodosSemrepetir = []
        for cont in range(nLinha):
            listaGrupoTodos.append(self.df.at[cont, 'Grupo'])
        listaGrupoTodos = sorted(listaGrupoTodos)
        grupoAnterior = ''
        for grupo in listaGrupoTodos:
            if grupo != grupoAnterior:
                listaGrupoTodosSemrepetir.append(grupo)
            grupoAnterior = grupo

        # criar uma lista com listas com [grupo, número do mês] pode ter repetido
        # listaGrupoRepetido [['3072', '06'], ['3104', '06'], ['3104', '08'], ['2892', '09'], ['2926', '08'], ['2926', '08'], ... ]
        listaGrupoRepetido = []
        for cont in range(nLinha):
            for coluna in listaColunasContp1:  # ['09', '08', '07', '06']
                inf = self.df.at[cont, 'Dt.contp' + coluna]
                inf = Renomear(inf=inf).vazio()
                if inf != '':
                    listaGrupoRepetido.append([self.df.at[cont, 'Grupo'], coluna])

        #  criar uma lista removendo dos grupo com repeticao [grupo, número do mês]
        #  listaGrupoMeses  [['2875', ['07']], ['2878', ['08']], ...,['2926', ['08']], ..., ['3131', ['08', '07', '06']], ..., ['4102', ['08', '07']], ['4103', ['08', '07']]]
        #  listaGrupoSemMes [['2894', []], ['2917', []]]
        listaGrupoMeses = []
        listaGrupoSemMes = []
        listaMesGrupo = []
        listaMesGrupoSemRepetir = []
        for grupo in listaGrupoTodosSemrepetir:
            condicaoTemMes = False
            for (grupo2, mes) in listaGrupoRepetido:
                if grupo == grupo2:
                    listaMesGrupo.append(mes)
                    condicaoTemMes = True
            if condicaoTemMes is True:
                # print(grupo, listaMesGrupo)
                listaMesGrupo = sorted(listaMesGrupo, reverse=True)
                grupoAnterior = ''
                listaMesGrupoSemRepetir = []
                for grupo3 in listaMesGrupo:
                    if grupo3 != grupoAnterior:
                        listaMesGrupoSemRepetir.append(grupo3)
                    grupoAnterior = grupo3
                listaGrupoMeses .append([grupo, listaMesGrupoSemRepetir])
            else:
                # grupos não tem contemplacao apesar de ter apuracao de lance
                listaGrupoSemMes.append([grupo, listaMesGrupo])
            listaMesGrupo = []

        # [grupo e o ultimo mes]
        # listaGrupoUltimoMes [['2875', '07'], ['2878', '08'], ['2884', '07'], ['2892', '09'], ['2903', '08'], ..., ['4102', '08'], ['4103', '08']]
        listaGrupoUltimoMes = []
        for [grupo, meses] in listaGrupoMeses:
            if meses[0] == '12':
                mes = meses[0]
                for mes in meses:
                    if mes == '04':
                        break
                    if mes == '03':
                        break
                    if mes == '02':
                        break
                    if mes == '01':
                        break
            else:
                mes = meses[0]
            listaGrupoUltimoMes.append([grupo, mes])

        # criar uma lista [grupo, [todos os lances]]
        #  listaGrupoLance[['3104', ['21,51', '15,85', '4,46']], ['2892', ['1,21']], ['2926', ['34,38', '7,79', '3,74', '1,28']], ....]
        #   '25,0', '25,0', '25,0', '25,0', '25,0', '25,0', '25,0', '25,0', '25,0', '25,0', '25,0', '25,0', '25,0', '25,0', '25,0', '25,0', '25,0'
        listaGrupoLance = []
        for (grupo, listaColuna) in listaGrupoMeses:
            for cont in range(nLinha):
                inf = Renomear(inf=self.df.at[cont, 'Num Lance']).vazio()
                if self.df.at[cont, 'Grupo'] == grupo and inf != '':
                    listaLancePorGrupo = []
                    for coluna in colunasInvertida:
                        inf2 = Renomear(inf=self.df.at[cont, coluna]).vazio()
                        if inf2 != '':
                            listaLancePorGrupo.append(inf2)
                        if coluna == 'Lance-1-1':
                            break
                    listaGrupoLance.append([grupo, listaLancePorGrupo])

        # criar uma lista [grupo, [todos os lances]] separandos os de 25
        # listaGrupoLanceDividido[['2892', ['1,21'], [0, '25%']], ['2904',
        # ['1,94'], ... ['3091', ['52,36',.. '3,33'], [1, '25%']], ...
        listaGrupoLanceDividido = []
        for (grupo, lances) in listaGrupoLance:
            lancesTodosMenos25 = []
            conteLance25 = 0
            for lance in lances:
                if lance != '25,0':
                    lancesTodosMenos25.append(lance)
                else:
                    conteLance25 += 1
            listaGrupoLanceDividido.append([grupo, lancesTodosMenos25, [conteLance25, '25%']])

        # separa os nomes da coluna dos lances contemplados todos
        # listaColunasLanceContempado['Lance09-1-1', 'Lance09-1-2', 'Lance09-1-3', 'Lance09-1-4', 'Lance09-1-5', 'Lance09-1-6', ..., 'Lance06-3-1', 'Lance06-3-2']
        listaColunasLanceContempado = []
        for coluna in colunas:
            palavra = ''
            for letra in coluna:
                palavra += letra
                if palavra == 'Lance0' or palavra == 'Lance1':
                    listaColunasLanceContempado.append(coluna)

        # separa os nomes da coluna dos lances contemplados por respequiivos meses
        # listaColunasLanceContempadoMes0 ['Lance09-1-1', 'Lance09-1-2', 'Lance09-1-3', ..., 'Lance09-2-3', 'Lance09-2-4']
        # listaColunasLanceContempadoMes1 ['Lance08-1-1', 'Lance08-1-2', 'Lance08-1-3', ..., 'Lance08-3-3', 'Lance08-4-1']
        # listaColunasLanceContempadoMes2 ['Lance07-1-1', 'Lance07-1-2', 'Lance07-1-3', ..., 'Lance07-4-1', 'Lance07-4-2']
        # listaColunasLanceContempadoMes3 ['Lance06-1-1', 'Lance06-1-2', 'Lance06-1-3', ..., 'Lance06-3-1', 'Lance06-3-2']
        listaColunasLanceContempadoMes0 = []
        listaColunasLanceContempadoMes1 = []
        listaColunasLanceContempadoMes2 = []
        listaColunasLanceContempadoMes3 = []
        ultimoPenultimoMes = []
        ultimoPenultimoMesSemRepetir = []
        for coluna in listaColunasLanceContempado:
            palavra = ''
            numero = ''
            comecaNumero = False
            for letra in coluna:
                palavra += letra
                if letra == '-':
                    break
                if comecaNumero:
                    numero += letra
                if palavra == 'Lance':
                    comecaNumero = True
            ultimoPenultimoMes.append(numero)
        penultimoNumero = ''
        for numero in ultimoPenultimoMes:
            if penultimoNumero != numero:
                ultimoPenultimoMesSemRepetir.append(numero)
                penultimoNumero = numero
        for coluna in listaColunasLanceContempado:
            palavra = ''
            for letra in coluna:
                palavra += letra
                try:
                    if palavra == 'Lance' + ultimoPenultimoMesSemRepetir[0]:
                        listaColunasLanceContempadoMes0.append(coluna)
                    elif palavra == 'Lance' + ultimoPenultimoMesSemRepetir[1]:
                        listaColunasLanceContempadoMes1.append(coluna)
                    elif palavra == 'Lance' + ultimoPenultimoMesSemRepetir[2]:
                        listaColunasLanceContempadoMes2.append(coluna)
                    elif palavra == 'Lance' + ultimoPenultimoMesSemRepetir[3]:
                        listaColunasLanceContempadoMes3.append(coluna)
                except IndexError:  # quando não existir a quantidade de coluna 4 ou menos
                    pass
        listaDasListaColunasLanceTeste = [
            listaColunasLanceContempadoMes0,
            listaColunasLanceContempadoMes1,
            listaColunasLanceContempadoMes2,
            listaColunasLanceContempadoMes3]
        listaDasListaColunasLance = []
        for lista in listaDasListaColunasLanceTeste:
            if lista != []:  # ira remover a lista vazias
                listaDasListaColunasLance.append(lista)

        # criar uma lista [grupo, [todos os lances contemplados do ultimo mes]]
        # listaGrupoLanceUltmosMes [['2875', ['Lance07-1-1', 'Lance07-1-2',
        # ...,'Lance07-4-2']], ['2878', ['Lance08-1-1', 'Lance08-1-2', ...,
        # 'Lance08-4-1']],...
        listaGrupoLanceUltmosMes = []
        for (grupo, mes) in listaGrupoUltimoMes:
            sair = False
            for lista in listaDasListaColunasLance:
                palavra = ''
                for letra in lista[0]:
                    palavra += letra
                    if palavra == 'Lance' + mes:
                        listaGrupoLanceUltmosMes.append([grupo, lista])
                        sair = True
                        break
                if sair is True:
                    break

        # Criar uma lista [grupo, [todos os valorea do lances do ultimo mes]]
        # listaGrupoLanceUltmosMesValor [['2875', ['5,82']], ['2878', ['3,12']], ['2884', ['5,8']], ['2892', ['1,21']], ['2903', ['10,77']] ]
        listaGrupoLanceUltmosMesValor = []
        for (grupo, colunasLances) in listaGrupoLanceUltmosMes:
            listaValoresLance = []
            for cont in range(nLinha):
                if self.df.at[cont, 'Grupo'] == grupo:
                    for colunaLance in colunasLances:
                        inf = Renomear(inf=self.df.at[cont, colunaLance]).vazio()
                        if inf != '':
                            listaValoresLance.append(inf)
            listaGrupoLanceUltmosMesValor.append([grupo, listaValoresLance])

        # criar uma lista com grupo e todos os lances
        # listaGrupoTodosMeses[['2875', [['Lance07-1-1', ...', 'Lance07-4-2']]],
        # ['2907', [['Lance09-1-1', ... 'Lance09-2-4'], ['Lance08-1-1',...
        # 'Lance08-4-1'], ['Lance07-1-1',... 'Lance07-4-2']]], ...
        listaGrupoTodosMeses = []
        for (grupo, meses) in listaGrupoMeses:
            listaTodosMeses = []
            for mes in meses:
                for lista in listaDasListaColunasLance:
                    palavra = ''
                    for letra in lista[0]:
                        palavra += letra
                        if palavra == 'Lance' + mes:
                            listaTodosMeses.append(lista)
            listaGrupoTodosMeses.append([grupo, listaTodosMeses])

        # criar uma lista [grupo, [todos os lances]] menos [grupo, [todos os lances contemplados]
        # listaGrupoLanceNaoExistente[['2892', []], ['2904', []], ['2907', ['10,18']], ['2909', []], ['2922', []], ['2923', ['7,79']], ['2926', ['3,74']],...]
        listaGrupoLanceNaoExistente = []
        # for (grupo1, valoresLance1) in listaGrupoLance:  #
        # listaGrupoLance[['3104', ['21,51', '15,85', '4,46']], ['2892',
        # ['1,21']],  ....]
        for (grupo1, valoresLance1, lista25) in listaGrupoLanceDividido:
            for (grupo2, valoresLance2) in listaGrupoLanceUltmosMesValor:
                if grupo1 == grupo2:
                    for valor in valoresLance2:
                        try:
                            valoresLance1.remove(valor)
                        except (ValueError, IndexError):
                            pass  # quando nao hover valor na lista, ocorreu nos teste devido alteracao forcada
            listaGrupoLanceNaoExistente.append([grupo1, valoresLance1, lista25])

        # coloca os valores de lances nao conteplados nas lisnha que tiver valor na coluna 'Num Lqance'.
        # Ou seja, os valores do lances que nao forma contemplados abaixo dos ultimos lances contemplados
        # coloca o valor de repeticao dos lances de 25% que é uma lance fixo
        for cont in range(nLinha):
            inf = Renomear(inf=self.df.at[cont, 'Num Lance']).vazio()
            if inf != '':
                grupo = self.df.at[cont, 'Grupo']
                for (grupo1, colunasLances) in listaGrupoLanceUltmosMes:
                    if grupo1 == grupo:
                        break
                for (grupo2, valores, lista25) in listaGrupoLanceNaoExistente:
                    if grupo2 == grupo:
                        break
                contar = 0
                for colunaLance in colunasLances:
                    try:
                        self.df.at[cont, colunaLance] = valores[contar]
                    except (ValueError, IndexError):
                        pass  # quando nao hover valor na lista, ocorreu nos teste devido alteracao forcada
                    contar += 1
                self.df.at[cont, 'Num 25%'] = str(lista25[0])
        return self.df

    def dfColunaCriarVazia(self):
        self.df.loc[:, self.coluna] = 0
        return self.df

    def dfColunaVariasCriarVazia(self):
        for cont in range(self.numeroMes):
            self.df.loc[:, 'Contp' + str(cont)] = 0
            for cont2 in range(1, 21, 1):
                self.df.loc[:, '%Lance' + str(cont) + '.' + str(cont2)] = ''
        return self.df

    def dfColunaCriarBaseOutraColuna(self):
        contar = 0
        colunaListaNova = []
        # ira criar colunas baseados nos meses enviados  "ordem1 , ordem2, ordem3""

        for coluna in self.colunaLista:
            contar += 1
            self.df.loc[:, self.coluna + str(contar)] = self.df[coluna]
            colunaListaNova.append(self.coluna + str(contar))
        nLinha = self.df[self.df.columns[0]].count()
        # ira mostra o numero do mair quantidade '3'
        maiorQuantidade = 1
        for cont in range(nLinha):
            quantidade = 0
            for coluna in colunaListaNova:
                inf = self.df.at[cont, coluna]
                inf = Renomear(inf=inf).vazio()
                if inf != '':
                    quantidade += 1
                if quantidade > maiorQuantidade:
                    maiorQuantidade = quantidade

        # ira colocar as data do formato desejados na colunas ordem
        for cont in range(nLinha):
            valor = 0
            for coluna in colunaListaNova:
                inf = self.df.at[cont, coluna]
                inf = Renomear(inf=inf).vazio()
                inf = Renomear(inf=inf).virgulaPonto()
                if inf != '':
                    valor += inf
            try:
                valor = (valor / maiorQuantidade)
                valor = float(str(round(valor, 2)) + str(int(self.df.at[cont, 'Grupo'])))
                self.df.at[cont, self.coluna] = valor
            except ZeroDivisionError:
                pass  # quando nao existir valores
        return self.df

    def dfColunaDesclassificadaOrdenar(self):
        nLinha = self.df[self.df.columns[0]].count()
        for cont in range(nLinha):
            inf = Renomear(inf=self.df.at[cont, self.coluna2]).vazio()
            #   pegar a coluna TA vazia para utilizar sua linha cont
            if inf == '':
                for cont2 in range(nLinha):
                    #  se a linha(cont)  coluna Grupo igual a linha(cont2) coluna Grupo
                    if self.df.at[cont, self.coluna3] == self.df.at[cont2, self.coluna3]:
                        inf = Renomear(inf=self.df.at[cont2, self.coluna2]).vazio()
                        #   pegar a coluna TA NAO vazia para utilizar sua linha cont2
                        if inf != '':
                            # ira salvar o numero do grupo na coluna ordenar que não tem informacao
                            # couna TA
                            self.df.at[cont, self.coluna] = self.df.at[cont2, self.coluna]
        return self.df

    def dfValorExcluirRepetida(self):
        colunaListaTodos = self.df.columns.to_list()
        nLinha = self.df[self.df.columns[0]].count()
        numeroLista = []
        numeroCondicao = False
        for coluna in colunaListaTodos:
            palavra = ''
            numero = ''
            for letra in coluna:
                palavra += letra
                if numeroCondicao is True:
                    numero += letra
                if palavra == self.coluna:
                    numeroCondicao = True
            if numeroCondicao is True:
                numeroLista.append(numero)
                numeroCondicao = False
        for numero in numeroLista:
            colunaContp = self.coluna + numero
            colunaConfir = self.coluna2 + numero + '-1'
            for cont in range(nLinha):
                if self.df.at[cont, colunaContp] == self.df.at[cont, colunaConfir]:
                    self.df.at[cont, colunaConfir] = '  <-   ='
        return self.df

    def dfColunaNUlt(self):
        # listaNUltCol = []
        for colun in self.coluna:  # ira pecorrer todas colunas de self.coluna
            if colun != self.coluna[-1]:
                continue
            for col in self.df.columns[::-
                                       1]:  # irar mostra todas colunas da tabela de tras para frente
                cont = 0
                nomeColuna = ''
                numeroColuna = ''
                for letra in col:
                    cont += 1
                    if cont <= len(
                            colun):  # se cont form menor ou igual ao tamanho da cluna original
                        nomeColuna += letra  # nome da coluna
                    else:
                        numeroColuna += letra  # numero
                if nomeColuna == colun:  # se nome da coluna for igual a formacao
                    if numeroColuna == '':
                        numeroColuna = 0
                    numeroColuna = int(numeroColuna)
                    self.nUltColX = numeroColuna
                    break
            if self.nUltColX is None:  # coluna lance não existe pois apagada ai o X é 0
                self.nUltColX = 0
            # listaNUltCol.append(self.nUltCol)
        return self.df, self.nUltColX

    def dfColunaRenomearNUlt(self):
        for col in self.coluna:  # ira pecorrer todas colunas de self.coluna
            if col != self.coluna[-1]:  # destatar todas coluna menos a X
                continue
            nLinha = self.df[self.df.columns[0]].count()
            for cont in range(nLinha):
                self.df.at[cont, col + str(self.nUltColX)] = col + col
        return self.df

    def dfLinhaCodicaoColComGrupo(self):
        nLinha = self.df[self.df.columns[0]].count()
        listaLinha = []
        for cont in range(nLinha):
            if self.df.at[cont, self.coluna[0]] != '=':  # grupo
                if self.df.at[cont, self.coluna[2]] != 'OK':  # dt. confm
                    if self.df.at[cont, self.coluna[1]] != 'X':   # lances
                        if self.mes == (datetime.strptime(
                            (self.df.at[cont, self.coluna[2]]),
                                '%d/%m/%y')).strftime('%m'):
                            listaLinha.append(cont)
        return self.df, listaLinha

    def dfLinhaCodicaoColSemGrupoSemContp(self):
        nLinha = self.df[self.df.columns[0]].count()
        listaLinha = []
        for cont in range(nLinha):
            if self.df.at[cont, self.coluna[0]] == '=':  # Grupo
                if self.df.at[cont,
                              self.coluna[2]] == '=' and self.df.at[cont - 1,
                                                                    self.coluna[2]] == 'OK':  # dt.contp
                    if self.df.at[cont, self.coluna[1]] != 'X':   # lances
                        # if self.mes == (datetime.strptime((self.df.at[cont, self.coluna[3]]),
                        # '%d/%m/%y')).strftime('%m'):
                        listaLinha.append(cont)
        return self.df, listaLinha

    def dfLinhaCodicaoColSemGrupoComContp(self):
        nLinha = self.df[self.df.columns[0]].count()
        listaLinha = []
        for cont in range(nLinha):
            if self.df.at[cont, self.coluna[0]] == '=':  # Grupo
                if self.df.at[cont,
                              self.coluna[2]] != '=' and self.df.at[cont - 1,
                                                                    self.coluna[2]] == 'OK':  # dt.contp
                    if self.df.at[cont, self.coluna[1]] != 'X':   # lances
                        if self.mes == (datetime.strptime(
                            (self.df.at[cont, self.coluna[2]]),
                                '%d/%m/%y')).strftime('%m'):
                            listaLinha.append(cont)
        return self.df, listaLinha

    def dfLinhaCodicaoColSoGrupo(self):
        nLinha = self.df[self.df.columns[0]].count()
        listaLinha = []
        for cont in range(nLinha):
            if self.df.at[cont, self.coluna[0]] != '=':  # Grupo
                listaLinha.append(cont)
        return self.df, listaLinha

    def dfColunaCodicaoVazia(self):
        nLinha = self.df[self.df.columns[0]].count()
        listaColuna = []
        for col in self.df.columns[::]:
            vazio = True
            for linha in range(nLinha):
                self.df.at[linha, col] = Renomear(inf=self.df.at[linha, col]).vazio()
                # self.df.at[linha, col] = int(self.df.at[linha, col])
                if self.df.at[linha, col] != '':  # Grupo
                    vazio = False
                    break
            if vazio is True:
                listaColuna.append(col)
        return self.df, listaColuna

    def dfColCriarMover(self):
        for cont in self.listaLinha:
            linha = cont
            if self.mesmaLinha is None:  # condicao necessario para saber se tem ou nao numero na coluna Grupo
                linha -= 1
            for col in self.coluna:
                try:
                    if col == self.coluna[-2]:  # coluna Lance
                        continue  # pular
                    if col != self.coluna[-1]:  # diferente coluna x
                        if self.df.at[cont, col] != '=':  # não vai copirar se for '='
                            col2 = col + self.mes  # coluna contp
                            if col != self.coluna[0]:  # coluna todas data
                                # numeroConfm = str(self.nUltColConfm+1)  # ultima numero da coluna
                                # confm + 1
                                col2 += '-' + str(self.nUltColConfm)
                            self.df.at[linha, col2] = self.df.at[cont, col]  # copiar valor
                            self.df.at[cont, col] = 'OK'  # substituir valor por OK
                except KeyError:
                    pass  # coluna não exite
                if col == self.coluna[-1]:  # coluna x que é os lances
                    nCol = 1
                    valorX = False
                    while True:
                        if self.df.at[cont,
                                      col + str(nCol)] == col + col:  # quando encontrar valor XX
                            break
                        try:
                            # formato da coluna Lance
                            col2 = self.coluna[-2] + self.mes + '-' + \
                                str(self.nUltColConfm) + '-' + str(nCol)
                        except TypeError:
                            # formato da coluna Lance
                            col2 = self.coluna[-2] + '-' + str(self.nUltColConfm) + '-' + str(nCol)
                        if self.df.at[cont, col + str(nCol)] == col:
                            valorX = True
                        if valorX is True:
                            self.df.at[linha, col2] = ''
                        else:
                            self.df.at[linha, col2] = Renomear(
                                inf=str(self.df.at[cont, col + str(nCol)])).pontoVirgula()  # copiar valor editado
                        self.df.at[cont, col + str(nCol)] = col  # substituir valores por X
                        nCol += 1
        return self.df

    def dfColCriarMover2(self):
        for cont in self.listaLinha:
            linha = cont
            if self.mesmaLinha is None:  # condicao necessario para saber se tem ou nao numero na coluna Grupo
                linha -= 1
            for col in self.coluna:
                try:
                    if col == self.coluna[-2]:  # coluna Lance
                        continue  # pular
                    if col == self.coluna[1]:  # coluna confir
                        continue  # pular
                    if col != self.coluna[-1]:  # diferente coluna x
                        if self.df.at[cont, col] != '=':  # não vai copirar se for '='
                            col2 = col + self.mes  # coluna contp
                            if col != self.coluna[0]:  # coluna todas data
                                # numeroConfm = str(self.nUltColConfm+1)  # ultima numero da coluna
                                # confm + 1
                                col2 += '-' + str(self.nUltColConfm)
                            self.df.at[linha, col2] = self.df.at[cont, col]  # copiar valor
                            self.df.at[cont, col] = 'OK'  # substituir valor por OK
                except KeyError:
                    pass  # coluna não exite
                if col == self.coluna[-1]:  # coluna x que é os lances
                    nCol = 1
                    valorX = False
                    while True:
                        if self.df.at[cont,
                                      col + str(nCol)] == col + col:  # quando encontrar valor XX
                            break
                        try:
                            # formato da coluna Lance
                            col2 = self.coluna[-2] + self.mes + '-' + str(nCol)
                        except TypeError:
                            col2 = self.coluna[-2] + '-' + str(nCol)  # formato da coluna Lance
                        if self.df.at[cont, col + str(nCol)] == col:
                            valorX = True
                        if valorX is True:
                            self.df.at[linha, col2] = ''
                        else:
                            self.df.at[linha, col2] = Renomear(
                                inf=str(self.df.at[cont, col + str(nCol)])).pontoVirgula()  # copiar valor editado
                        self.df.at[cont, col + str(nCol)] = col  # substituir valores por X
                        nCol += 1
        return self.df

    def dfColunaCriarMoverSemCol1(self):
        nLinha = self.df[self.df.columns[0]].count()
        loop = False
        for cont in range(nLinha):
            if self.df.at[cont,
                          self.coluna2] == '' and self.df.at[cont - 1,
                                                             self.coluna2] != '' and self.df.at[cont,
                                                                                                self.coluna] != '' and self.df.at[cont - 1,
                                                                                                                                  self.coluna] == '':
                if self.mes == (
                    datetime.strptime((self.df.at[cont, self.coluna]),
                                      '%d/%m/%y')).strftime('%m'):
                    self.df.at[cont -
                               1, self.coluna +
                               str(self.nUltCol)] = self.df.at[cont, self.coluna]
                    self.df.at[cont, self.coluna] = ''
                    loop = True
        return self.df, loop

# Linhas
    def dfLinhaJuntarSemRepetir(self):
        nLinha = self.df[self.df.columns[0]].count()
        lista = []
        while nLinha >= 1:
            nLinha -= 1
            inf = str(self.df.at[nLinha, self.coluna2])
            lista.append(inf)
            if self.df.at[nLinha, self.coluna] != '=':
                lista = sorted(lista)
                inf = ''
                y = ''
                for x in lista:
                    if x != y:
                        inf += x + ' - '
                    y = x
                inf = inf[:-3]
                inf = Renomear(inf=inf).planoMarcaModelo()
                self.df.at[nLinha, self.coluna2] = inf
                lista = []
        return self.df

    def dfLinhaJuntarMenorMaior(self):
        nLinha = self.df[self.df.columns[0]].count()
        lista = []
        while nLinha >= 1:
            nLinha -= 1
            inf = self.df.at[nLinha, self.coluna2]
            inf = str(inf)
            inf = Renomear(inf=inf).valor()
            lista.append(float(inf))
            if self.df.at[nLinha, self.coluna] != '=':
                lista = sorted(lista)
                self.df.at[nLinha, self.coluna2] = f'{lista[0]:.2f} - {lista[-1]:.2f}'
                lista = []
        return self.df

    def dfLinhaCaracterEspecial(self):
        nLinha = self.df[self.df.columns[0]].count() + 1
        for cont in range(nLinha):
            try:
                self.df.at[cont, self.coluna] = Renomear(inf=self.df.at[cont, self.coluna]).vazio()
            except KeyError:  # se direto nao tem o 0 se importado nao tem o ultimo
                continue
        return self.df

    def dfLinhaExcluir(self):
        try:
            for linha in self.textoLinha:
                self.df = self.df[self.df[self.coluna] != linha]
        except KeyError:
            pass  # erro ocorre se não existir a self.coluna
        return self.df

    def dfLinhaExcluir2(self):
        diasAnterior = 120
        nLinha = self.df[self.df.columns[0]].count()
        data = date.today() - timedelta(diasAnterior)
        listaData = []
        try:
            for cont in range(nLinha):
                dataStr = self.df.at[cont, self.coluna]
                dataGrupo = datetime.strptime(dataStr, '%d/%m/%Y').date()
                if dataGrupo < data:
                    listaData.append(dataStr)
            listaData = sorted(listaData)
            dataAnterior = '01/01/01'
            for dataGrupo2 in listaData:
                if dataGrupo2 != dataAnterior:
                    self.df = self.df[self.df[self.coluna] != dataGrupo2]
                dataAnterior = dataGrupo2
        except KeyError:
            # print(f'####error {e}')
            pass  # erro ocorre se não existir a self.coluna
        return self.df

    # def dfColunaExcluirRepetida(self):
    #     self.df = self.df[[self.coluna]]
    #     lista = []
    #     cont = 0
    #     grupo = None
    #     nLinha = self.df[self.df.columns[0]].count()
    #     # print(f'numero de linha: {nLinha}')
    #     for cont in range(nLinha):
    #         if grupo != self.df.at[cont, self.coluna]:
    #             lista.append(self.df.at[cont, self.coluna])
    #             grupo = self.df.at[cont, self.coluna]
    #     return lista

    def dfLinhaRepetida(self):
        cont2 = 0
        self.nXRept = 0
        nLinha = self.df[self.df.columns[0]].count()
        for cont in range(nLinha):
            if cont == 0:
                continue
            if self.df.at[cont, self.coluna] == self.df.at[cont2, self.coluna]:
                self.df.at[cont, self.coluna] = '='
            else:
                cont2 = cont
        return self.df

    def dfLinhaRepetida2Col(self):
        cont2 = 0
        # self.nXRept = 0
        nLinha = self.df[self.df.columns[0]].count()
        for cont in range(nLinha):
            if cont == 0:
                continue
            if self.df.at[cont,
                          self.coluna2] == '=' and self.df.at[cont,
                                                              self.coluna[0]] == self.df.at[cont2,
                                                                                            self.coluna[0]]:  # grupo # ssdt.contp
                self.df.at[cont, self.coluna[0]] = '='
            else:
                cont2 = cont
        return self.df

    def dfLinhaJuntar(self):
        nLinha = self.df[self.df.columns[0]].count() - 1
        lista = []
        listaLinha = []
        for cont in range(nLinha, -1, -1):
            inf = self.df.at[cont, self.coluna2]  # lance
            # inf = Renomear(inf=inf).valor()
            lista.append(inf)
            if self.df.at[cont, self.coluna] != '=':  # juncao
                lista = sorted(lista, key=float)  # ordenar lista
                inf = ''
                for x in lista:
                    inf += str(x) + '-'  # escrever todas as informacões em lista
                inf = inf[:-1]  # escluir o ultimo '-'
                self.df.at[cont, self.coluna2] = inf  # lance
                lista = []
            else:
                listaLinha.append(cont)
        return self.df, listaLinha

    def dfLinhaVaziaExcluir(self):
        for cont in self.lista:
            self.df = self.df.drop(index=cont)
        return self.df

    def dfCamposNumero(self):
        novaLista = []
        for coluna in self.campoLista:
            novaLista.append(coluna)
            numeroCondicao = False
            numeroLista = []
            numero = ''
            for letra in coluna:
                if letra == '0' or letra == '1':
                    numeroCondicao = True
                if numeroCondicao is True:
                    if letra == '-':
                        numeroLista.append(int(numero))
                        numero = ''
                    else:
                        numero += letra
            numeroLista.append(int(numero))
            novaLista.append(numeroLista)
        return novaLista

    def dfCamposNumero2(self):
        novaLista = []
        for coluna in self.campoLista:
            novaLista.append(coluna)
            numeroCondicao = False
            numeroLista = []
            numero = ''
            for letra in coluna:
                # if letra == '0' or letra == '1':
                #     numeroCondicao = True
                if numeroCondicao is True:
                    numero += letra
                if letra == '-':
                    # numeroLista.append(int(numero))
                    numero = ''
                    numeroCondicao = True
            numeroLista.append(int(numero))
            novaLista.append(numeroLista)
        return novaLista

    def dfColunaLinhas(self):
        nColunas = len(self.colunas)
        for cont in range(nColunas):
            self.df.at[self.numeroLinha, self.colunas[cont]] = self.lista[cont]
        return self.df

    def dfDf2(self):
        nLinha = self.df2[self.df2.columns[0]].count()
        colunas = self.df.columns.to_list()
        for coluna in colunas:
            for cont in range(nLinha):
                if coluna == 'Grupo':
                    self.df.at[cont, coluna] = str(self.df2.at[cont, coluna])
                elif coluna == 'Prox.assembleia':
                    self.df.at[cont, coluna] = str(
                        int(self.df2.at[cont, 'Realizada']) + 1) + ' - ' + str(self.df2.at[cont, 'Prox_Assembleia'])
                elif coluna == 'Prazoplano':
                    self.df.at[cont, coluna] = str(int(self.df2.at[cont, 'ARealizar']))
                elif coluna == 'Vencimento':
                    self.df.at[cont, coluna] = str(self.df2.at[cont, 'VencimentoNew'])
                else:
                    self.df.at[cont, coluna] = '0.001'
        return self.df

    def dfDf2RemoverRepetido360(self):
        lista = []
        nLinha = self.df2[self.df2.columns[0]].count()
        for cont in range(nLinha):
            inf = self.df2.at[cont, self.coluna]
            inf = int(inf)
            lista.append(inf)
        for grupo in lista:
            self.df = self.df[self.df[self.coluna] != str(grupo)]

        return self.df


if __name__ == '__main__':
    import main
