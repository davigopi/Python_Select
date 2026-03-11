# flake8: noqa
# pyright: # type: ignore
import time


class Log:
    def __init__(self, *args, **kwargs):
        self.write_log = kwargs.get('write_log')
        self.path_all_log = kwargs.get('path_all_log')

    def ler(self):
        with open(self.path_all_log, 'r', encoding='utf-8') as arquivo:
            return arquivo.read()

    def limpar(self):
        with open(self.path_all_log, 'w') as arquivo:
            arquivo.write('')

    def escrever(self):
        try:
            with open(self.path_all_log, 'a', encoding="utf-8") as arquivo:
                arquivo.write('\n' + self.write_log)
            # print(f'⛏️  LOG: escreveu ({self.write_log}) no caminho ({self.path_all_log})')
        except TypeError as e:
            print(f'❌ LOG: Error ({e}) ao tenta escrever ({self.write_log}) no caminho ({self.path_all_log})')


if __name__ == '__main__':
    log = Log()
    pasta = ''
    tabela = 'Tabelas/'
    logs = 'Logs/'
    arq_log = 'log'
    ext_Log = '.txt'

    p_log = pasta + logs
    path_all_log = p_log + arq_log + ext_Log

    log.path_all_log = path_all_log
    write_log = time.strftime("%H:%M:%S")
    log.write_log = write_log
    log.escrever()
    # Log(path_all_log=path_all_log).limpar()
    # Log(path_all_log=path_all_log, write_log=write_log).escrever()
