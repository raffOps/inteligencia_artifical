from direcao import Direcao


class Nodo:
    def __init__(self, estado: str, estado_pai=None, acao=None, custo_caminho=0):
        self.estado = estado
        self.estado_pai = estado_pai
        self.acao = acao
        self.custo_caminho = custo_caminho
        self.posicao_vazio = self.procura_vazio()
        self.sucessores = None

    def __hash__(self):
        return hash(self.estado)

    def __eq__(self, other):
        return self.estado == other.estado

    def __str__(self):
        return """{}\t{}\t{}\n{}\t{}\t{}\n{}\t{}\t{}""".format(*self.estado)

    def procura_vazio(self):
        return self.estado.find("_")

    def get_proxima_posicao_vazio(self, acao):
        if acao == Direcao.cima:
            proxima_posicao = self.posicao_vazio - 3 if self.posicao_vazio > 2 else self.posicao_vazio
        elif acao == Direcao.abaixo:
            proxima_posicao = self.posicao_vazio + 3 if self.posicao_vazio < 6 else self.posicao_vazio
        elif acao == Direcao.esquerda:
            proxima_posicao = self.posicao_vazio - 1 if self.posicao_vazio not in (0, 3, 6) else self.posicao_vazio
        else:
            proxima_posicao = self.posicao_vazio + 1 if self.posicao_vazio not in (2, 5, 8) else self.posicao_vazio
        
        return proxima_posicao
    
    def faz_acao(self, acao):
        proxima_posicao_vazio = self.get_proxima_posicao_vazio(acao)
        estado_filho = list(self.estado)
        estado_filho[self.posicao_vazio] = self.estado[proxima_posicao_vazio]
        estado_filho[proxima_posicao_vazio] = self.estado[self.posicao_vazio]
        estado_filho = ''.join(estado_filho)
        nodo_filho = Nodo(estado_filho, self, acao.name, self.custo_caminho+1)
        return nodo_filho
    
    def get_sucessores(self):
        return [self.faz_acao(acao) for acao in Direcao]

    def get_caminho(self):
        caminho = []
        nodo = self
        while True:
            caminho.append(nodo)
            if nodo.custo_caminho == 0:
                return caminho[::-1]
            else:
                nodo = nodo.estado_pai
