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

    def get_proximo_nodo(self):
        return self.fronteira.popleft()

    def acha_objetivo(self):
        while True:
            proximo_nodo = self.get_proximo_nodo()
            #print(proximo_nodo.acao)
            #print(proximo_nodo)
            #print("*"*20)
            #input()
            if not proximo_nodo:
                raise Exception("Nao existe caminho")
            elif proximo_nodo == self.objetivo:
                return proximo_nodo.get_caminho()
            elif proximo_nodo.estado not in self.conhecidos:
                self.conhecidos.add(proximo_nodo.estado)
                sucessores = proximo_nodo.get_sucessores()
                for sucessor in sucessores:
                    if sucessor not in self.fronteira:
                        self.fronteira.append(sucessor)


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





