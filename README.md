# 📊 Análise de Algoritmos de Ordenação em Python

## 📌 Descrição

Trabalho da **Atividade Avaliativa 3 de Estrutura de Dados II**, com o tema **Central de Distribuição de Pedidos**.

O projeto compara Bubble Sort, Insertion Sort, Selection Sort e Quick Sort em vetores de 10, 20 e 1.000 elementos. Os números representam as chaves usadas para ordenar os pedidos. A comparação considera a quantidade de operações e o efeito da organização inicial dos dados.

## 🎯 Objetivo

Entender como cada algoritmo se comporta quando a quantidade de dados aumenta e relacionar os resultados às complexidades estudadas em aula. O desafio adicional compara os mesmos valores em ordem aleatória, crescente e inversa.

## 🛠️ Tecnologias utilizadas

- Python
- Google Colab

## ⚙️ Funcionalidades

- Implementação dos quatro algoritmos de ordenação
- Contagem de comparações, trocas e movimentações
- Testes com vetores de 10, 20 e 1.000 elementos
- Uso de semente fixa e cópias iguais para comparar os algoritmos
- Comparação de dados aleatórios, ordenados e inversos
- Validação das ordenações e dos contadores
- Geração de tabelas e exportação dos resultados

## 🧩 Estrutura do projeto

### 🔹 Algoritmos de ordenação

O arquivo [analise_ordenacao.py](analise_ordenacao.py) reúne o código completo. Cada algoritmo recebe uma lista, ordena seus valores e retorna as operações contabilizadas.

### 🔹 Preparação dos experimentos

A chamada `random.seed(42)` é feita uma única vez. Em seguida, são geradas as bases de 10, 20 e 1.000 elementos, nessa ordem, com `random.randint(1, 10000)`. Os limites estão incluídos e podem aparecer números repetidos.

Cada algoritmo recebe `entrada.copy()` e começa com os contadores zerados. Os cenários ordenado e inverso são montados a partir da mesma base de cada tamanho, preservando os valores e suas quantidades.

### 🔹 Comparação dos resultados

São realizadas 36 ordenações: quatro algoritmos, três tamanhos e três cenários. A atividade principal usa as 12 execuções com dados aleatórios. O desafio inclui essas mesmas execuções e as outras 24.

A função `sorted()` é usada somente para preparar os cenários e conferir as saídas. Essas operações ficam fora da contagem. As entradas utilizadas estão em [vetores_base.json](resultados/vetores_base.json).

## 📚 Aprendizados

- Implementação de algoritmos de ordenação em Python
- Diferença entre comparações, trocas e movimentações
- Análise de complexidade com a notação Big-O
- Influência da ordem inicial dos dados
- Importância da escolha do pivô no Quick Sort
- Organização de experimentos reproduzíveis
- Interpretação de resultados e verificação automática

## 🔍 Explicação das implementações

### Bubble Sort

Compara valores vizinhos e troca os que estão fora de ordem. A cada passagem, o maior valor do trecho chega ao final. Se uma passagem não fizer nenhuma troca, o algoritmo encerra, pois o vetor já está ordenado.

### Insertion Sort

Separa uma chave e desloca para a direita os valores anteriores que são maiores que ela. Depois, coloca a chave na posição encontrada. Por trabalhar com deslocamentos, essa implementação não faz trocas entre pares de posições.

### Selection Sort

Procura o menor valor no trecho ainda não ordenado e o coloca na posição atual. A troca acontece somente quando o menor está em outra posição. Mesmo em uma lista já ordenada, ele precisa percorrer o trecho para procurar o mínimo.

### Quick Sort

Usa a partição de Lomuto, com o último elemento como pivô. Os valores menores ou iguais ao pivô são colocados à esquerda, e o processo continua nos trechos restantes.

Uma pilha explícita substitui as chamadas recursivas. Isso evita o limite de recursão do Python, mas não resolve o pior caso O(n²) quando as partições ficam muito desequilibradas.

## 🔢 Critérios de contagem

| Medida | O que é contado |
| :--- | :--- |
| Comparações (C) | Cada comparação avaliada entre valores, inclusive quando o resultado é falso. |
| Trocas (T) | Cada troca entre duas posições distintas, mesmo que tenham valores iguais. |
| Movimentações (M) | Cada escrita em uma posição do vetor. Uma troca corresponde a duas movimentações. |
| C + M | Soma das comparações com as movimentações, usada para comparar o trabalho contado dos quatro algoritmos. |

Trocar uma posição consigo mesma não executa escritas e não aumenta os contadores. Leituras, atribuições a variáveis auxiliares, testes de índices e laços, uso da pilha, geração dos dados, cópias, validação e exportação ficam fora da contagem.

