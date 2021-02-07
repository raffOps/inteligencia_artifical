from src.nodo import Nodo


estado = Nodo("01234_678")
for sucessor in estado.sucessores:
    print(sucessor)