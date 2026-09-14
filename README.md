# 📊 Análise de Algoritmos de Ordenação em Python

## 📌 Descrição

Projeto acadêmico desenvolvido na disciplina de **Estrutura de Dados II**, utilizando Python para implementar e analisar algoritmos de ordenação aplicados ao contexto de uma **Central de Distribuição de Pedidos**.

O projeto compara **Bubble Sort, Insertion Sort, Selection Sort e Quick Sort**, observando como o tamanho e a organização inicial dos dados influenciam a quantidade de comparações, trocas e movimentações realizadas durante a ordenação.

## 🎯 Objetivo

Aplicar conceitos de estruturas de dados e análise de algoritmos por meio da implementação prática de quatro métodos de ordenação, comparando seu comportamento experimental com as respectivas complexidades teóricas.

Também é objetivo garantir condições iguais de teste, utilizando uma semente fixa e cópias idênticas de cada vetor, além de avaliar os algoritmos em três cenários: dados aleatórios, já ordenados e em ordem inversa.

## 🎓 Identificação acadêmica

| Identificação | Informação |
| :--- | :--- |
| Aluno | Dhiogo Martins Antônio da Silva |
| Professora | Karla Roberto Sartin |
| Curso | Engenharia de Software |
| Instituição | Centro Universitário do Distrito Federal - UDF |
| Ano | 2026 |

## 🛠️ Tecnologias utilizadas

- Python 3.10 ou superior
- Biblioteca padrão do Python
- Módulo `random` para geração reproduzível dos vetores
- Módulos `csv` e `json` para exportação dos resultados
- `unittest` para validação automatizada

## ⚙️ Funcionalidades

- Implementação do Bubble Sort com parada antecipada
- Implementação do Insertion Sort por deslocamentos
- Implementação do Selection Sort
- Implementação do Quick Sort com partição de Lomuto
- Contagem individual de comparações, trocas e movimentações
- Geração de vetores com 10, 20 e 1.000 elementos
- Uso de `random.seed(42)` para reprodução do experimento
- Utilização de cópias idênticas para garantir igualdade entre os testes
- Comparação de vetores aleatórios, ordenados e inversos
- Validação de todas as ordenações com `sorted()`
- Exibição automática das tabelas no terminal
- Exportação dos resultados em CSV, JSON e Markdown
- Testes automatizados para conferir a ordenação e os contadores

## 🧩 Estrutura do projeto

O trabalho foi organizado nas etapas propostas pela atividade avaliativa.

### 🔹 Implementação dos algoritmos

Os quatro algoritmos foram implementados manualmente em Python. Cada função ordena o vetor recebido e retorna as métricas coletadas durante sua execução.

### 🔹 Preparação dos experimentos

São gerados vetores aleatórios de **10, 20 e 1.000 elementos**. Cada algoritmo recebe uma cópia da mesma entrada por meio de `.copy()`, evitando que a execução de um algoritmo altere os dados utilizados pelos seguintes.

### 🔹 Contagem das operações

O experimento diferencia comparações entre valores, trocas entre posições e escritas realizadas no vetor. Essa separação permite comparar corretamente algoritmos que trabalham por troca com o Insertion Sort, que trabalha principalmente por deslocamentos.

### 🔹 Análise dos resultados

As tabelas apresentam as métricas obtidas na execução. Em seguida, são respondidas as questões analíticas de **a até i**, relacionando os resultados observados às complexidades Big-O.

### 🔹 Desafio adicional

Os quatro algoritmos também são avaliados com os mesmos valores em três organizações iniciais: aleatória, crescente e inversa. O desafio evidencia que a organização da entrada não afeta todos os algoritmos da mesma forma.

## 📚 Aprendizados

- Implementação manual de algoritmos de ordenação em Python
- Diferença entre comparações, trocas e movimentações
- Análise das complexidades O(n), O(n log n) e O(n²)
- Influência da organização inicial dos dados
- Importância da escolha do pivô no Quick Sort
- Uso de sementes fixas em experimentos reproduzíveis
- Garantia de igualdade entre testes com cópias dos vetores
- Validação automatizada de algoritmos e métricas
- Exportação de resultados para diferentes formatos
- Interpretação de resultados experimentais sem confundi-los com tempo de execução

