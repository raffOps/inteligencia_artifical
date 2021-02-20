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

    def acha_objetivo(self):
        while True:
            proximo_nodo = self.pop_nodo_fronteira()
            if not proximo_nodo:
                raise Exception("Nao existe caminho")
            elif proximo_nodo == self.objetivo:
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
    try:
        caminho = grafo.acha_objetivo()
        movimentos = len(caminho) - 1
        print(f"Solucao tem {movimentos} movimentos.")
    except Exception as e:
        pass



    # grafo = BFS("123456_78")
    # caminho = grafo.acha_objetivo()
    #
    # for nodo in caminho:
    #     print(nodo.acao)
    #     print("\n")
    #     print(nodo)
    #     print("-"*20)





