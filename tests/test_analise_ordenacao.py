"""Auditoria independente da ordenacao e dos contadores (biblioteca padrao).

Execute na raiz do repositorio: python -m unittest discover -s tests -v
Os observadores medem operacoes reais, sem reproduzir os algoritmos.
"""

import itertools
import random
import unittest
from unittest.mock import patch

import analise_ordenacao as analise


class Observador:
    def __init__(self):
        self.comparacoes = 0
        self.escritas = 0


class InteiroObservavel(int):
    """Registra cada comparacao efetivamente executada entre valores."""

    def __new__(cls, valor, observador):
        objeto = super().__new__(cls, valor)
        objeto.observador = observador
        return objeto

    def __lt__(self, outro):
        self.observador.comparacoes += 1
        return int.__lt__(self, outro)

    def __le__(self, outro):
        self.observador.comparacoes += 1
        return int.__le__(self, outro)

    def __gt__(self, outro):
        self.observador.comparacoes += 1
        return int.__gt__(self, outro)

    def __ge__(self, outro):
        self.observador.comparacoes += 1
        return int.__ge__(self, outro)

    def __eq__(self, outro):
        self.observador.comparacoes += 1
        return int.__eq__(self, outro)

    def __ne__(self, outro):
        self.observador.comparacoes += 1
        return int.__ne__(self, outro)


class VetorObservavel(list):
    """Registra cada escrita em uma posicao do vetor."""

    def __init__(self, valores, observador):
        self.observador = observador
        super().__init__(InteiroObservavel(x, observador) for x in valores)

    def __setitem__(self, indice, valor):
        if isinstance(indice, slice):
            raise AssertionError("A auditoria espera escritas por indice.")
        self.observador.escritas += 1
        super().__setitem__(indice, valor)


def inversoes(valores):
    """Conta pares fora de ordem pela definicao matematica de inversao."""
    return sum(
        valores[i] > valores[j]
        for i in range(len(valores))
        for j in range(i + 1, len(valores))
    )