## ▶️ Como executar

Requer **Python 3.10 ou superior**. Não é necessário instalar bibliotecas adicionais.

1. Baixe ou clone o repositório e abra um terminal na pasta do projeto.
2. Execute:

```bash
python analise_ordenacao.py
```

No Windows, também é possível usar `py analise_ordenacao.py`; em ambientes que disponibilizam o comando `python3`, use `python3 analise_ordenacao.py`.

O programa exibe as tabelas, verifica as **36 ordenações** contra `sorted(base)` e salva os arquivos da pasta `resultados/`. Cada nova execução substitui os resultados anteriores com as métricas do experimento reproduzido. A execução que originou estas tabelas utilizou **CPython 3.12.14**.

Para executar os testes de correção e de contagem:

```bash
python -m unittest discover -s tests -v
```

## 📁 Arquivos do repositório

```text
Analise-de-Algoritmos-de-Ordenacao-Python/
├── analise_ordenacao.py         # Código completo e executável
├── README.md                   # Metodologia, tabelas e respostas
├── .gitignore
├── tests/
│   └── test_analise_ordenacao.py # Auditoria independente dos contadores
└── resultados/
    ├── ambiente.json           # Versão do Python e parâmetros
    ├── vetores_base.json       # Todas as entradas aleatórias utilizadas
    ├── resultados.csv          # As 36 medições em formato tabular
    ├── resultados.json         # As mesmas medições em JSON
    └── tabelas.md              # Tabelas geradas automaticamente
```

## Etapa 1 - Código Python e preparação das entradas

O arquivo [analise_ordenacao.py](analise_ordenacao.py) contém a implementação completa. Sua reprodução abaixo permite consultar o trabalho diretamente pelo README.

<details>
<summary><strong>Abrir o código Python completo e comentado</strong></summary>

```python
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
```

</details>

### Reprodutibilidade e isonomia

- A chamada **`random.seed(42)` ocorre uma única vez**, antes da geração das bases.
- Os tamanhos são gerados na ordem **10, 20 e 1.000**, consumindo a mesma sequência do gerador. Não se reinicializa a semente para cada tamanho ou algoritmo.
- Cada valor é obtido com **`random.randint(1, 10000)`**, incluindo os dois extremos. São permitidos valores repetidos.
- Cada algoritmo recebe **`entrada.copy()`** e inicia com contadores zerados. Assim, a ordenação anterior não altera a entrada do algoritmo seguinte.
- Os cenários ordenado e inverso derivam da mesma base aleatória de cada tamanho. Mudam somente a organização, preservando os valores e suas quantidades.
- `sorted()` serve apenas para preparar os cenários e validar a saída. Nenhum dos quatro algoritmos usa uma ordenação pronta para implementar sua lógica.
- São executadas **3 × 3 × 4 = 36 combinações**, uma vez cada. A atividade principal corresponde às 12 medições aleatórias; o desafio as reutiliza e acrescenta as 24 medições das outras organizações.

Base de 10 elementos:

```text
[1825, 410, 4507, 4013, 3658, 2287, 1680, 8936, 1425, 9675]
```

Base de 20 elementos:

```text
[6913, 521, 489, 1536, 3583, 3812, 8280, 9864, 435, 9196,
 3258, 8929, 6874, 3612, 7360, 9655, 4558, 107, 2616, 6925]
```

A base completa de 1.000 elementos está em [resultados/vetores_base.json](resultados/vetores_base.json). Guardar as entradas permite reproduzir exatamente o experimento mesmo se um ambiente apresentar diferenças na geração de números pseudoaleatórios.

## Etapa 2 - Critério exato de contagem

### Medidas comuns

