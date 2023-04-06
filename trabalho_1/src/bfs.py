from nodo import Nodo
from collections import deque
import sys


class BFS:
    def __init__(self, raiz: str, objetivo="12345678_"):
        self.nodo_raiz = Nodo(raiz)
        self.objetivo = Nodo(objetivo)
        self.conhecidos = set()
        self.fronteira = self.inicia_fronteira()

    def inicia_fronteira(self):
        return deque([self.nodo_raiz])

    def pop_nodo_fronteira(self):
        return self.fronteira.popleft()

    def push_nodo_fronteira(self, sucessor):
        self.fronteira.append(sucessor)

    def existe_caminho(self):
        inversoes_totais = 0
        raiz = self.nodo_raiz.estado
        for indice in range(9):
            if raiz[indice] != "_":
                for indice_2 in range(indice+1, 9):
                    if raiz[indice_2] != "_":
                        elemento1 = int(raiz[indice])
                        elemento2 = int(raiz[indice_2])
                        if elemento1 < elemento2:
                            inversoes_totais += 1
        return inversoes_totais % 2 == 0

    def acha_objetivo(self):
        if not self.existe_caminho():
            return []
        while True:
            proximo_nodo = self.pop_nodo_fronteira()
            if proximo_nodo == self.objetivo:
                return proximo_nodo.get_caminho()
            elif proximo_nodo.estado not in self.conhecidos:
                self.conhecidos.add(proximo_nodo.estado)
                sucessores = proximo_nodo.get_sucessores()
                for sucessor in sucessores:
                    if self.nao_estah_sucessor_na_fronteira(sucessor):
                        self.push_nodo_fronteira(sucessor)

    def nao_estah_sucessor_na_fronteira(self, sucessor):
        return sucessor not in self.fronteira


if __name__ == "__main__":
    estado = sys.argv[1]
    grafo = BFS(estado)
    if caminho := grafo.acha_objetivo():
        print(' '.join([nodo.acao for nodo in caminho[1:]]))
