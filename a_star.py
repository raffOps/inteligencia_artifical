from bfs import BFS
import heapq
import sys


class AStarHamming(BFS):
    def __init__(self, raiz: str, objetivo="12345678_"):
        super().__init__(raiz, objetivo)

    def inicia_fronteira(self):
        return [self.nodo_raiz]

    def push_nodo_fronteira(self, sucessor):
        estimativa_custo = self.get_estimativa_custo(sucessor)
        heapq.heappush(self.fronteira, (estimativa_custo, sucessor))

    def pop_nodo_fronteira(self):
        return heapq.heappop(self.fronteira)

    def estah_sucessor_na_fronteira(self, sucessor):
        for estimativa, nodo in self.fronteira:
            if nodo == sucessor:
                return True
        return False

    @staticmethod
    def get_estimativa_custo(sucessor):
        objetivo = "12345678_"
        contador_pecas_fora_do_lugar = 0
        for peca_sucessor, peca_objetivo in zip(sucessor.estado, objetivo):
            if peca_sucessor != peca_objetivo:
                contador_pecas_fora_do_lugar += 1
        return contador_pecas_fora_do_lugar

# if __name__ == "__main__":
#     estado = sys.argv[1]
#     grafo = AStarHamming(estado)
#     try:
#         caminho = grafo.acha_objetivo()
#         movimentos = len(caminho) - 1
#         print(f"Solucao tem {movimentos} movimentos.")
#     except Exception as e:
#         print(e)

estado = "2_3541687"
grafo = AStarHamming(estado)

caminho = grafo.acha_objetivo()
movimentos = len(caminho) - 1
print(f"Solucao tem {movimentos} movimentos.")