class TestOrdenacaoEContadores(unittest.TestCase):
    def auditar(self, algoritmo, entrada):
        observador = Observador()
        vetor = VetorObservavel(entrada, observador)
        metricas = algoritmo(vetor)
        # Converte para int antes de validar para nao contaminar a observacao.
        self.assertEqual([int(x) for x in vetor], sorted(entrada))
        self.assertEqual(metricas.comparacoes, observador.comparacoes)
        self.assertEqual(metricas.movimentacoes, observador.escritas)
        self.assertEqual(metricas.total, observador.comparacoes + observador.escritas)
        self.assertGreaterEqual(metricas.trocas, 0)
        if algoritmo is analise.insertion_sort:
            self.assertEqual(metricas.trocas, 0)
        else:
            self.assertEqual(metricas.movimentacoes, 2 * metricas.trocas)
        return metricas

    def test_auditoria_exaustiva_com_negativos_e_repetidos(self):
        # 364 entradas, incluindo vazia, unitaria, iguais e inversas.
        # Para cada entrada, os quatro algoritmos sao observados externamente.
        for tamanho in range(6):
            for valores in itertools.product((-1, 0, 1), repeat=tamanho):
                for nome, algoritmo in analise.ALGORITMOS.items():
                    with self.subTest(algoritmo=nome, entrada=valores):
                        self.auditar(algoritmo, valores)

    def test_invariantes_por_inversoes_e_formula_selection(self):
        gerador = random.Random(2026)
        entradas = [[], [7], [3, 3, 3], [-1, -4, 2, -1]]
        entradas += [list(range(12)), list(range(11, -1, -1))]
        entradas += [[gerador.randint(-8, 8) for _ in range(n)] for n in range(2, 31)]
        for entrada in entradas:
            with self.subTest(entrada=entrada):
                n = len(entrada)
                quantidade_inversoes = inversoes(entrada)
                bubble = self.auditar(analise.bubble_sort, entrada)
                insertion = self.auditar(analise.insertion_sort, entrada)
                selection = self.auditar(analise.selection_sort, entrada)
                self.assertEqual(bubble.trocas, quantidade_inversoes)
                self.assertEqual(insertion.movimentacoes, quantidade_inversoes + max(0, n - 1))
                # Cada chave que nao e um novo minimo estrito termina com
                # uma comparacao falsa. As demais terminam por limite de indice.
                falsas = sum(any(x <= entrada[i] for x in entrada[:i]) for i in range(1, n))
                self.assertEqual(insertion.comparacoes, quantidade_inversoes + falsas)
                self.assertEqual(selection.comparacoes, n * (n - 1) // 2)
                self.assertLessEqual(selection.trocas, max(0, n - 1))

    def test_vazios_e_unitarios_nao_realizam_operacoes(self):
        for entrada in ([], [9]):
            for nome, algoritmo in analise.ALGORITMOS.items():
                with self.subTest(algoritmo=nome, entrada=entrada):
                    self.assertEqual(algoritmo(entrada.copy()), analise.Metricas())

    def test_entrada_ordenada_e_parada_antecipada(self):
        entrada = list(range(25))
        self.assertEqual(self.auditar(analise.bubble_sort, entrada), analise.Metricas(24, 0, 0))
        self.assertEqual(self.auditar(analise.insertion_sort, entrada), analise.Metricas(24, 0, 24))
        self.assertEqual(self.auditar(analise.selection_sort, entrada), analise.Metricas(300, 0, 0))
        self.assertEqual(self.auditar(analise.quick_sort, entrada), analise.Metricas(300, 0, 0))

    def test_inverso_distinto_tem_contagens_exatas(self):
        entrada = list(range(12, 0, -1))
        esperadas = {
            analise.bubble_sort: analise.Metricas(66, 66, 132),
            analise.insertion_sort: analise.Metricas(66, 0, 77),
            analise.selection_sort: analise.Metricas(66, 6, 12),
            analise.quick_sort: analise.Metricas(66, 6, 12),
        }
        for algoritmo, esperado in esperadas.items():
            with self.subTest(algoritmo=algoritmo.__name__):
                self.assertEqual(self.auditar(algoritmo, entrada), esperado)

    def test_iguais_evidenciam_degeneracao_do_quick(self):
        entrada = [5] * 12
        esperadas = {
            analise.bubble_sort: analise.Metricas(11, 0, 0),
            analise.insertion_sort: analise.Metricas(11, 0, 11),
            analise.selection_sort: analise.Metricas(66, 0, 0),
            analise.quick_sort: analise.Metricas(66, 0, 0),
        }
        for algoritmo, esperado in esperadas.items():
            with self.subTest(algoritmo=algoritmo.__name__):
                self.assertEqual(self.auditar(algoritmo, entrada), esperado)

    def test_troca_distinta_igual_e_autotroca(self):
        observador = Observador()
        vetor = VetorObservavel([4, 4, 2], observador)
        metricas = analise.Metricas()
        analise.trocar(vetor, 0, 0, metricas)
        self.assertEqual(metricas, analise.Metricas())
        self.assertEqual(observador.escritas, 0)
        analise.trocar(vetor, 0, 1, metricas)
        self.assertEqual(metricas, analise.Metricas(0, 1, 2))
        analise.trocar(vetor, 1, 2, metricas)
        self.assertEqual(metricas, analise.Metricas(0, 2, 4))
        self.assertEqual(observador.escritas, 4)
        self.assertEqual(observador.comparacoes, 0)
        self.assertEqual([int(x) for x in vetor], [4, 2, 4])

    def test_quick_mil_elementos_degenerados_sem_recursion_error(self):
        casos = (
            (list(range(1000)), analise.Metricas(499500, 0, 0)),
            (list(range(999, -1, -1)), analise.Metricas(499500, 500, 1000)),
            ([7] * 1000, analise.Metricas(499500, 0, 0)),
        )
        for entrada, esperado in casos:
            with self.subTest(primeiro=entrada[0], ultimo=entrada[-1]):
                self.assertEqual(self.auditar(analise.quick_sort, entrada), esperado)


class TestExperimentos(unittest.TestCase):
    def test_semente_e_sequencia_de_geracao(self):
        gerador = random.Random(42)
        esperado = {n: [gerador.randint(1, 10000) for _ in range(n)] for n in (10, 20, 1000)}
        estado_anterior = random.getstate()
        try:
            bases = analise.gerar_bases()
            repeticao = analise.gerar_bases()
        finally:
            random.setstate(estado_anterior)
        self.assertEqual(bases, esperado)
        self.assertEqual(repeticao, esperado)
        self.assertEqual(bases[10], [1825, 410, 4507, 4013, 3658, 2287, 1680, 8936, 1425, 9675])

    def test_cenarios_preservam_multiconjunto_e_base(self):
        base = [4, -2, 4, 0, -2]
        copia = base.copy()
        cenarios = analise.criar_cenarios(base)
        self.assertEqual(cenarios, {
            "Aleatorio": copia,
            "Ordenado": [-2, -2, 0, 4, 4],
            "Inverso": [4, 4, 0, -2, -2],
        })
        self.assertEqual(base, copia)
        for entrada in cenarios.values():
            self.assertIsNot(entrada, base)
            self.assertEqual(sorted(entrada), sorted(base))

    def test_experimentos_entregam_copias_identicas_e_preservam_bases(self):
        bases = {4: [4, -2, 4, 0], 2: [8, 1]}
        originais = {n: vetor.copy() for n, vetor in bases.items()}
        recebidas = {nome: [] for nome in analise.ALGORITMOS}
        # Preserva as referencias para provar que cada chamada recebe outro objeto.
        objetos = []
        auditorias = {}
        for nome, algoritmo in analise.ALGORITMOS.items():
            def registrar(vetor, nome=nome, algoritmo=algoritmo):
                recebidas[nome].append(vetor.copy())
                objetos.append(vetor)
                return algoritmo(vetor)
            auditorias[nome] = registrar
        with patch.dict(analise.ALGORITMOS, auditorias, clear=True):
            resultados = analise.executar_experimentos(bases)
        esperado = []
        for base in originais.values():
            esperado.extend([base, sorted(base), sorted(base, reverse=True)])
        for entradas in recebidas.values():
            self.assertEqual(entradas, esperado)
        self.assertEqual(len({id(vetor) for vetor in objetos}), len(objetos))
        self.assertEqual(bases, originais)
        self.assertEqual(len(resultados), 2 * 3 * 4)
        for resultado in resultados:
            self.assertEqual(resultado.total, resultado.comparacoes + resultado.movimentacoes)


if __name__ == "__main__":
    unittest.main()
