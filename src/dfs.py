from nodo import Nodo
from collections import deque
from bfs import BFS


class DFS(BFS):
    def __init__(self, raiz: str, objetivo="12345678_"):
        super().__init__(raiz, objetivo)

    def get_proximo_nodo(self):
        return self.fronteira.pop()


if __name__ == "__main__":
    grafo = DFS("12345_678")
    caminho = grafo.acha_objetivo()

    for nodo in caminho:
        print(nodo.acao)
        print("\n")
        print(nodo)
        print("-"*20)










