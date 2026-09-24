"""Atividade Avaliativa 3 - Estrutura de Dados II.

Central de Distribuicao de Pedidos: analise de quatro algoritmos.
Execute: python analise_ordenacao.py
Requer Python 3.10+ e utiliza somente a biblioteca padrao.

Convencoes:
  C: comparacoes entre valores, incluindo resultados verdadeiros e falsos.
  T: trocas entre duas posicoes distintas (mesmo se os valores forem iguais).
  M: escritas em posicoes do vetor; cada troca realiza duas escritas.
  C + M: custo didatico comum; nao e tempo de execucao nem total de instrucoes.

Nao contam: testes de indices/lacos, leituras, variaveis auxiliares, pilha,
geracao de entradas, copias, preparacao dos cenarios e validacao da saida.
"""

from __future__ import annotations

import csv
import json
import platform
import random
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Callable


TAMANHOS = (10, 20, 1000)
LIMITE_MINIMO = 1
LIMITE_MAXIMO = 10000


@dataclass
class Metricas:
    """Contadores de uma unica execucao do algoritmo."""

    comparacoes: int = 0
    trocas: int = 0
    movimentacoes: int = 0

    @property
    def total(self) -> int:
        """Nao soma trocas novamente: suas escritas ja estao em M."""
        return self.comparacoes + self.movimentacoes


def trocar(vetor: list[int], i: int, j: int, metricas: Metricas) -> None:
    """Troca indices distintos e conta uma troca e duas escritas no vetor."""
    if i != j:  # Comparacao de indices: nao entra em C.
        vetor[i], vetor[j] = vetor[j], vetor[i]
        metricas.trocas += 1
        metricas.movimentacoes += 2


def bubble_sort(vetor: list[int]) -> Metricas:
    """Bubble Sort com limite decrescente e parada se nao houver troca."""
    metricas = Metricas()
    for fim in range(len(vetor) - 1, 0, -1):
        houve_troca = False
        for j in range(fim):
            metricas.comparacoes += 1
            if vetor[j] > vetor[j + 1]:
                trocar(vetor, j, j + 1, metricas)
                houve_troca = True
        if not houve_troca:
            break
    return metricas


def insertion_sort(vetor: list[int]) -> Metricas:
    """Insertion Sort por deslocamento, sem trocas entre pares."""
    metricas = Metricas()
    for i in range(1, len(vetor)):
        chave = vetor[i]  # Leitura/variavel auxiliar: nao conta como M.
        j = i - 1
        while j >= 0:
            # So incrementa C se a comparacao entre valores for avaliada.
            # A ultima comparacao falsa tambem conta; j >= 0 nao conta.
            metricas.comparacoes += 1
            if vetor[j] > chave:
                vetor[j + 1] = vetor[j]
                metricas.movimentacoes += 1
                j -= 1
            else:
                break
        vetor[j + 1] = chave
        # Conta a escrita final mesmo que a chave fique na posicao original.
        metricas.movimentacoes += 1
    return metricas


def selection_sort(vetor: list[int]) -> Metricas:
    """Selection Sort: procura o menor e evita troca de um indice consigo."""
    metricas = Metricas()
    for i in range(len(vetor) - 1):
        menor = i
        for j in range(i + 1, len(vetor)):
            metricas.comparacoes += 1
            if vetor[j] < vetor[menor]:
                menor = j
        trocar(vetor, i, menor, metricas)
    return metricas


def particionar(
    vetor: list[int], inicio: int, fim: int, metricas: Metricas
) -> int:
    """Lomuto: ultimo elemento como pivo, comparacao <= e sem autotrocas."""
    pivo = vetor[fim]
    i = inicio - 1
    for j in range(inicio, fim):
        metricas.comparacoes += 1
        if vetor[j] <= pivo:
            i += 1
            trocar(vetor, i, j, metricas)
    trocar(vetor, i + 1, fim, metricas)
    return i + 1


def quick_sort(vetor: list[int]) -> Metricas:
    """Quick Sort com pilha explicita: nao depende do limite de recursao.

    A pilha substitui as chamadas recursivas e preserva a ordenacao por
    particionamento. Isso evita RecursionError nos cenarios degenerados,
    mas nao elimina o pior caso quadratico causado pela escolha do pivo.
    """
    metricas = Metricas()
    if len(vetor) < 2:
        return metricas
    pilha = [(0, len(vetor) - 1)]
    while pilha:
        inicio, fim = pilha.pop()
        posicao_pivo = particionar(vetor, inicio, fim, metricas)
        # Empilha apenas intervalos com pelo menos dois elementos.
        # Direita primeiro: a esquerda sera processada antes (pilha LIFO).
        if posicao_pivo + 1 < fim:
            pilha.append((posicao_pivo + 1, fim))
        if inicio < posicao_pivo - 1:
            pilha.append((inicio, posicao_pivo - 1))
    return metricas


ALGORITMOS: dict[str, Callable[[list[int]], Metricas]] = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Selection Sort": selection_sort,
    "Quick Sort": quick_sort,
}


