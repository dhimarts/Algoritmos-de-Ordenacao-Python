# Resultados da execucao

C = comparacoes entre valores; T = trocas entre indices distintos; M = escritas no vetor. Cada troca acrescenta 2 a M. Insertion Sort desloca valores e, por isso, tem T = 0.

C + M e um custo didatico; nao mede tempo. Nao some T novamente, pois suas escritas ja fazem parte de M.

## Etapa 3 - Vetores aleatorios

| n | Cenario | Algoritmo | C | T | M | C + M |
| ---: | :--- | :--- | ---: | ---: | ---: | ---: |
| 10 | Aleatorio | Bubble Sort | 44 | 19 | 38 | 82 |
| 10 | Aleatorio | Insertion Sort | 27 | 0 | 28 | 55 |
| 10 | Aleatorio | Selection Sort | 45 | 7 | 14 | 59 |
| 10 | Aleatorio | Quick Sort | 29 | 7 | 14 | 43 |
| 20 | Aleatorio | Bubble Sort | 189 | 84 | 168 | 357 |
| 20 | Aleatorio | Insertion Sort | 99 | 0 | 103 | 202 |
| 20 | Aleatorio | Selection Sort | 190 | 16 | 32 | 222 |
| 20 | Aleatorio | Quick Sort | 58 | 28 | 56 | 114 |
| 1.000 | Aleatorio | Bubble Sort | 499.122 | 239.681 | 479.362 | 978.484 |
| 1.000 | Aleatorio | Insertion Sort | 240.670 | 0 | 240.680 | 481.350 |
| 1.000 | Aleatorio | Selection Sort | 499.500 | 992 | 1.984 | 501.484 |
| 1.000 | Aleatorio | Quick Sort | 10.385 | 4.543 | 9.086 | 19.471 |

## Desafio adicional - Tres cenarios

### 10 elementos

| n | Cenario | Algoritmo | C | T | M | C + M |
| ---: | :--- | :--- | ---: | ---: | ---: | ---: |
| 10 | Aleatorio | Bubble Sort | 44 | 19 | 38 | 82 |
| 10 | Aleatorio | Insertion Sort | 27 | 0 | 28 | 55 |
| 10 | Aleatorio | Selection Sort | 45 | 7 | 14 | 59 |
| 10 | Aleatorio | Quick Sort | 29 | 7 | 14 | 43 |
| 10 | Ordenado | Bubble Sort | 9 | 0 | 0 | 9 |
| 10 | Ordenado | Insertion Sort | 9 | 0 | 9 | 18 |
| 10 | Ordenado | Selection Sort | 45 | 0 | 0 | 45 |
| 10 | Ordenado | Quick Sort | 45 | 0 | 0 | 45 |
| 10 | Inverso | Bubble Sort | 45 | 45 | 90 | 135 |
| 10 | Inverso | Insertion Sort | 45 | 0 | 54 | 99 |
| 10 | Inverso | Selection Sort | 45 | 5 | 10 | 55 |
| 10 | Inverso | Quick Sort | 45 | 5 | 10 | 55 |

### 20 elementos

| n | Cenario | Algoritmo | C | T | M | C + M |
| ---: | :--- | :--- | ---: | ---: | ---: | ---: |
| 20 | Aleatorio | Bubble Sort | 189 | 84 | 168 | 357 |
| 20 | Aleatorio | Insertion Sort | 99 | 0 | 103 | 202 |
| 20 | Aleatorio | Selection Sort | 190 | 16 | 32 | 222 |
| 20 | Aleatorio | Quick Sort | 58 | 28 | 56 | 114 |
| 20 | Ordenado | Bubble Sort | 19 | 0 | 0 | 19 |
| 20 | Ordenado | Insertion Sort | 19 | 0 | 19 | 38 |
| 20 | Ordenado | Selection Sort | 190 | 0 | 0 | 190 |
| 20 | Ordenado | Quick Sort | 190 | 0 | 0 | 190 |
| 20 | Inverso | Bubble Sort | 190 | 190 | 380 | 570 |
| 20 | Inverso | Insertion Sort | 190 | 0 | 209 | 399 |
| 20 | Inverso | Selection Sort | 190 | 10 | 20 | 210 |
| 20 | Inverso | Quick Sort | 190 | 10 | 20 | 210 |

### 1.000 elementos

| n | Cenario | Algoritmo | C | T | M | C + M |
| ---: | :--- | :--- | ---: | ---: | ---: | ---: |
| 1.000 | Aleatorio | Bubble Sort | 499.122 | 239.681 | 479.362 | 978.484 |
| 1.000 | Aleatorio | Insertion Sort | 240.670 | 0 | 240.680 | 481.350 |
| 1.000 | Aleatorio | Selection Sort | 499.500 | 992 | 1.984 | 501.484 |
| 1.000 | Aleatorio | Quick Sort | 10.385 | 4.543 | 9.086 | 19.471 |
| 1.000 | Ordenado | Bubble Sort | 999 | 0 | 0 | 999 |
| 1.000 | Ordenado | Insertion Sort | 999 | 0 | 999 | 1.998 |
| 1.000 | Ordenado | Selection Sort | 499.500 | 0 | 0 | 499.500 |
| 1.000 | Ordenado | Quick Sort | 499.500 | 0 | 0 | 499.500 |
| 1.000 | Inverso | Bubble Sort | 499.500 | 499.456 | 998.912 | 1.498.412 |
| 1.000 | Inverso | Insertion Sort | 499.496 | 0 | 500.455 | 999.951 |
| 1.000 | Inverso | Selection Sort | 499.500 | 517 | 1.034 | 500.534 |
| 1.000 | Inverso | Quick Sort | 483.534 | 517 | 1.034 | 484.568 |
