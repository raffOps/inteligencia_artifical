class Nodo:
    def __init__(self, estado: str):
        self.estado = estado
        self.posicao_vazio = self.procura_vazio()
        self.sucessores = self.expande()

    # def get_matrix(self, estado: str):
    #     return np.array(list(self.estado)).reshape(3, 3)

    # def procura_vazio(self):
    #     i, j = np.where(self.estado == "_")
    #     return i[0], j[0]
    
    def procura_vazio(self):
        return self.estado.find("_")

    def calcula_proximas_acoes(self):
        cima = self.posicao_vazio - 3 if self.posicao_vazio > 2 else self.posicao_vazio
        baixo = self.posicao_vazio + 3 if self.posicao_vazio < 6 else self.posicao_vazio
        esquerda = self.posicao_vazio - 1 if self.posicao_vazio not in (0, 3, 6) else self.posicao_vazio
        direita = self.posicao_vazio + 1 if self.posicao_vazio not in (2, 5, 8) else self.posicao_vazio
        
        return cima, baixo, esquerda, direita
    
    def faz_acao(self, estado_pai, direcao):
        estado_filho = list(estado_pai)
        estado_filho[self.posicao_vazio] = estado_pai[direcao]
        estado_filho[direcao] = estado_pai[self.posicao_vazio]
        return ''.join(estado_filho)
    
    def expande(self):
        cima, baixo, esquerda, direita = self.calcula_proximas_acoes()
        estado_vai_pra_cima = self.faz_acao(self.estado, cima)
        estado_vai_pra_baixo = self.faz_acao(self.estado, baixo)
        estado_vai_pra_esquerda = self.faz_acao(self.estado, esquerda)
        estado_vai_pra_direita = self.faz_acao(self.estado, direita)
        return estado_vai_pra_cima, estado_vai_pra_baixo, estado_vai_pra_esquerda, estado_vai_pra_direita

