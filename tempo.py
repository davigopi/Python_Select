# flake8: noqa
# pyright: # type: ignore

import time
import os
from log import Log
from renomear import Renomear


class Tempo:
    def __init__(self, *args, tempo=60, **kwargs):
        self.tempo = tempo
        self.tpInicSeg = kwargs.get('tpInicSeg')
        self.tpInicSegProg = kwargs.get('tpInicSegProg')
        self.escreva = kwargs.get('escreva')
        self.pAL = kwargs.get('pAL')

    def contagem_regressiva(self):
        while self.tempo >= 0:
            print('------------------------------------')
            print(f'Tempo restante para termino: {self.tempo} seg')
            print('------------------------------------')
            self.tempo -= 1
            time.sleep(1)
            os.system('cls')
        return

    def tempo_execucao(self):
        tpMaxLog = 20
        if self.tpInicSeg is not None:
            tpFimSeg = (int(time.strftime("%H")) * 60 * 60) + (int(time.strftime("%M")) * 60) + int(time.strftime("%S"))  # noqa
            tpTotSeg = tpFimSeg - int(self.tpInicSeg)
            tpTotSegProg = tpFimSeg - int(self.tpInicSegProg)
            seg = tpTotSegProg % 60
            mt = int(((tpTotSegProg - seg) / 60) % 60)
            hora = int(((tpTotSegProg - (mt * 60) - seg) / (60**2)))
            total = str("%02d" % hora) + ':' + str("%02d" % mt) + ':' + str("%02d" % seg)
            if tpTotSeg >= tpMaxLog:  # tempo par gravar no log
                tpMinSeg = tpTotSeg
                tpSeg = tpMinSeg % 60
                tpMin = round((tpMinSeg - tpSeg) / 60)
                if self.escreva == 'fim':
                    self.escreva = 'TEMPO INFORMA: ' + total + ' tempo de execução em todo o programa'
                else:
                    self.escreva = 'ERRO TEMPO: ' + total + ' tempo de execução, passou: ' + \
                        str(tpMin) + ':' + str(tpSeg) + ' -> ' + self.escreva
                Log(pAL=self.pAL, escreva=self.escreva).escrever()
            # %s (de string) é para substituir uma string, %f (de float) é para substituir um float e %d (de integer) é para substituir um integer
        else:
            valor = int(time.strftime("%H")) * 60 * 60
            valor += int(time.strftime("%M")) * 60
            valor += int(time.strftime("%S"))
            return valor

    def tempo_arq(self):
        hora = int(time.strftime('%H')) + round(float(time.strftime('%M')) / 60, 2)
        data = time.strftime('-%y-%m-%d-')
        inf = data + str(hora)
        datahora = Renomear(inf=inf).tempo()
        return datahora


if __name__ == '__main__':
    datahora = tpInicSegProg = Tempo().tempo_arq()
    print(datahora)