| Símbolo | O que é contado |
| :---: | :--- |
| **C** | Cada comparação efetivamente avaliada entre valores do vetor ou entre um valor e a chave/pivô. Tanto resultados verdadeiros quanto falsos contam. |
| **T** | Cada troca entre duas posições distintas do vetor. Trocas entre posições distintas com valores iguais também contam. Uma tentativa de trocar um índice consigo mesmo é ignorada e não executa escritas. |
| **M** | Cada escrita em uma posição do vetor. Uma troca executa duas escritas, portanto acrescenta **2 a M**. |
| **C + M** | Soma didática das comparações com as escritas no vetor, usada para comparar a quantidade de operações contabilizadas na mesma unidade. |

Não entram na contagem testes de índices e laços, leituras, atribuições a variáveis auxiliares, manipulação da pilha, geração dos dados, cópias, preparação dos cenários, validação e exportação. Por exemplo, guardar a chave do Insertion Sort em uma variável não incrementa M.

**C + M não representa tempo de execução nem todas as instruções executadas pelo Python.** Também não se soma T novamente: as duas escritas de cada troca já estão incluídas em M. Esta convenção usa escritas no vetor como movimentações; não usa a convenção alternativa de três atribuições por troca que inclui uma variável temporária.

### Regras por algoritmo

| Algoritmo | Comparação contada | Trocas e movimentações | Variante utilizada |
| :--- | :--- | :--- | :--- |
| Bubble Sort | Cada `vetor[j] > vetor[j + 1]`. | Cada troca de vizinhos soma 1 a T e 2 a M. | Limite interno decrescente e parada antecipada quando uma passagem não realiza trocas. |
| Insertion Sort | Cada `vetor[j] > chave`, inclusive a última avaliação falsa. Se `j < 0`, não existe comparação entre valores a contar. | Cada deslocamento soma 1 a M; a colocação final da chave soma 1 a M, mesmo se permanecer no mesmo lugar. T é sempre zero nesta implementação. | Inserção por deslocamentos, sem troca entre pares. |
| Selection Sort | Cada `vetor[j] < vetor[menor]`. | A troca final só acontece se `menor != i`: soma 1 a T e 2 a M. | Busca completa pelo menor no trecho ainda não ordenado. |
| Quick Sort | Cada `vetor[j] <= pivo`. | Trocas na partição e na colocação do pivô somam 1 a T e 2 a M quando os índices são distintos. | Partição de Lomuto, último elemento como pivô e pilha explícita. |

**A coluna M permite comparar o trabalho de movimentação dos quatro algoritmos.** O zero na coluna T do Insertion Sort indica que ele trabalha por deslocamentos, não que não movimente dados.

A pilha explícita do Quick Sort substitui as chamadas recursivas e evita `RecursionError` nas entradas de 1.000 elementos. Ela **não corrige o pior caso quadrático** causado por partições desequilibradas.

## Etapa 3 - Tabela de resultados

Resultados para os vetores **aleatórios**, medidos pela execução do programa. O ponto nas tabelas separa milhares.

| n | Algoritmo | Comparações (C) | Trocas (T) | Movimentações (M) | C + M |
| ---: | :--- | ---: | ---: | ---: | ---: |
| 10 | Bubble Sort | 44 | 19 | 38 | 82 |
| 10 | Insertion Sort | 27 | 0 | 28 | 55 |
| 10 | Selection Sort | 45 | 7 | 14 | 59 |
| 10 | Quick Sort | 29 | 7 | 14 | 43 |
| 20 | Bubble Sort | 189 | 84 | 168 | 357 |
| 20 | Insertion Sort | 99 | 0 | 103 | 202 |
| 20 | Selection Sort | 190 | 16 | 32 | 222 |
| 20 | Quick Sort | 58 | 28 | 56 | 114 |
| 1.000 | Bubble Sort | 499.122 | 239.681 | 479.362 | 978.484 |
| 1.000 | Insertion Sort | 240.670 | 0 | 240.680 | 481.350 |
| 1.000 | Selection Sort | 499.500 | 992 | 1.984 | 501.484 |
| 1.000 | Quick Sort | 10.385 | 4.543 | 9.086 | 19.471 |

## Etapa 4 - Respostas analíticas

