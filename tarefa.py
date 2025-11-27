# flake8: noqa
# pyright: # type: ignore

import time
# import sys
from funct import Funct
from dfSite import DfSite
from tempo import Tempo
from log import Log
# from botao import Botao
# from IPython.display import display

from bs4 import BeautifulSoup  # Analisar documentos HTML e XML


class Tarefa:
    def __init__(self, *args, **kwargs):
        self.driver = kwargs.get('driver')
        self.url = kwargs.get('url')
        self.texto = kwargs.get('texto')
        self.texto1 = kwargs.get('texto1')
        self.texto2 = kwargs.get('texto2')
        self.texto3 = kwargs.get('texto3')
        self.indTx1 = kwargs.get('indTx1')
        self.indTx2 = kwargs.get('indTx2')
        self.indTx3 = kwargs.get('indTx3')
        self.indTx4 = kwargs.get('indTx4')
        self.tpInicSegProg = kwargs.get('tpInicSegProg')
        self.pAL = kwargs.get('pAL')
        self.ultNIndex = kwargs.get('ultNIndex')
        self.ultCel1 = kwargs.get('ultCel1')
        self.ultCel2 = kwargs.get('ultCel2')
        self.colCel1 = kwargs.get('colCel1')
        self.colCel2 = kwargs.get('colCel2')
        self.tratarModelo = kwargs.get('tratarModelo')
        self.tag1 = kwargs.get('tag1')
        self.tag2 = kwargs.get('tag2')
        self.tag3 = kwargs.get('tag3')
        self.tagCab = kwargs.get('tagCab')
        self.tempo = kwargs.get('tempo')
        self.gNewcon = kwargs.get('gNewcon')
        self.fator_repeticao = 4  # 1=1s, 2=3s, 3=7s, 4=15s, 5=31s, 6=63, 7=127s...
        self.quantidades_tentativas = 4
        self.xpath_present_secreen = kwargs.get('xpath_present_secreen')
        # self.retornar = True

    def zera_variaveis(self):
        self.tag2 = None
        self.tag3 = None
        self.tagCab = None
        # self.ultNIndex = None
        self.html = None
        self.url = None
        self.texto1 = None
        self.texto2 = None
        self.texto3 = None
        self.tratarModelo = None
        self.gNewcon = None
        self.xpath_present_secreen = None
        self.tempo = None

    # tarefas repetida do 360
    def tasks_repeat_360(self):
        tpInicSegPlano = Tempo().tempo_execucao()

        faz = 'click_texto'
        Funct(driver=self.driver, urls=[
                self.texto], faz=faz, pAL=self.pAL).funct()

        # Marca
        faz = 'locate'
        Funct(driver=self.driver, urls=[
                self.url], faz=faz, pAL=self.pAL).funct()

        contHtmlErrado = 0
        contHtmlVazio = 0
        tempoEsperar = 1
        while True:
            funct = Funct()
            funct.driver = self.driver
            funct.urls = [self.url]
            funct.pAL = self.pAL
            funct.funct()
            # Funct(driver=self.driver, urls=[self.url], pAL=self.pAL).funct()
            if self.xpath_present_secreen:
                funct.xpath_present_secreen = self.xpath_present_secreen
            funct.faz = 'informar'
            funct.tag1 = self.tag1
            html = funct.funct()
            # html = Funct(driver=self.driver, urls=[
            #                self.url], tag1=self.tag1, pAL=self.pAL, faz=faz).funct()
            dfSite = DfSite()
            dfSite.html = html
            dfSite.tag1 = self.tag1
            dfSite.tag2 = self.tag2
            htmlTag = dfSite.df()
            # htmlTag = DfSite(html=html, tag1=self.tag1, tag2=self.tag2).df()

            # consultra erros:
            if htmlTag == []:  # não existe info entao repita pode ser atualizacao no site
                contHtmlVazio += 1
                time.sleep(tempoEsperar)
            else:
                funct.urls = [htmlTag[0]]
                # funct.retornar = True
                funct.faz = 'click_texto'
                retorno = funct.funct()

                # retorno = Funct(
                #     driver=self.driver,
                #     urls=[textoNovo],
                #     faz=faz,
                #     retornar=retornar,
                #     pAL=self.pAL).funct()
                if retorno is False:  # não conseguiu clicar na info, é possivel que as informações seja antigas, refazer processo
                    contHtmlErrado += 1
                    time.sleep(tempoEsperar)
                else:
                    break
            if contHtmlErrado >= 5 or contHtmlVazio >= 5:
                break
        escreva = 'plano: ' + '/' + self.texto
        tempo_ = Tempo()
        tempo_.tpInicSeg = tpInicSegPlano
        tempo_.tpInicSegProg = self.tpInicSegProg
        tempo_.escreva = escreva
        tempo_.pAL = self.pAL
        tempo_.tempo_execucao()
        # Tempo(tpInicSeg=tpInicSegPlano, tpInicSegProg=self.tpInicSegProg,
        #       escreva=escreva, pAL=self.pAL).tempo_execucao()
        self.zera_variaveis()
        return htmlTag

    def df_newcon(self):
        log = Log()
        tempo = Tempo()

        tpInicSegModelo = tempo.tempo_execucao()  # tempo para log
        if self.gNewcon is not None:
            self.texto1 = self.gNewcon
            self.testeVazio = 1
        else:
            self.testeVazio = 4
        if self.ultNIndex == '0':
            self.ultCel1 = ''
            self.ultCel2 = ''
        if self.ultCel1 == 0:
            self.ultCel1 = ''
        if self.ultCel2 == 0:
            self.ultCel2 = ''
        penulNIndex = self.ultNIndex
        penulCel1 = self.ultCel1
        penulCel2 = self.ultCel2
        contHtmlVazio = 0
        contHtmlErrado = 0
        tempoEsperar = 1
        escreva2 = ''
        while True:
            funct = Funct()
            if self.xpath_present_secreen:
                funct.xpath_present_secreen = self.xpath_present_secreen
            funct.driver = self.driver
            funct.pAL = self.pAL
            funct.urls = [self.url]
            funct.tag1 = self.tag1
            funct.tag2 = self.tag2
            funct.tempo = self.tempo
            funct.gNewcon = self.gNewcon
            funct.quantidades_tentativas = self.quantidades_tentativas
            funct.faz = 'informar'
            html = funct.funct()  # retorna o html df
            if isinstance(html, str) and html == 'ERROR':
                print(f'TAREFA OBS: html == ERROR')
                return html, penulNIndex, penulCel1, penulCel2
            if html:
                dfSite = DfSite()
                dfSite.html = html
                dfSite.ultNIndex = self.ultNIndex
                dfSite.tag1 = self.tag1
                dfSite.tag2 = self.tag2
                dfSite.tag3 = self.tag3
                dfSite.tagCab = self.tagCab
                dfSite.texto1 = self.texto1
                dfSite.texto2 = self.texto2
                dfSite.texto3 = self.texto3
                dfSite.tratarModelo = self.tratarModelo
                dfSite.indTx1 = self.indTx1
                dfSite.indTx2 = self.indTx2
                dfSite.indTx3 = self.indTx3
                dfSite.indTx4 = self.indTx4
                htmlNew = dfSite.df()

                # não existe html e url
                if isinstance(htmlNew, str) and htmlNew == 'ERROR':
                    print(f'TAREFA OBS: htmlNew == ERROR')
                    return htmlNew, penulNIndex, penulCel1, penulCel2

                # descobrir se df esta sem informações
                numero_de_linhas = len(htmlNew)
                if numero_de_linhas == 1:
                    numero_bem = htmlNew.iat[0, 4]
                    numero_bem = str(numero_bem)
                    numero_bem = numero_bem.replace('\xa0', '')
                    numero_bem = numero_bem.replace(' ', '')
                    if numero_bem == '':
                        numero_bem = 0
                    # numero_bem = int(numero_bem)
                    # numero_bem = numero_bem.replace(' ', '')
                    # if numero_bem == '':
                    if numero_bem == 0:
                        return 'VAZIO', penulNIndex, penulCel1, penulCel2
            else:
                htmlNew = []

            try:  # quando não existe info na df ele gera erro
                self.ultNIndex = htmlNew.iat[-1, 0]   # ultima linha da primeira coluna(Index)
                # ultima linha da coluna definida colCel
                self.ultCel1 = htmlNew.iat[-1, int(self.colCel1)]
                # ultima linha da coluna definida colCel
                self.ultCel2 = htmlNew.iat[-1, int(self.colCel2)]
            except (ValueError, AttributeError, IndexError) as e:  # Tabela esta vazia!
                self.ultNIndex = penulNIndex
                self.ultCel1 = ''
                self.ultCel2 = ''
                contHtmlVazio += 1
                time.sleep(tempoEsperar)
                escreva2 = f'Exceção: {e.__class__.__name__}'
            # dfs atualizadas?
            if str(self.ultCel1) == str(penulCel1) and str(self.ultCel2) == str(penulCel2):
                self.ultNIndex = penulNIndex
            else:  # se diferente foi atualizad e esta correro
                penulNIndex = self.ultNIndex
                penulCel1 = self.ultCel1
                penulCel2 = self.ultCel2
                break
            log.pAL = self.pAL
            contHtmlErrado += 1
            if contHtmlErrado >= self.fator_repeticao:  # erro df não é atualizado
                escreva = 'TAREFA ERRO: Tabela não atualizar = df anterio '
                escreva += f'{str(contHtmlErrado)} vezes: {self.texto1} /'
                escreva += f'{self.texto2} / {self.texto3}'
                log.escreva = escreva
                log.escrever()
                break
            if contHtmlVazio >= self.testeVazio:   # erro não existe df
                escreva = f'TAREFA ERRO: Tabela vazia: {str(contHtmlVazio)} vezes {escreva2}: {self.texto1} / {self.texto2} / {self.texto3}'
                log.escreva = escreva
                log.escrever()
                break
            print(f'TAREFA OBS: Tempo de espera é {tempoEsperar} segundos.')
            print(f'TAREFA OBS: tempo contHtmlErrado {contHtmlErrado} e self.fator_repeticao {self.fator_repeticao}')  # noqa
            time.sleep(tempoEsperar)
            tempoEsperar *= 2  # fator para prologar a espera

        escreva = ''
        if self.texto1 is not None:
            escreva += '/' + self.texto1
        if self.texto2 is not None:
            escreva += '/' + self.texto2
        if self.texto3 is not None:
            escreva += '/' + self.texto3

        tempo.tpInicSeg = tpInicSegModelo
        tempo.tpInicSegProg = self.tpInicSegProg
        tempo.escreva = escreva
        tempo.pAL = self.pAL
        tempo.tempo_execucao()
        # Tempo(tpInicSeg=tpInicSegModelo, tpInicSegProg=self.tpInicSegProg,
        #       escreva=escreva, pAL=self.pAL).tempo_execucao()

        self.zera_variaveis()
        return htmlNew, self.ultNIndex, self.ultCel1, self.ultCel2

    def infoHTML(self):
        funct = Funct()
        if self.xpath_present_secreen:
            funct.xpath_present_secreen = self.xpath_present_secreen
        funct.faz = 'informar'
        funct.driver = self.driver
        funct.digitar = self.gNewcon
        funct.pAL = self.pAL
        funct.urls = [self.url]
        html = funct.funct()
        if html == 'ERROR':
            return html
        # Deu o erro linha abaixo -> TypeError: object of type 'bool' has no len()
        inf = BeautifulSoup(html, "lxml").find(text=True)
        return inf
