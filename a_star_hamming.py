from bfs import BFS
import heapq
import sys


class AStarHamming(BFS):
    def __init__(self, raiz: str, objetivo="12345678_"):
        super().__init__(raiz, objetivo)

    def inicia_fronteira(self):
        fronteira = [(0, self.nodo_raiz)]
        return fronteira

    def push_nodo_fronteira(self, sucessor):
        heuristica = self.get_heuristica(sucessor)
        self.fronteira.append((heuristica+sucessor.custo_caminho, sucessor))

    def pop_nodo_fronteira(self):
        self.fronteira = sorted(self.fronteira, key=lambda tupla: tupla[0])
        return self.fronteira.pop(0)[1]

    def nao_estah_sucessor_na_fronteira(self, sucessor):
        for estimativa, nodo in self.fronteira:
            if nodo == sucessor:
                return False
        return True

    @staticmethod
    def get_heuristica(sucessor):
        objetivo = "185432_67"
        return sum(peca_sucessor != peca_objetivo for peca_sucessor, peca_objetivo in zip(sucessor.estado, objetivo))

if __name__ == "__main__":
    estado = sys.argv[1]
    grafo = AStarHamming(estado)
    try:
        caminho = grafo.acha_objetivo()
        movimentos = len(caminho) - 1
        print(f"Solucao tem {movimentos} movimentos.")
    except Exception as e:
        pass