### a) Qual algoritmo realizou o menor número de comparações para 10 elementos?

O **Insertion Sort**, com **27 comparações**. O Quick Sort realizou 29, o Bubble Sort 44 e o Selection Sort 45. Uma complexidade média melhor não garante a menor contagem para toda entrada pequena: a ordem concreta dos valores e o particionamento influenciam o resultado.

### b) Qual algoritmo realizou menos trocas ou movimentações?

Para **10 elementos**, **Selection Sort e Quick Sort empataram**, com **7 trocas e 14 movimentações** cada. O Insertion Sort realizou 28 movimentações e o Bubble Sort 38.

Para **20 elementos**, o Selection Sort realizou menos movimentações: **32**, contra 56 do Quick, 103 do Insertion e 168 do Bubble. Para **1.000 elementos**, o Selection também teve o menor número: **1.984**, contra 9.086 do Quick, 240.680 do Insertion e 479.362 do Bubble.

Literalmente, o Insertion Sort tem zero trocas entre pares em todos os testes, pois desloca os valores. Por isso, a resposta comparativa usa **M**, a medida comum de escritas no vetor, e não interpreta esse zero como ausência de trabalho.

### c) O comportamento observado para 10 elementos permaneceu semelhante quando o tamanho aumentou para 20?

**Parcialmente.** O menor número de comparações passou do Insertion Sort para o Quick Sort: com 20 elementos, o Quick fez **58**, enquanto o Insertion fez **99**. O empate entre Quick e Selection em movimentações também deixou de ocorrer: o Selection passou a realizar menos escritas.

Por outro lado, a ordem pelo custo **C + M** permaneceu **Quick, Insertion, Selection e Bubble**. O Quick passou de 43 para 114, o Insertion de 55 para 202, o Selection de 59 para 222 e o Bubble de 82 para 357.

### d) O que aconteceu com a quantidade de operações quando o vetor passou para 1.000 elementos?

A quantidade cresceu fortemente, principalmente nos algoritmos quadráticos. Com 1.000 elementos, o custo **C + M** foi **978.484 no Bubble**, **481.350 no Insertion**, **501.484 no Selection** e **19.471 no Quick**.

De 20 para 1.000 elementos, a entrada cresceu **50 vezes**. O custo contado cresceu aproximadamente **2.740,85 vezes no Bubble**, **2.382,92 no Insertion**, **2.258,94 no Selection** e **170,80 no Quick**. Os fatores não precisam ser exatamente 2.500, pois são entradas aleatórias distintas e os termos de menor ordem têm maior peso no tamanho 20. Esses fatores descrevem as contagens, não uma medição de velocidade.

### e) Bubble Sort, Insertion Sort e Selection Sort são O(n²) em situações típicas. Eles apresentaram exatamente a mesma quantidade de operações?

**Não.** Para 1.000 elementos aleatórios, o Bubble fez **499.122 comparações e 479.362 escritas**; o Insertion fez **240.670 comparações e 240.680 escritas**; e o Selection fez **499.500 comparações e 1.984 escritas**.

A notação O(n²) descreve um limite assintótico de crescimento, sem fixar constantes ou contagens exatas. Nesta implementação, o Selection sempre compara todos os candidatos e faz exatamente **n(n − 1)/2 comparações**, mas no máximo **n − 1 trocas**. O Bubble usa trocas de vizinhos e pode parar antes. O Insertion desloca somente os valores maiores que a chave, aproveitando a ordem já existente.

Nesta base, existem **239.681 inversões estritas**: pares de posições `i < j` em que `base[i] > base[j]`. O Bubble precisa de uma troca por inversão, produzindo **2 × 239.681 = 479.362 escritas**. O Insertion faz **239.681 deslocamentos + 999 colocações de chave = 240.680 escritas**. Isso explica uma diferença concreta entre algoritmos da mesma classe de crescimento.

### f) Qual algoritmo apresentou maior crescimento no número de operações?

Usando o critério comum **C + M**, o **Bubble Sort** apresentou o maior crescimento, tanto absoluto quanto proporcional, no aumento de **20 para 1.000 elementos**.