| Algoritmo | Comparações | Trocas e movimentações |
| :--- | :--- | :--- |
| Bubble Sort | Cada avaliação de `vetor[j] > vetor[j + 1]`. | Cada troca de vizinhos acrescenta 1 a T e 2 a M. |
| Insertion Sort | Cada avaliação de `vetor[j] > chave`, incluindo a última falsa. Se `j < 0`, não há comparação entre valores a contar. | Cada deslocamento acrescenta 1 a M. A escrita final da chave também acrescenta 1, mesmo quando ela fica no mesmo lugar. T é zero. |
| Selection Sort | Cada avaliação de `vetor[j] < vetor[menor]`. | A troca entre posições distintas acrescenta 1 a T e 2 a M. |
| Quick Sort | Cada avaliação de `vetor[j] <= pivo`. | As trocas da partição e da colocação do pivô acrescentam 1 a T e 2 a M quando os índices são diferentes. |

Para comparar as movimentações de todos os algoritmos, é usada a coluna M. O zero em T no Insertion Sort significa que ele usa deslocamentos, embora continue escrevendo no vetor.

C + M é uma soma das operações escolhidas para o estudo, e não uma medida de tempo ou de todas as instruções do programa. T não é somado novamente porque as escritas de cada troca já estão incluídas em M.

## 📊 Resultados com vetores aleatórios

As tabelas apresentam as contagens obtidas na execução. O ponto é usado como separador de milhares.

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

## 🧪 Desafio adicional e comparação

Para cada tamanho, os mesmos valores foram avaliados em três organizações: aleatória, crescente e inversa.

### 10 elementos

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

### 20 elementos

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

### 1.000 elementos

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

Não. Cada algoritmo aproveita ou é prejudicado pela ordem dos dados de um jeito.

No Bubble Sort, o vetor já ordenado permite encerrar depois da primeira passagem. Com 1.000 elementos, foram apenas 999 comparações e nenhuma movimentação. No inverso, ele precisou fazer 499.500 comparações e 998.912 movimentações.

O Insertion Sort também se beneficia da ordem crescente. Nesse cenário, fez 999 comparações e 999 movimentações, que correspondem à escrita final de cada chave. No inverso, precisou deslocar muitos valores, chegando a 499.496 comparações e 500.455 movimentações.

O Selection Sort manteve 499.500 comparações nos três cenários de 1.000 elementos, porque sempre procura o menor valor em todo o trecho restante. A quantidade de trocas mudou: foram 992 no aleatório, nenhuma no ordenado e 517 no inverso.

Já o Quick Sort foi prejudicado pelas entradas organizadas. Como o pivô é o último elemento, as divisões ficaram muito desequilibradas. Ele passou de 10.385 comparações no aleatório para 499.500 no ordenado e 483.534 no inverso. Mesmo sem trocar posições no vetor ordenado, continuou fazendo muitas comparações.

A base de 1.000 elementos tem 960 valores distintos e 44 pares de posições com valores iguais. Por isso, o inverso tem 499.456 inversões estritas, em vez de 499.500. Isso explica as trocas do Bubble e parte das diferenças nas contagens. As repetições também afetam as partições do Quick, então a fórmula exata do caso inverso com valores distintos não se aplica diretamente a essa base.

## 📝 Respostas do relatório

### a) Qual algoritmo realizou o menor número de comparações para 10 elementos?

Foi o Insertion Sort, com 27 comparações. O Quick Sort fez 29, o Bubble Sort fez 44 e o Selection Sort fez 45. Nesse vetor pequeno, o Insertion precisou comparar menos valores. Isso mostra que o Quick não necessariamente terá a menor contagem em toda entrada, mesmo tendo uma complexidade média melhor.

### b) Qual algoritmo realizou menos trocas ou movimentações?

Com 10 elementos, Selection Sort e Quick Sort empataram: cada um fez 7 trocas, equivalentes a 14 movimentações. O Insertion fez 28 movimentações e o Bubble fez 38.

Nos vetores maiores, o Selection fez menos movimentações: 32 com 20 elementos e 1.984 com 1.000. O Insertion aparece com zero trocas porque trabalha por deslocamentos, mas esses deslocamentos contam como movimentações. Por isso, a coluna M é a mais adequada para comparar os quatro nessa questão.

### c) O comportamento observado para 10 elementos permaneceu semelhante quando o tamanho aumentou para 20?

Em parte. Com 20 elementos, o Quick Sort passou a fazer menos comparações: foram 58, contra 99 do Insertion. O Selection também passou a movimentar menos dados que o Quick, com 32 movimentações contra 56.

Ao somar comparações e movimentações, a ordem continuou a mesma nos dois tamanhos: Quick, Insertion, Selection e Bubble. Então, algumas posições mudaram dependendo da operação observada, mas o Quick manteve o menor total.

