import numpy as np


def get_tabuleiro():
    with open("arquivo_estado_tabuleiro") as file:
        tabuleiro = [[char for char in file.readline()[:-1]] for _ in range(8)]
        tabuleiro = np.array(tabuleiro).reshape(8, 8)
        return tabuleiro


def get_localizacao_pecas(tabuleiro, jogador):
    localizacoes = list(zip(np.where(tabuleiro == jogador)))
    return localizacoes


def get_jogadas_disponiveis(tabuleiro, jogador):
    oponente = "W" if jogador == "B" else "B"
    localizacao_pecas_oponentes = get_localizacao_pecas(tabuleiro, oponente)
    return localizacao_pecas_oponentes




tabuleiro = get_tabuleiro()
get_jogadas_disponiveis(tabuleiro, "B")