| Algoritmo | C + M com 20 | C + M com 1.000 | Aumento absoluto | Fator aproximado |
| :--- | ---: | ---: | ---: | ---: |
| Bubble Sort | 357 | 978.484 | 978.127 | 2.740,85 vezes |
| Insertion Sort | 202 | 481.350 | 481.148 | 2.382,92 vezes |
| Selection Sort | 222 | 501.484 | 501.262 | 2.258,94 vezes |
| Quick Sort | 114 | 19.471 | 19.357 | 170,80 vezes |

A mesma conclusão para C + M vale de 10 para 1.000 elementos. A métrica deve ser explicitada: **se fossem consideradas somente as comparações e seu aumento absoluto**, de 20 para 1.000 o Selection teria o maior aumento, **499.310**, contra **498.933** do Bubble.

### g) Como o comportamento experimental do Quick Sort se diferenciou dos demais algoritmos?

Nos dados aleatórios, o Quick Sort dividiu o problema em partições e apresentou crescimento muito menor no maior tamanho. Com **1.000 elementos**, realizou **10.385 comparações**, enquanto os outros algoritmos ficaram entre **240.670 e 499.500**.

Seu custo C + M, **19.471**, foi cerca de **50,25 vezes menor que o do Bubble**. Isso é coerente com crescimento médio O(n log n), sem representar uma razão de tempos. A vantagem não é universal: com 10 elementos, o Insertion fez menos comparações; nos cenários organizados, o último pivô tornou o Quick muito menos eficiente.

### h) Os resultados encontrados são coerentes com as complexidades teóricas estudadas?

**Sim.** As contagens dos dados aleatórios são compatíveis com o crescimento quadrático dos três algoritmos simples e com o crescimento médio O(n log n) do Quick Sort. No desafio, os melhores casos adaptativos do Bubble e do Insertion e o pior caso do Quick com último pivô ficam evidentes.

| Algoritmo utilizado | Melhor caso | Caso médio | Pior caso |
| :--- | :---: | :---: | :---: |
| Bubble Sort com parada antecipada | O(n) | O(n²) | O(n²) |
| Insertion Sort por deslocamentos | O(n) | O(n²) | O(n²) |
| Selection Sort | O(n²) | O(n²) | O(n²) |
| Quick Sort com Lomuto | O(n log n) | O(n log n) | O(n²) |

No caso médio do Quick, considera-se uma distribuição de entradas que produza partições razoavelmente equilibradas em média; não se trata de uma garantia para qualquer vetor. **Um experimento com uma base por tamanho ilustra a teoria, mas não prova uma complexidade nem estima estatisticamente o desempenho médio.**

### i) Se fosse responsável pela central de distribuição e precisasse ordenar milhares de pedidos, qual dos quatro algoritmos escolheria?

Escolheria o **Quick Sort** para lotes grandes com organização variada, por seu comportamento médio O(n log n) e pela menor contagem total observada com 1.000 pedidos aleatórios: **19.471 operações contabilizadas**.

Para colocá-lo em um sistema real, ajustaria a seleção do pivô, por exemplo escolhendo-o aleatoriamente, para reduzir o risco de partições sempre desequilibradas em lotes já organizados. Essa mudança reduz o risco, mas não elimina a possibilidade de pior caso O(n²), e **não foi aplicada nas medições deste trabalho**. Com muitos valores iguais, uma partição em três grupos também merece avaliação.

A decisão depende do perfil dos pedidos: se os lotes já estiverem ordenados ou quase ordenados, Bubble com parada e Insertion podem exigir menos operações. Além disso, esta versão do Quick não garante estabilidade; se for necessário preservar a ordem de chegada entre prioridades iguais, esse requisito precisa ser considerado na implementação.

## Desafio adicional - Organização inicial dos dados

Para cada tamanho, foram avaliadas três organizações do mesmo multiconjunto:

1. **Aleatório:** a base produzida pelo gerador.
2. **Ordenado:** a base em ordem crescente, incluindo eventuais empates.
3. **Inverso:** a base em ordem decrescente, incluindo eventuais empates.

