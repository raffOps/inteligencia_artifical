import pytest
from src.nodo import Nodo
from src.direcao import Direcao

@pytest.fixture
def estado_012345_678():
    return Nodo("01234_678")


def test_vai_pra_cima_012345_6(estado_012345_678):
    estado = estado_012345_678
    proximo_estado = estado.sucessores[Direcao.CIMA.value]
    assert proximo_estado == "01_342678"


def test_vai_pra_baixo_012345_6(estado_012345_678):
    estado = estado_012345_678
    proximo_estado = estado.sucessores[Direcao.BAIXO.value]
    assert proximo_estado == "01234867_"


def test_vai_pra_direita_012345_6(estado_012345_678):
    estado = estado_012345_678
    proximo_estado = estado.sucessores[Direcao.DIREITA.value]
    assert proximo_estado == "01234_678"


def test_vai_pra_esquerda_012345_6(estado_012345_678):
    estado = estado_012345_678
    proximo_estado = estado.sucessores[Direcao.ESQUERDA.value]
    assert proximo_estado == "0123_4678"








