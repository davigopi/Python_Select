import numpy as np  # numpy = biblioteca para matemática vetorizada e estatística
from typing import List, Dict, Union, Tuple  # Tipagem estática para organizar tipos esperados
from scipy.stats import norm  # fornece funções da distribuição normal (estatística)


class AnaliseConsorcio:
    def __init__(self, months: List[List[float]], prazo: Union[int, str], realizadas: Union[int, str], **kwargs):
        if not months:
            raise ValueError("Você precisa fornecer ao menos um mês de dados.")

        # Inverte a ordem para trabalhar internamente do mais antigo para o mais recente
        months_ordenado = list(reversed(months))

        # Converte lista comum em array numérico otimizado
        self.months = [np.array(m, dtype=float) for m in months_ordenado if len(m) > 0]

        if not self.months:
            raise ValueError("Todos os meses enviados estão vazios.")

        self.prazo = max(int(prazo), 1)
        self.realizadas = min(int(realizadas) + 1, self.prazo)
        self.metadata = kwargs

        # Pega o menor valor do array
        self.cortes = np.array([np.min(m) for m in self.months])

        # Calcula o valor central do array
        self.medianas = np.array([np.median(m) for m in self.months])
        self.medias_20 = np.array([self._media_percentual(m, 0.2) for m in self.months])

        # Calcula tendência uma única vez para evitar recalcular depois
        self.tendencia_cortes = self._calcular_tendencia(self.cortes)
        self.tendencia_medianas = self._calcular_tendencia(self.medianas)

    def _media_percentual(self, mes: np.ndarray, percent: float) -> float:
        if mes.size == 0:
            return 0.0
        # Encontra o valor que separa X% dos menores dados
        corte = np.percentile(mes, percent * 100)
        # calcula média aritmética
        return float(np.mean(mes[mes <= corte]))

    def _calcular_tendencia(self, dados: np.ndarray) -> float:
        if len(dados) < 2:
            return 0.0
        # cria sequência numérica [0,1,2,...] (0 = mais antigo, N = mais recente)
        x = np.arange(len(dados))
        # ajusta uma reta (regressão linear) retorna coeficientes da equação dessa reta
        slope, _ = np.polyfit(x, dados, 1)
        return float(slope)

    def calcular_volatilidade(self) -> float:
        # Calcula desvio padrão (volatilidade estatística)
        return float(np.mean([np.std(m) for m in self.months]))

    # Calcula o nível de oscilação da média dos lances
    def calcular_oscilacao(self, nivel: float = 0.95) -> float:
        if not self.months:
            return 0.0

        # junta vários arrays em um único array
        todos = np.concatenate(self.months)

        media = np.mean(todos)
        desvio = np.std(todos)
        n = len(todos)

        if n == 0 or media == 0:
            return 0.0

        # norm.ppf calcula o valor crítico Z da distribuição normal baseado no nível de confiança informado (ex: 95%)
        z = norm.ppf((1 + nivel) / 2)

        # calcula raiz quadrada
        margem = z * (desvio / np.sqrt(n))

        # amplitude do intervalo = 2 * margem
        amplitude = 2 * margem

        # percentual de oscilação em relação à média
        oscilacao = amplitude / media

        return float(oscilacao)

    def classificar_oscilacao(self, oscilacao: float) -> str:
        if oscilacao < 0.05:
            return "Pouca"
        elif oscilacao < 0.10:
            return "Normal"
        return "Grande"

    def score_tendencia(self) -> str:
        slope = self.tendencia_cortes
        if slope < -0.1:
            return "Queda Forte"
        elif slope < 0:
            return "Queda"
        elif slope > 0.1:
            return "Alta Forte"
        elif slope > 0:
            return "Alta"
        else:
            return "Estabilidade"

    def classificar_grupo(self) -> str:
        percentual = self.realizadas / self.prazo
        if percentual < 0.15:
            return "Novo"          
        elif percentual <= 0.30:
            return "Em formação"  
        elif percentual <= 0.55:
            return "Intermediário" 
        elif percentual <= 0.78:
            return "Maduro"   
        return "Encerramento"   

    # Retorna um dicionário com chave string e valor podendo ser string OU float
    def sugestao_lances(self) -> Dict[str, Union[str, float]]:
        status = self.classificar_grupo()
        volatilidade = self.calcular_volatilidade()

        tendencia = np.mean([
            self.tendencia_cortes,
            self.tendencia_medianas
        ])

        # usado aqui para criar pesos crescentes (meses mais recentes têm maior peso)
        pesos = np.arange(1, len(self.medias_20) + 1)

        # permite média ponderada
        base = np.average(self.medias_20, weights=pesos)

        base_final = base + tendencia

        ajustes = {
            "Novo": volatilidade * 0.5,
            "Intermediário": 0.0,
            "Antigo": -(volatilidade * 0.3)
        }

        base_final += ajustes.get(status, 0)

        oscilacao = self.calcular_oscilacao()
        classificacao_oscilacao = self.classificar_oscilacao(oscilacao)
        oscilacao_str = str(round(oscilacao * 100, 2)) + '%'
        volatilidade_str = str(round(volatilidade, 2)) + '%'
        
        return {
            "Duracao": status + ', ' + str(self.realizadas) + 'ª de ' + str(self.prazo),
            "Tendencia": self.score_tendencia(),
            "Oscilacao_Media_Lances": classificacao_oscilacao + ' de ' + oscilacao_str,
            "Volatilidade": volatilidade_str,
            "Sugestao_Agressiva": round(base_final + volatilidade, 2),
            "Sugestao_Equilibrada": round(base_final, 2),
            "Sugestao_Conservadora": round(base_final - volatilidade, 2),
            **self.metadata
        }

# --- Exemplo de Uso ---
if __name__ == "__main__":
    import main