### Tabela comparativa - 10 elementos

| n | Cenário | Algoritmo | Comparações (C) | Trocas (T) | Movimentações (M) | C + M |
| ---: | :--- | :--- | ---: | ---: | ---: | ---: |
| 10 | Aleatório | Bubble Sort | 44 | 19 | 38 | 82 |
| 10 | Aleatório | Insertion Sort | 27 | 0 | 28 | 55 |
| 10 | Aleatório | Selection Sort | 45 | 7 | 14 | 59 |
| 10 | Aleatório | Quick Sort | 29 | 7 | 14 | 43 |
| 10 | Ordenado | Bubble Sort | 9 | 0 | 0 | 9 |
| 10 | Ordenado | Insertion Sort | 9 | 0 | 9 | 18 |
| 10 | Ordenado | Selection Sort | 45 | 0 | 0 | 45 |
| 10 | Ordenado | Quick Sort | 45 | 0 | 0 | 45 |
| 10 | Inverso | Bubble Sort | 45 | 45 | 90 | 135 |
| 10 | Inverso | Insertion Sort | 45 | 0 | 54 | 99 |
| 10 | Inverso | Selection Sort | 45 | 5 | 10 | 55 |
| 10 | Inverso | Quick Sort | 45 | 5 | 10 | 55 |

### Tabela comparativa - 20 elementos

| n | Cenário | Algoritmo | Comparações (C) | Trocas (T) | Movimentações (M) | C + M |
| ---: | :--- | :--- | ---: | ---: | ---: | ---: |
| 20 | Aleatório | Bubble Sort | 189 | 84 | 168 | 357 |
| 20 | Aleatório | Insertion Sort | 99 | 0 | 103 | 202 |
| 20 | Aleatório | Selection Sort | 190 | 16 | 32 | 222 |
| 20 | Aleatório | Quick Sort | 58 | 28 | 56 | 114 |
| 20 | Ordenado | Bubble Sort | 19 | 0 | 0 | 19 |
| 20 | Ordenado | Insertion Sort | 19 | 0 | 19 | 38 |
| 20 | Ordenado | Selection Sort | 190 | 0 | 0 | 190 |
| 20 | Ordenado | Quick Sort | 190 | 0 | 0 | 190 |
| 20 | Inverso | Bubble Sort | 190 | 190 | 380 | 570 |
| 20 | Inverso | Insertion Sort | 190 | 0 | 209 | 399 |
| 20 | Inverso | Selection Sort | 190 | 10 | 20 | 210 |
| 20 | Inverso | Quick Sort | 190 | 10 | 20 | 210 |

### Tabela comparativa - 1.000 elementos

| n | Cenário | Algoritmo | Comparações (C) | Trocas (T) | Movimentações (M) | C + M |
| ---: | :--- | :--- | ---: | ---: | ---: | ---: |
| 1.000 | Aleatório | Bubble Sort | 499.122 | 239.681 | 479.362 | 978.484 |
| 1.000 | Aleatório | Insertion Sort | 240.670 | 0 | 240.680 | 481.350 |
| 1.000 | Aleatório | Selection Sort | 499.500 | 992 | 1.984 | 501.484 |
| 1.000 | Aleatório | Quick Sort | 10.385 | 4.543 | 9.086 | 19.471 |
| 1.000 | Ordenado | Bubble Sort | 999 | 0 | 0 | 999 |
| 1.000 | Ordenado | Insertion Sort | 999 | 0 | 999 | 1.998 |
| 1.000 | Ordenado | Selection Sort | 499.500 | 0 | 0 | 499.500 |
| 1.000 | Ordenado | Quick Sort | 499.500 | 0 | 0 | 499.500 |
| 1.000 | Inverso | Bubble Sort | 499.500 | 499.456 | 998.912 | 1.498.412 |
| 1.000 | Inverso | Insertion Sort | 499.496 | 0 | 500.455 | 999.951 |
| 1.000 | Inverso | Selection Sort | 499.500 | 517 | 1.034 | 500.534 |
| 1.000 | Inverso | Quick Sort | 483.534 | 517 | 1.034 | 484.568 |