### d) O que aconteceu com a quantidade de operações quando o vetor passou para 1.000 elementos?

A quantidade aumentou bastante, principalmente no Bubble, no Insertion e no Selection. Somando comparações e movimentações, o Bubble chegou a 978.484 operações, o Insertion a 481.350 e o Selection a 501.484. O Quick ficou em 19.471.

A diferença ficou mais clara nesse tamanho. Os três primeiros passaram a exigir centenas de milhares de operações, enquanto o Quick resolveu a mesma entrada com uma contagem bem menor.

### e) Bubble Sort, Insertion Sort e Selection Sort apresentam complexidade O(n²) em situações típicas. Eles apresentaram exatamente a mesma quantidade de operações?

Não. Para 1.000 elementos aleatórios, o Bubble fez 499.122 comparações e 479.362 movimentações. O Insertion fez 240.670 comparações e 240.680 movimentações. Já o Selection fez 499.500 comparações, mas apenas 1.984 movimentações.

Ter complexidade O(n²) não significa executar a mesma quantidade de operações. Essa notação descreve um limite de crescimento conforme a entrada aumenta. Cada algoritmo organiza os dados de uma forma: o Bubble troca vizinhos, o Insertion desloca valores e o Selection procura o menor antes de trocar. Por isso, suas contagens são diferentes.

### f) Qual algoritmo apresentou maior crescimento no número de operações?

Considerando a soma C + M, foi o Bubble Sort. De 20 para 1.000 elementos, ele passou de 357 para 978.484 operações, um aumento de 978.127, ou aproximadamente 2.740,85 vezes. Foi o maior crescimento absoluto e proporcional entre os quatro nessa comparação.

A resposta depende da medida escolhida. Se fossem consideradas apenas as comparações e seu aumento absoluto, o Selection teria o maior crescimento: 499.310, contra 498.933 do Bubble. Usando comparações e movimentações juntas, o maior crescimento foi do Bubble.

### g) Como o comportamento experimental do Quick Sort se diferenciou dos demais algoritmos?

Nos dados aleatórios, o Quick precisou de muito menos comparações quando a entrada aumentou. Com 1.000 elementos, fez 10.385 comparações, enquanto os demais ficaram entre 240.670 e 499.500.

Esse resultado está ligado à divisão do problema em partes menores. Quando as partições ficam equilibradas, o trabalho cresce menos do que nos algoritmos quadráticos. No desafio, porém, a escolha do último elemento como pivô prejudicou o Quick nos vetores ordenados e inversos.

### h) Os resultados encontrados são coerentes com as complexidades teóricas estudadas?

Sim. Nos vetores aleatórios, o Bubble, o Insertion e o Selection tiveram um crescimento compatível com O(n²). O Quick apresentou uma contagem menor no maior vetor, coerente com seu comportamento médio O(n log n).

O desafio também mostrou os casos especiais: Bubble e Insertion aproveitaram o vetor já ordenado, enquanto o Quick com último pivô chegou ao pior caso nessa entrada.

| Algoritmo | Melhor caso | Caso médio | Pior caso |
| :--- | :---: | :---: | :---: |
| Bubble Sort com parada antecipada | O(n) | O(n²) | O(n²) |
| Insertion Sort | O(n) | O(n²) | O(n²) |
| Selection Sort | O(n²) | O(n²) | O(n²) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) |

Como foi usada uma base por tamanho, o experimento ajuda a observar a teoria, mas não é uma prova das complexidades nem uma média de várias amostras. O caso médio do Quick pressupõe uma distribuição de entradas em que as partições não sejam sempre muito desequilibradas.

### i) Se você fosse responsável pelo sistema da central de distribuição e precisasse ordenar milhares de pedidos, qual dos quatro algoritmos escolheria?

Eu escolheria o Quick Sort para lotes grandes com dados em ordens variadas. Ele teve o menor total no teste aleatório de 1.000 elementos, com 19.471 operações, e seu comportamento médio O(n log n) é mais adequado para esse volume.

Eu teria cuidado com a escolha do pivô. O desafio mostrou que usar sempre o último elemento pode aumentar muito o trabalho quando os pedidos já vêm organizados. Em um sistema real, consideraria escolher o pivô aleatoriamente para reduzir esse risco, embora isso não elimine a possibilidade de pior caso O(n²). Essa alteração não foi usada nos resultados deste trabalho.

Se os pedidos chegassem quase sempre ordenados, também avaliaria o Insertion Sort. Outro ponto é que esta versão do Quick não garante a ordem original entre valores iguais; se fosse necessário preservar a chegada de pedidos com a mesma prioridade, esse requisito precisaria entrar na escolha.
