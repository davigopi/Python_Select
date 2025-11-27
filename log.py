# flake8: noqa
# pyright: # type: ignore
import time


class Log:
    def __init__(self, *args, **kwargs):
        self.escreva = kwargs.get('escreva')
        self.pAL = kwargs.get('pAL')

    def ler(self):
        with open(self.pAL, 'r', encoding='utf-8') as arquivo:
            return arquivo.read()

    def limpar(self):
        with open(self.pAL, 'w') as arquivo:
            arquivo.write('')

    def escrever(self):
        try:
            with open(self.pAL, 'a') as arquivo:
                arquivo.write('\n' + self.escreva)
        except TypeError as e:
            text = f'LOG ERROR: (({e})) o pAL é: (({self.pAL})) '
            text += f'o escreva é: (({self.escreva}))'
            print(text)


if __name__ == '__main__':
    log = Log()
    pasta = ''
    tabela = 'Tabelas/'
    logs = 'Logs/'
    arq_log = 'log'
    ext_Log = '.txt'

    p_log = pasta + logs
    pAL = p_log + arq_log + ext_Log

    log.pAL = pAL
    escreva = time.strftime("%H:%M:%S")
    log.escreva = escreva
    log.escrever()
    # Log(pAL=pAL).limpar()
    # Log(pAL=pAL, escreva=escreva).escrever()
