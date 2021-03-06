import numpy as np


def get_tabuleiro():
    with open("arquivo_estado_tabuleiro") as file:
        tabuleiro = [[char for char in file.readline()[:-1]] for _ in range(8)]
        tabuleiro = np.array(tabuleiro).reshape(8, 8)
        return tabuleiro


def get_localizacao_pecas(tabuleiro, jogador):
    posicoes_linha, posicoes_coluna = np.where(tabuleiro == jogador)
    return list(zip(posicoes_linha, posicoes_coluna))


def procura_jogada_direita(peca_jogador_x, peca_jogador_y, oponente, tabuleiro):
    pecas_do_oponentes_possiveis_de_serem_capturadas = []
    posicao_vazio = None
    for posicao_coluna_a_direita in range(peca_jogador_y+1, 8):
        if tabuleiro[peca_jogador_x, posicao_coluna_a_direita] == oponente:
            pecas_do_oponentes_possiveis_de_serem_capturadas.append((peca_jogador_x, posicao_coluna_a_direita))
        elif tabuleiro[peca_jogador_x, posicao_coluna_a_direita] == ".":
            posicao_vazio = (peca_jogador_x, posicao_coluna_a_direita)
            break
    if pecas_do_oponentes_possiveis_de_serem_capturadas and posicao_vazio:
        return posicao_vazio, pecas_do_oponentes_possiveis_de_serem_capturadas


def procura_jogada_diagonal_45(peca_jogador_x, peca_jogador_y, oponente, tabuleiro):
    pecas_do_oponentes_possiveis_de_serem_capturadas = []
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
            pecas_do_oponentes_possiveis_de_serem_capturadas.append((linha, coluna))

    if pecas_do_oponentes_possiveis_de_serem_capturadas and posicao_vazio:
        return posicao_vazio, pecas_do_oponentes_possiveis_de_serem_capturadas


def procura_jogada_cima(peca_jogador_x, peca_jogador_y, oponente, tabuleiro):
    pecas_do_oponentes_possiveis_de_serem_capturadas = []
    posicao_vazio = None
    for posicao_linha_em_cima in range(peca_jogador_x - 1, 0, -1):
        if tabuleiro[posicao_linha_em_cima, peca_jogador_y] == oponente:
            pecas_do_oponentes_possiveis_de_serem_capturadas.append((posicao_linha_em_cima, peca_jogador_y))
        elif tabuleiro[posicao_linha_em_cima, peca_jogador_y] == ".":
            posicao_vazio = (posicao_linha_em_cima, peca_jogador_y)
            break
    if pecas_do_oponentes_possiveis_de_serem_capturadas and posicao_vazio:
        return posicao_vazio, pecas_do_oponentes_possiveis_de_serem_capturadas


def procura_jogada_diagonal_135(peca_jogador_x, peca_jogador_y, oponente, tabuleiro):
    pecas_do_oponentes_possiveis_de_serem_capturadas = []
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
            pecas_do_oponentes_possiveis_de_serem_capturadas.append((linha, coluna))

    return posicao_vazio, pecas_do_oponentes_possiveis_de_serem_capturadas


def procura_jogada_esquerda(peca_jogador_x, peca_jogador_y, oponente, tabuleiro):
    pecas_do_oponentes_possiveis_de_serem_capturadas = []
    posicao_vazio = None
    for posicao_coluna_a_esquerda in range(peca_jogador_y - 1, 0, -1):
        if tabuleiro[peca_jogador_x, posicao_coluna_a_esquerda] == oponente:
            pecas_do_oponentes_possiveis_de_serem_capturadas.append((peca_jogador_x, posicao_coluna_a_esquerda))
        elif tabuleiro[peca_jogador_x, posicao_coluna_a_esquerda] == ".":
            posicao_vazio = (peca_jogador_x, posicao_coluna_a_esquerda)
            break
    if pecas_do_oponentes_possiveis_de_serem_capturadas and posicao_vazio:
        return posicao_vazio, pecas_do_oponentes_possiveis_de_serem_capturadas


def procura_jogada_diagonal_225(peca_jogador_x, peca_jogador_y, oponente, tabuleiro):
    pecas_do_oponentes_possiveis_de_serem_capturadas = []
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
            pecas_do_oponentes_possiveis_de_serem_capturadas.append((linha, coluna))

    if pecas_do_oponentes_possiveis_de_serem_capturadas and posicao_vazio:
        return posicao_vazio, pecas_do_oponentes_possiveis_de_serem_capturadas


def procura_jogada_baixo(peca_jogador_x, peca_jogador_y, oponente, tabuleiro):
    pecas_do_oponentes_possiveis_de_serem_capturadas = []
    posicao_vazio = None
    for posicao_linha_em_baixo in range(peca_jogador_x + 1, 8):
        if tabuleiro[posicao_linha_em_baixo, peca_jogador_y] == oponente:
            pecas_do_oponentes_possiveis_de_serem_capturadas.append((posicao_linha_em_baixo, peca_jogador_y))
        elif tabuleiro[posicao_linha_em_baixo, peca_jogador_y] == ".":
            posicao_vazio = (posicao_linha_em_baixo, peca_jogador_y)
            break
    if pecas_do_oponentes_possiveis_de_serem_capturadas and posicao_vazio:
        return posicao_vazio, pecas_do_oponentes_possiveis_de_serem_capturadas

def procura_jogada_diagonal_315(peca_jogador_x, peca_jogador_y, oponente, tabuleiro):
    pecas_do_oponentes_possiveis_de_serem_capturadas = []
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
            pecas_do_oponentes_possiveis_de_serem_capturadas.append((linha, coluna))

    if pecas_do_oponentes_possiveis_de_serem_capturadas and posicao_vazio:
        return posicao_vazio, pecas_do_oponentes_possiveis_de_serem_capturadas


def get_jogadas_disponiveis(tabuleiro, jogador):
    oponente = "W" if jogador == "B" else "B"
    localizacao_pecas_jogador = get_localizacao_pecas(tabuleiro, jogador)
    jogadas_disponiveis = {}
    for peca_jogador_x, peca_jogador_y in localizacao_pecas_jogador:
        jogadas_disponiveis[(peca_jogador_x, peca_jogador_y)] = []
        direcao = [procura_jogada_direita, procura_jogada_diagonal_45,
                   procura_jogada_cima, procura_jogada_diagonal_135,
                   procura_jogada_esquerda, procura_jogada_diagonal_225,
                   procura_jogada_baixo, procura_jogada_diagonal_315]
        for procura in direcao:
            jogadas = procura(peca_jogador_x, peca_jogador_y, oponente, tabuleiro)
            if jogadas:
                jogadas_disponiveis[(peca_jogador_x, peca_jogador_y)].append(jogadas)

    return jogadas_disponiveis

tabuleiro = get_tabuleiro()
get_jogadas_disponiveis(tabuleiro, "B")