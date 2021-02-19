from bfs import BFS
import heapq


class AStarHamming(BFS):
    def __init__(self, raiz: str, objetivo="12345678_"):
        super().__init__(raiz, objetivo)

    def inicia_fronteira(self):
        return []

    def push_nodo_fronteira(self, sucessor):
        estimativa_custo = self.get_estimativa_custo(sucessor)
        heapq.heappush(self.fronteira, (estimativa_custo, sucessor))

    def pop_nodo_fronteira(self):
        return heapq.heappop(self.fronteira)

    @staticmethod
    def get_estimativa_custo(self, sucessor):
        objetivo = "12345678_"
        contador_pecas_fora_do_lugar = 0
        for peca_sucessor, peca_objetivo in zip(sucessor.estado, objetivo):
            if peca_sucessor != peca_objetivo:
                contador_pecas_fora_do_lugar += 1
        return contador_pecas_fora_do_lugar
