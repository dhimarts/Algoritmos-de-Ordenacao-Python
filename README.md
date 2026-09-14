# 📊 Análise de Algoritmos de Ordenação em Python

## 📌 Descrição

Projeto acadêmico desenvolvido na disciplina de **Estrutura de Dados II**, utilizando Python para implementar e analisar algoritmos de ordenação aplicados ao contexto de uma **Central de Distribuição de Pedidos**.

O projeto compara **Bubble Sort, Insertion Sort, Selection Sort e Quick Sort**, observando como o tamanho e a organização inicial dos dados influenciam a quantidade de comparações, trocas e movimentações realizadas durante a ordenação.

## 🎯 Objetivo

Aplicar conceitos de estruturas de dados e análise de algoritmos por meio da implementação prática de quatro métodos de ordenação, comparando seu comportamento experimental com as respectivas complexidades teóricas.

Também é objetivo garantir condições iguais de teste, utilizando uma semente fixa e cópias idênticas de cada vetor, além de avaliar os algoritmos em três cenários: dados aleatórios, já ordenados e em ordem inversa.

## 🛠️ Tecnologias utilizadas

- Python
- 

## ⚙️ Funcionalidades

- Implementação de algoritmos de ordenação
- Contagem individual de comparações, trocas e movimentações
- Geração de vetores com elementos
- Uso de `random.seed(42)` para reprodução do experimento
- Utilização de cópias idênticas para garantir igualdade entre os testes
- Comparação de vetores aleatórios, ordenados e inversos
- Validação de todas as ordenações com `sorted()`
- Exibição automática das tabelas no terminal
- Exportação dos resultados em CSV, JSON e Markdown
- Testes automatizados para conferir a ordenação e os contadores

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


