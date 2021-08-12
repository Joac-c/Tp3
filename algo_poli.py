from grafo import Grafo
import funciones_grafo


def _imprimir_camino(padres, destino, origen):
    if padres[destino] != origen: 
        _imprimir_camino(padres, padres[destino], origen)
        print("-> %d", destino)
    else:
        print("%d ", destino)
    return


def min_seguimientos(grafo, origen, destino):
    padres, orden = funciones_grafo.bfs(grafo, origen)
    _imprimir_camino(padres, destino, origen)


def mas_imp(grafo, cant):
    print(funciones_grafo.pagerank(grafo))    