@dataclass
class Resultado:
    tamanho: int
    cenario: str
    algoritmo: str
    comparacoes: int
    trocas: int
    movimentacoes: int
    total: int


def gerar_bases() -> dict[int, list[int]]:
    """Semeia uma vez e gera 10, depois 20, depois 1000 valores."""
    random.seed(42)
    return {
        tamanho: [random.randint(LIMITE_MINIMO, LIMITE_MAXIMO)
                  for _ in range(tamanho)]
        for tamanho in TAMANHOS
    }


def criar_cenarios(base: list[int]) -> dict[str, list[int]]:
    """Tres organizacoes do MESMO multiconjunto, inclusive repeticoes."""
    return {
        "Aleatorio": base.copy(),
        "Ordenado": sorted(base),
        "Inverso": sorted(base, reverse=True),
    }


def executar_experimentos(
    bases: dict[int, list[int]],
) -> list[Resultado]:
    """Executa 3 tamanhos x 3 cenarios x 4 algoritmos = 36 ordenacoes."""
    resultados = []
    for tamanho, base in bases.items():
        esperado = sorted(base)  # Referencia de validacao, fora da contagem.
        for cenario, entrada in criar_cenarios(base).items():
            for nome, algoritmo in ALGORITMOS.items():
                copia = entrada.copy()  # Isonomia: cada algoritmo recebe a mesma entrada.
                metricas = algoritmo(copia)
                if copia != esperado:
                    raise RuntimeError(
                        f"Falha na ordenacao: {nome}, {cenario}, n={tamanho}"
                    )
                resultados.append(Resultado(
                    tamanho=tamanho,
                    cenario=cenario,
                    algoritmo=nome,
                    comparacoes=metricas.comparacoes,
                    trocas=metricas.trocas,
                    movimentacoes=metricas.movimentacoes,
                    total=metricas.total,
                ))
    return resultados


def numero(valor: int) -> str:
    """Separador de milhares usado nas tabelas em portugues."""
    return f"{valor:,}".replace(",", ".")


def tabela_markdown(resultados: list[Resultado]) -> str:
    linhas = [
        "| n | Cenario | Algoritmo | C | T | M | C + M |",
        "| ---: | :--- | :--- | ---: | ---: | ---: | ---: |",
    ]
    for r in resultados:
        linhas.append(
            f"| {numero(r.tamanho)} | {r.cenario} | {r.algoritmo} | "
            f"{numero(r.comparacoes)} | {numero(r.trocas)} | "
            f"{numero(r.movimentacoes)} | {numero(r.total)} |"
        )
    return "\n".join(linhas)


def relatorio_tabelas(resultados: list[Resultado]) -> str:
    partes = [
        "# Resultados da execucao",
        "C = comparacoes entre valores; T = trocas entre indices distintos; "
        "M = escritas no vetor. Cada troca acrescenta 2 a M. "
        "Insertion Sort desloca valores e, por isso, tem T = 0.",
        "C + M e um custo didatico; nao mede tempo. "
        "Nao some T novamente, pois suas escritas ja fazem parte de M.",
        "## Etapa 3 - Vetores aleatorios",
        tabela_markdown([r for r in resultados if r.cenario == "Aleatorio"]),
        "## Desafio adicional - Tres cenarios",
    ]
    for tamanho in TAMANHOS:
        partes.extend([
            f"### {numero(tamanho)} elementos",
            tabela_markdown([r for r in resultados if r.tamanho == tamanho]),
        ])
    return "\n\n".join(partes) + "\n"


def salvar_resultados(
    bases: dict[int, list[int]], resultados: list[Resultado], pasta: Path
) -> None:
    """Salva entradas e metricas reais em formatos abertos e auditaveis."""
    pasta.mkdir(parents=True, exist_ok=True)
    registros = [asdict(r) for r in resultados]
    with (pasta / "resultados.csv").open("w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=list(registros[0]))
        escritor.writeheader()
        escritor.writerows(registros)
    (pasta / "resultados.json").write_text(
        json.dumps(registros, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (pasta / "vetores_base.json").write_text(
        json.dumps(bases, indent=2) + "\n", encoding="utf-8"
    )
    (pasta / "ambiente.json").write_text(json.dumps({
        "python": platform.python_version(),
        "implementacao": platform.python_implementation(),
        "semente": 42,
        "tamanhos_na_ordem_de_geracao": list(TAMANHOS),
        "gerador": "random.randint(1, 10000), extremos inclusivos",
        "repeticoes_por_combinacao": 1,
        "quantidade_de_execucoes": len(resultados),
        "validacao": "Todas as saidas coincidiram com sorted(base).",
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (pasta / "tabelas.md").write_text(relatorio_tabelas(resultados), encoding="utf-8")


def main() -> None:
    bases = gerar_bases()
    resultados = executar_experimentos(bases)
    pasta = Path(__file__).resolve().parent / "resultados"
    salvar_resultados(bases, resultados, pasta)
    print(relatorio_tabelas(resultados))
    print(f"Validacao concluida: {len(resultados)} ordenacoes corretas.")
    print(f"Arquivos salvos em: {pasta}")


if __name__ == "__main__":
    main()
