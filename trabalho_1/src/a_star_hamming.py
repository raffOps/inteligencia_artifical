from bfs import BFS
import heapq
import sys


class AStarHamming(BFS):
    def __init__(self, raiz: str, objetivo="12345678_"):
        super().__init__(raiz, objetivo)
        self.indice = 0

    def inicia_fronteira(self):
        return [(0, self.nodo_raiz)]

    def push_nodo_fronteira(self, sucessor):
        heuristica = self.get_heuristica(sucessor)
        heapq.heappush(self.fronteira, (heuristica+sucessor.custo_caminho, self.indice, sucessor))
        self.indice += 1

    def pop_nodo_fronteira(self):
        return heapq.heappop(self.fronteira)[-1]

    def nao_estah_sucessor_na_fronteira(self, sucessor):
        return all(nodo != sucessor for *_, nodo in self.fronteira)

    def get_heuristica(self, sucessor):
        objetivo = "185432_67"
        return sum(peca_sucessor != peca_objetivo for peca_sucessor, peca_objetivo in zip(sucessor.estado, objetivo))


if __name__ == "__main__":
    estado = sys.argv[1]
    grafo = AStarHamming(estado)
    if caminho := grafo.acha_objetivo():
        print(' '.join([nodo.acao for nodo in caminho[1:]]))
