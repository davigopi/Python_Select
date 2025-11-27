# flake8: noqa
# pyright: # type: ignore
# # import time
# import sys
from funct import Funct
from log import Log
import random


class Botao:
    def __init__(self, *args, **kwargs):
        self.driver = kwargs.get('driver')
        self.texto = kwargs.get('texto')
        self.url = kwargs.get('url')
        self.pAL = kwargs.get('pAL')

    def botao1(self):
        contBotaoErro = 1
        vertical = -10  # variavel que meche na tela para encontrar o botao
        while True:
            tempo = 1 + random.random()
            retorno1 = False
            retorno2 = False

            if (contBotaoErro % 4) == 0:
                url = '//*[@id="divPasso1"]/div/div[2]/div/div[1]'
                faz = 'scroll'
                vertical = -2000
                Funct(driver=self.driver, urls=[url], faz=faz, vertical=vertical, tempo=tempo, pAL=self.pAL).funcao()
                vertical = 720
                Funct(driver=self.driver, urls=[url], faz=faz, vertical=vertical, tempo=tempo, pAL=self.pAL).funcao()
                vertical = -10
                escreva = f'BOTAO -> não visivel no site:({self.texto}) Nº vezes:({contBotaoErro}) divide 4 rest 0 -> Medida extrema, sacudir site!!!!!)'
                Log(escreva=escreva, pAL=self.pAL).escrever()

            url = '//*[@id="busca_andamento_modelo"]'
            faz = 'scroll'
            vertical *= 2
            Funct(driver=self.driver, urls=[url], faz=faz, vertical=vertical, tempo=tempo, pAL=self.pAL).funcao()  # levantar texto

            # retornar = True   , retornar=retornar
            retorno1 = Funct(driver=self.driver, urls=[self.url], tempo=tempo, pAL=self.pAL).funcao()  # clicar na caixa de opcao
            if retorno1 is True:
                faz = 'click_texto'
                Funct(driver=self.driver, urls=[self.texto], faz=faz, tempo=tempo, pAL=self.pAL).funcao()  # clicar na opcao

                url = '//*[@id="divPasso1"]/div/div[2]/div/div[5]/div[3]/div/input'
                # retornar = True     , retornar=retornar
                retorno2 = Funct(driver=self.driver, urls=[url], tempo=tempo, pAL=self.pAL).funcao()  # clicar botao

            if retorno2 is True:
                break
                # time.sleep(2)
            if contBotaoErro >= 15:
                escreva = f'BOTAO ERRO: não visivel no site:({self.texto}), url:({url}), Nº vezes: ({contBotaoErro}) ESGOTADO!!!'
                Log(escreva=escreva, pAL=self.pAL).escrever()
                break
            if contBotaoErro >= 2:
                escreva = f'BOTAO ALERTA: não visivel no site:({self.texto}) Nº vezes: ({contBotaoErro})'
                Log(escreva=escreva, pAL=self.pAL).escrever()
            contBotaoErro += 1
            # sys.exit()
