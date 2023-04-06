import numpy as np


def get_tabuleiro():
    with open("arquivo_estado_tabuleiro") as file:
        tabuleiro = [list(file.readline()[:-1]) for _ in range(8)]
        tabuleiro = np.array(tabuleiro).reshape(8, 8)
        return tabuleiro


def get_localizacao_pecas(tabuleiro, jogador):
    posicoes_linha, posicoes_coluna = np.where(tabuleiro == jogador)
    return list(zip(posicoes_linha, posicoes_coluna))


def procura_jogada_direita(peca_jogador_x, peca_jogador_y, oponente, tabuleiro):
    pecas_capturadas = []
    posicao_vazio = None
    for posicao_coluna_a_direita in range(peca_jogador_y+1, 8):
        if tabuleiro[peca_jogador_x, posicao_coluna_a_direita] == oponente:
            pecas_capturadas.append((peca_jogador_x, posicao_coluna_a_direita))
        elif tabuleiro[peca_jogador_x, posicao_coluna_a_direita] == ".":
            posicao_vazio = (peca_jogador_x, posicao_coluna_a_direita)
            break
    return posicao_vazio, pecas_capturadas


def procura_jogada_diagonal_45(peca_jogador_x, peca_jogador_y, oponente, tabuleiro):
    pecas_capturadas = []
    posicao_vazio = None
    linha, coluna = peca_jogador_x, peca_jogador_y
    while True:
        linha -= 1
        coluna += 1
        if linha < 0 or coluna > 7:
            break
        elif tabuleiro[linha, coluna] == ".":
            posicao_vazio = (linha, coluna)
            break
        elif tabuleiro[linha, coluna] == oponente:
            pecas_capturadas.append((linha, coluna))

    return posicao_vazio, pecas_capturadas


def procura_jogada_cima(peca_jogador_x, peca_jogador_y, oponente, tabuleiro):
    pecas_capturadas = []
    posicao_vazio = None
    for posicao_linha_em_cima in range(peca_jogador_x - 1, 0, -1):
        if tabuleiro[posicao_linha_em_cima, peca_jogador_y] == oponente:
            pecas_capturadas.append((posicao_linha_em_cima, peca_jogador_y))
        elif tabuleiro[posicao_linha_em_cima, peca_jogador_y] == ".":
            posicao_vazio = (posicao_linha_em_cima, peca_jogador_y)
            break
    return posicao_vazio, pecas_capturadas


def procura_jogada_diagonal_135(peca_jogador_x, peca_jogador_y, oponente, tabuleiro):
    pecas_capturadas = []
    posicao_vazio = None
    linha, coluna = peca_jogador_x, peca_jogador_y
    while True:
        linha -= 1
        coluna -= 1
        if linha < 0 or coluna < 0:
            break
        elif tabuleiro[linha, coluna] == ".":
            posicao_vazio = (linha, coluna)
            break
        elif tabuleiro[linha, coluna] == oponente:
            pecas_capturadas.append((linha, coluna))

    return posicao_vazio, pecas_capturadas


def procura_jogada_esquerda(peca_jogador_x, peca_jogador_y, oponente, tabuleiro):
    pecas_capturadas = []
    posicao_vazio = None
    for posicao_coluna_a_esquerda in range(peca_jogador_y - 1, 0, -1):
        if tabuleiro[peca_jogador_x, posicao_coluna_a_esquerda] == oponente:
            pecas_capturadas.append((peca_jogador_x, posicao_coluna_a_esquerda))
        elif tabuleiro[peca_jogador_x, posicao_coluna_a_esquerda] == ".":
            posicao_vazio = (peca_jogador_x, posicao_coluna_a_esquerda)
            break
    return posicao_vazio, pecas_capturadas


def procura_jogada_diagonal_225(peca_jogador_x, peca_jogador_y, oponente, tabuleiro):
    pecas_capturadas = []
    posicao_vazio = None
    linha, coluna = peca_jogador_x, peca_jogador_y
    while True:
        linha += 1
        coluna -= 1
        if linha > 7 or coluna < 0:
            break
        elif tabuleiro[linha, coluna] == ".":
            posicao_vazio = (linha, coluna)
            break
        elif tabuleiro[linha, coluna] == oponente:
            pecas_capturadas.append((linha, coluna))

    return posicao_vazio, pecas_capturadas


def procura_jogada_baixo(peca_jogador_x, peca_jogador_y, oponente, tabuleiro):
    pecas_capturadas = []
    posicao_vazio = None
    for posicao_linha_em_baixo in range(peca_jogador_x + 1, 8):
        if tabuleiro[posicao_linha_em_baixo, peca_jogador_y] == oponente:
            pecas_capturadas.append((posicao_linha_em_baixo, peca_jogador_y))
        elif tabuleiro[posicao_linha_em_baixo, peca_jogador_y] == ".":
            posicao_vazio = (posicao_linha_em_baixo, peca_jogador_y)
            break

    return posicao_vazio, pecas_capturadas


def procura_jogada_diagonal_315(peca_jogador_x, peca_jogador_y, oponente, tabuleiro):
    pecas_capturadas = []
    posicao_vazio = None
    linha, coluna = peca_jogador_x, peca_jogador_y
    while True:
        linha += 1
        coluna += 1
        if linha > 7 or coluna > 7:
            break
        elif tabuleiro[linha, coluna] == ".":
            posicao_vazio = (linha, coluna)
            break
        elif tabuleiro[linha, coluna] == oponente:
            pecas_capturadas.append((linha, coluna))

    return posicao_vazio, pecas_capturadas


def get_jogadas_disponiveis(tabuleiro, jogador):
    oponente = "W" if jogador == "B" else "B"
    localizacao_pecas_jogador = get_localizacao_pecas(tabuleiro, jogador)
    jogadas_disponiveis = []
    for peca_jogador_x, peca_jogador_y in localizacao_pecas_jogador:
        direcao = [procura_jogada_direita, procura_jogada_diagonal_45,
                   procura_jogada_cima, procura_jogada_diagonal_135,
                   procura_jogada_esquerda, procura_jogada_diagonal_225,
                   procura_jogada_baixo, procura_jogada_diagonal_315]
        for procura in direcao:
            posicao_vazio, pecas_do_oponente_capturadas = procura(peca_jogador_x, peca_jogador_y,
                                                                                       oponente, tabuleiro)
            if posicao_vazio and pecas_do_oponente_capturadas:
                posicoes_capturadas = pecas_do_oponente_capturadas
                posicoes_capturadas.append(posicao_vazio)
                jogadas_disponiveis.append((posicao_vazio, pecas_do_oponente_capturadas))

    return jogadas_disponiveis


def get_heuristica(posicoes_capturadas):
    return sum(
        10 if posicao_x in [0, 7] or posicao_y in [0, 7] else 1
        for posicao_x, posicao_y in posicoes_capturadas
    )

# tabuleiro = get_tabuleiro()
# jogadas_disponiveis = get_jogadas_disponiveis(tabuleiro, "B")
# jogadas_disponiveis_com_heuristica = [(jogada, posicoes_capturadas, get_heuristica(posicoes_capturadas))
#                                       for (jogada, posicoes_capturadas) in jogadas_disponiveis]
#
# print(jogadas_disponiveis_com_heuristica)