### A organização inicial dos dados interfere na quantidade de operações realizadas por todos os algoritmos da mesma maneira?

**Não. A influência depende da lógica do algoritmo, da variante implementada e da métrica observada.**

**Bubble Sort:** aproveita a entrada já ordenada graças à parada antecipada. Para 1.000 elementos ordenados, faz apenas **999 comparações e nenhuma movimentação**. No inverso, faz **499.500 comparações e 998.912 escritas**. As inversões exigem muitas trocas de vizinhos.

**Insertion Sort:** também aproveita a ordem existente. No vetor ordenado de 1.000 elementos, faz **999 comparações e 999 escritas**: não há deslocamentos, mas cada chave é reescrita uma vez pela convenção adotada. No inverso, faz **499.496 comparações e 500.455 escritas**, pois quase todo novo elemento exige deslocar muitos anteriores.

**Selection Sort:** realiza **499.500 comparações nos três cenários de 1.000 elementos**, pois sempre percorre integralmente o trecho ainda não ordenado para selecionar o mínimo. Sua quantidade de trocas, entretanto, muda: **992 no aleatório, zero no ordenado e 517 no inverso**. Portanto, a organização não altera C nesta implementação, mas altera T e M.

**Quick Sort:** é muito sensível ao pivô. O último elemento de uma entrada crescente é sempre um máximo do intervalo; com a comparação `<=`, a partição deixa um lado vazio e o outro com um elemento a menos. Assim, o número de comparações passa de **10.385 no aleatório para 499.500 no ordenado**, embora não haja trocas entre índices distintos no vetor ordenado. No inverso, também ocorrem partições muito desequilibradas, resultando em **483.534 comparações**. Poucas movimentações não significam, por si só, baixo custo de ordenação.

**Efeito dos valores repetidos:** as bases de 10 e 20 elementos têm valores distintos, mas a base de 1.000 tem **960 valores distintos**: 924 aparecem uma vez, 32 aparecem duas vezes e 4 aparecem três vezes. Isso gera **44 pares de posições com valores iguais**. No inverso, há **499.500 − 44 = 499.456 inversões estritas**, explicando as 499.456 trocas do Bubble e as **499.456 + 999 = 500.455 escritas** do Insertion. As repetições também alteram o particionamento do Quick; por isso, sua contagem inversa não é exatamente n(n − 1)/2. A fórmula exata do vetor inverso com valores todos distintos não deve ser aplicada automaticamente a esse caso.

Os resultados mostram que **Bubble e Insertion se beneficiam de dados ordenados; Selection mantém seu esforço de comparação; e Quick com último pivô perde eficiência em entradas organizadas**. Não existe uma influência uniforme da organização inicial sobre os quatro algoritmos.

## Verificação e limites do experimento

- As **36 saídas** foram conferidas com `sorted(base)`, verificando simultaneamente a ordem e a preservação dos valores.
- A suíte de testes observa comparações entre chaves e escritas no vetor de forma independente dos contadores declarados pelo algoritmo.
- Também verifica casos pequenos, valores repetidos, negativos, entradas ordenadas e inversas, relações matemáticas de contagem e o Quick Sort com 1.000 valores ordenados sem recursão.
- Os valores representam **execuções individuais**, não médias de várias amostras. Nenhum tempo foi estimado a partir das contagens.
- Mudar a semente, a distribuição, a ordem de geração, a escolha do pivô, a parada antecipada ou a convenção de contagem pode alterar as tabelas.
- As tabelas são desta implementação Python. Os números da atividade anterior em C++ não foram reutilizados, pois os geradores e as variantes podem produzir contagens diferentes.

## Arquivos de resultados

- [Tabelas geradas pela execução](resultados/tabelas.md)
- [Métricas em CSV](resultados/resultados.csv)
- [Métricas em JSON](resultados/resultados.json)
- [Vetores base utilizados](resultados/vetores_base.json)
- [Ambiente e parâmetros](resultados/ambiente.json)
