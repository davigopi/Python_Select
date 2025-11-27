    def tratarDfNewcon(self):
        colunaExcluir = ['Cota', 'Filial', 'Bem', 'Modalidade']
        colunaGrupo = 'Grupo'
        colunaLance = 'Lance'
        colunaL = ''
        colunaLance1 = 'Lance1'
        colunaL1 = '1'
        colunaDt = 'Dt.contp'
        colunaDt2 = 'Dt.confm'
        colunaNova = 'GrupoDt'
        colunaNova2 = 'GrupoDt2'
        colunaDtNova = 'Dt'
        colunaDt2Nova = 'Dt2'
        textoVazio = ''
        linhaVazia = True 
        for coluna in colunaExcluir:
            if coluna == 'Modalidade':
                textoLinha = 'Sorteio'
                self.df = Tratar(df=self.df, coluna=coluna, textoLinha=textoLinha).dfLinhaExcluir()  # exclui linhas Sorteio da coluna modalidade
            self.df = Tratar(df=self.df, coluna=coluna).dfColunaExcluir()  # excluir coluna
        self.df = Tratar(df=self.df).dfColunaIndex()  # irar criar uma nova coluna index
        self.df = Tratar(df=self.df).dfColunaALterarNome()
        self.df = Tratar(df=self.df, coluna=colunaDt, colunaDtNova=colunaDtNova).dfColunaData()  # criar uma coluna data ano mes e dia
        self.df = Tratar(df=self.df, coluna=colunaDt2, colunaDtNova=colunaDt2Nova).dfColunaData()  # criar uma coluna data ano mes e dia
        self.df = Tratar(df=self.df, coluna=colunaGrupo, coluna2=colunaDtNova, colunaNova=colunaNova).dfColunaJuntar()  # juntar duas colunas e criando uma nova
        self.df = Tratar(df=self.df, coluna=colunaNova, coluna2=colunaDt2Nova, colunaNova=colunaNova2).dfColunaJuntar()  # """"
        self.df = Tratar(df=self.df, coluna=colunaLance).dfColunaConverterFloat()
        self.df = Tratar(df=self.df, coluna=colunaNova2, coluna2=colunaLance).dfColunaOrdenar()  # ordenar primeiro coluna segundo coluna2
        self.df = Tratar(df=self.df).dfColunaIndex()  # irar criar uma nova coluna index
        # self.df = Tratar(df=self.df, coluna=colunaLance).dfColunaPontaVirqula()  # ira alterar o ponto pela virgula (excel)
        self.df = Tratar(df=self.df, coluna=colunaNova2).dfLinhaRepetidaExcluir()  # exluir linhas repetidas 
        self.df = Tratar(df=self.df, coluna=colunaNova2, coluna2=colunaLance).dfLinhaJuntar()
        self.df = Tratar(df=self.df, coluna=colunaNova2, textoLinha=textoVazio).dfLinhaExcluir()
        self.df = Tratar(df=self.df).dfColunaIndex()
        colunaExcluir = [colunaNova, colunaDtNova, colunaNova2, colunaDt2Nova]
        for coluna in colunaExcluir:
            self.df = Tratar(df=self.df, coluna=coluna).dfColunaExcluir()  # excluir coluna  
        self.df = Tratar(df=self.df, coluna=colunaGrupo).dfLinhaRepetidaExcluir()  # exluir campo repetidos na linha
        # self.df = Tratar(df=self.df, coluna=colunaLance, coluna2=colunaL).dfColunaCriarUnicaLinha()   # criar colunas a partir -
        self.df = Tratar(df=self.df, coluna=colunaLance).dfColunaMover()  # mover para coluna nova a partir '-'
        self.df = Tratar(df=self.df, coluna=colunaLance).dfColunaExcluir()  # excluir coluna
        self.df = Tratar(df=self.df, coluna=colunaDt, coluna2=colunaDt2).dfDataIgual()  # compar as datas de Dt com Dt2 e apaga dt2 se igual
        self.df = Tratar(df=self.df, coluna=colunaDt).dfLinhaRepetidaExcluir()  # excluir linhas repetidas
        self.df = Tratar(df=self.df).dfColunaVazia()
        self.df, nUltCol = Tratar(df=self.df, coluna=colunaDt).dfColunaNUlt()
        self.df = Tratar(df=self.df, coluna=colunaGrupo, coluna2=colunaDt, nUltCol=nUltCol).dfColunaCriarMoverComColuna()  # move colua dtcontp 1ª vez linha grupo
        self.df, nUltCol = Tratar(df=self.df, coluna=colunaDt2).dfColunaNUlt()
        self.df = Tratar(df=self.df, coluna=colunaGrupo, coluna2=colunaDt2, nUltCol=nUltCol).dfColunaCriarMoverComColuna()  # move coluna dtcontm 1ª vez linha grupo
        self.df = Tratar(df=self.df, coluna=colunaGrupo, coluna2=colunaLance).dfColunaCriarMoverMuitasComColuna()  # move colunas lances a 1ª vez linha grupo
        while True:
            while True:
                self.df, nUltCol = Tratar(df=self.df, coluna=colunaDt2).dfColunaNUlt()
                # move coluna dtcontm 2ªou 3ª.. mesmo mes 1ª
                self.df, loop1 = Tratar(df=self.df, coluna=colunaGrupo, coluna2=colunaDt2, coluna3=colunaDt, nUltCol=nUltCol).dfColunaCriarMoverSemColuna3() 
                if loop1 is False:
                    break
                self.df, nUltCol = Tratar(df=self.df, coluna=colunaLance).dfColunaNUlt()
                self.df, nUltCol2 = Tratar(df=self.df, coluna=colunaDt2).dfColunaNUlt()
                # move coluna lance 2ªou 3ª.. mesmo mes 1ª
                self.df, lista = Tratar(df=self.df, coluna=colunaLance, coluna2=colunaDt2, nUltCol=nUltCol, nUltCol2=nUltCol2).dfColunaCriarMoverMuitasSemColuna() 
                self.df = Tratar(df=self.df, lista=lista).dfLinhaVaziaExcluir()  # excluirar todas as linhas que tiver na lista
                self.df = Tratar(df=self.df).dfColunaIndex()
            self.df, nUltCol = Tratar(df=self.df, coluna=colunaDt).dfColunaNUlt()
            self.df, loop2 = Tratar(df=self.df, coluna=colunaGrupo, coluna2=colunaDt, nUltCol=nUltCol).dfColunaCriarMoverSemColuna2()
            if loop2 is False:
                break
            self.df, nUltCol = Tratar(df=self.df, coluna=colunaDt2).dfColunaNUlt()
            self.df, loop2 = Tratar(df=self.df, coluna=colunaGrupo, coluna2=colunaDt2, coluna3=colunaDt, nUltCol=nUltCol).dfColunaCriarMoverSemColuna3()
            self.df, nUltCol = Tratar(df=self.df, coluna=colunaLance).dfColunaNUlt()
            self.df, nUltCol2 = Tratar(df=self.df, coluna=colunaDt).dfColunaNUlt()
            # move coluna lance 2ªou 3ª.. mesmo mes 1ª
            self.df, lista = Tratar(df=self.df, coluna=colunaLance, coluna2=colunaDt, nUltCol=nUltCol, nUltCol2=nUltCol2).dfColunaCriarMoverMuitasSemColuna()
            self.df = Tratar(df=self.df, lista=lista).dfLinhaVaziaExcluir()
            self.df = Tratar(df=self.df).dfColunaIndex()
        colunaExcluir = [colunaDt, colunaDt2, 'X', 'Separar']
        self.df, nUltCol = Tratar(df=self.df, coluna='X').dfColunaNUlt()
        for coluna in colunaExcluir:
            self.df = Tratar(df=self.df, coluna=coluna, nUltCol=nUltCol).dfColunaExcluir()  # excluir coluna
        return self.df