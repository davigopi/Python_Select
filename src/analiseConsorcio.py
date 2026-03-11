# flake8: noqa
# pyright: # type: ignore

import numpy as np
from typing import List, Dict, Union
from scipy.stats import norm


class AnaliseConsorcio:
    def __init__(self, months: List[List[float]], prazo: Union[int, str], realizadas: Union[int, str], **kwargs):
        if not months:
            raise ValueError("Você precisa fornecer ao menos um mês de dados.")

        months_ordenado = list(reversed(months))
        self.months = [np.array(m, dtype=float) for m in months_ordenado if len(m) > 0]

        if not self.months:
            raise ValueError("Todos os meses enviados estão vazios.")

        self.prazo = max(int(prazo), 1)
        self.realizadas = min(int(realizadas) + 1, self.prazo)
        self.metadata = kwargs

        self.cortes = np.array([np.min(m) for m in self.months])
        self.medianas = np.array([np.median(m) for m in self.months])
        self.medias_20 = np.array([self._media_percentual(m, 0.2) for m in self.months])

        self.tendencia_cortes = self._calcular_tendencia(self.cortes)
        self.tendencia_medianas = self._calcular_tendencia(self.medianas)

    def _media_percentual(self, mes: np.ndarray, percent: float) -> float:
        if mes.size == 0:
            return 0.0
        corte = np.percentile(mes, percent * 100)
        return float(np.mean(mes[mes <= corte]))

    def _calcular_tendencia(self, dados: np.ndarray) -> float:
        if len(dados) < 2:
            return 0.0
        x = np.arange(len(dados))
        slope, _ = np.polyfit(x, dados, 1)
        return float(slope)

    # 🔵 1 - Dispersão interna média dos meses
    def calcular_dispersao_media_mensal(self) -> float:
        return float(np.mean([np.std(m) for m in self.months]))

    # 🟢 2 - Índice de confiabilidade estatística da média
    def calcular_indice_confiabilidade_media(self, nivel: float = 0.95) -> float:
        if not self.months:
            return 0.0

        todos = np.concatenate(self.months)
        media = np.mean(todos)
        desvio = np.std(todos)
        n = len(todos)

        if n == 0 or media == 0:
            return 0.0

        z = norm.ppf((1 + nivel) / 2)
        margem = z * (desvio / np.sqrt(n))
        amplitude = 2 * margem

        return float(amplitude / media)

    def classificar_indice_confiabilidade_media(self, indice: float) -> str:
        if indice < 0.05:
            return "Alta Precisao"
        elif indice < 0.10:
            return "Precisao Moderada"
        return "Baixa Precisao"

    # 🔴 3 - Instabilidade real entre meses (mercado)
    def calcular_instabilidade_mensal(self) -> float:
        if len(self.medianas) < 2:
            return 0.0

        variacoes = []

        for i in range(1, len(self.medianas)):
            anterior = self.medianas[i - 1]
            atual = self.medianas[i]

            if anterior != 0:
                variacao = abs((atual - anterior) / anterior)
                variacoes.append(variacao)

        return float(np.mean(variacoes)) if variacoes else 0.0

    def classificar_instabilidade(self, instabilidade: float) -> str:
        if instabilidade < 0.03:
            return "Estavel"
        elif instabilidade < 0.08:
            return "Moderada"
        return "Instavel"

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
        return "Estabilidade"

    def classificar_grupo(self) -> float:
        return round((self.realizadas / self.prazo * 100), 2)

    # 🧠 Índice consolidado de risco
    def calcular_indice_risco(self) -> float:
        dispersao = self.calcular_dispersao_media_mensal()
        instabilidade = self.calcular_instabilidade_mensal()
        tendencia = abs(np.mean([self.tendencia_cortes, self.tendencia_medianas]))

        # Normalização simples
        return float((dispersao * 0.4) + (instabilidade * 100 * 0.4) + (tendencia * 0.2))

    def sugestao_lances(self) -> Dict[str, Union[str, float]]:
        nivel_maturidade_grupo = self.classificar_grupo()
        dispersao = self.calcular_dispersao_media_mensal()
        instabilidade = self.calcular_instabilidade_mensal()
        indice_confiabilidade = self.calcular_indice_confiabilidade_media()

        tendencia = np.mean([self.tendencia_cortes, self.tendencia_medianas])

        pesos = np.arange(1, len(self.medias_20) + 1)
        base = np.average(self.medias_20, weights=pesos)

        base_final = base + tendencia

        indice_risco = self.calcular_indice_risco()

        return {
            "Nivel_Maturidade_Grupo_Percentual": nivel_maturidade_grupo,
            "Tendencia": self.score_tendencia(),

            "Dispersao_Media_Mensal": round(dispersao, 2),

            "Indice_Confiabilidade_Media_Percentual": round(indice_confiabilidade * 100, 2),
            "Classificacao_Confiabilidade": self.classificar_indice_confiabilidade_media(indice_confiabilidade),

            "Instabilidade_Mensal_Percentual": round(instabilidade * 100, 2),
            "Classificacao_Instabilidade": self.classificar_instabilidade(instabilidade),

            "Indice_Risco_Grupo_Percentual": round(indice_risco, 2),

            "Sugestao_Agressiva_Percentual": round(base_final + dispersao, 2),
            "Sugestao_Equilibrada_Percentual": round(base_final, 2),
            "Sugestao_Conservadora_Percentual": round(base_final - dispersao, 2),

            **self.metadata
        }


if __name__ == "__main__":
    import main