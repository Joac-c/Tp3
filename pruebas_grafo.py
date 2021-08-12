from grafo import Grafo
import grafo_lib

def imprimir_lista(lista):
	for i in range(0, len(lista) - 1):
		print("{}, ".format(lista[i]), end='')
	print(lista[len(lista) - 1])

def imprimir_comunidad(numero, lista):
	print("Comunidad {}: ".format(numero), end='')
	imprimir_lista(lista)
#cfc

ENTRANTE = 1
SALIENTE = 0

def cfc(grafo):
	antivisitados = set(grafo.obtener_vertices())
	pila = []
	i = 1
	##Esto habria que repetirlo para los vertices que pueden estar desconectados
	while len(antivisitados) != 0:
		vertice = antivisitados.pop()
		antivisitados, pila = grafo_lib._recorrido_dfs(grafo, vertice, antivisitados, pila, SALIENTE)
	
	antivisitados = set(grafo.obtener_vertices())
	
	while len(pila) != 0:
		conexos = []
		vertice = pila.pop(-1)
		if not vertice in antivisitados: continue
		antivisitados, conexos  = grafo_lib._recorrido_dfs(grafo, vertice, antivisitados, conexos, ENTRANTE)
		print("CFC {}:".format(i), end='')
		imprimir_lista(conexos)
		i += 1

def main():
    """
    g = Grafo()
    vertices = (("a", "b"),  ("b", "c"), ("b", "d"), ("c", "e"), ("d", "f"), ("d", "g"))
    for tupla in vertices:
        g.agregar(tupla[0], tupla[1])

    print("los adyasentes son")
    print(g.adyasentes("a"))
    print(g.adyasentes("b"))
    print(g.adyasentes("c"))
    print("Recorrido desde a \n")
    print("dfs\n")
    g.recorrido_dfs("a", print)
    g.recorrido_dfs("a", None)
    print("bfs\n")
    g.recorrido_bfs("a", print)
    """
    grafo = Grafo(True)
    grafo.agregar_vertices(["A", "B", "C", "D", "E", "F"])
    aristas = [("A", "B",1), ("A", "C", 5), ("B", "C", 4), ("B", "D", 1), ("D", "C", 2), ("C", "E", 1), ("E", "F", 2), ("D", "F", 3),("E", "D", 1)]
    grafo.agregar_aristas(aristas)
    print(grafo.obtener_adyacentes("B"))
    print(grafo.obtener_vertices_entrada("B"))
    print(grafo.obtener_vertices_entrada("D"))
    print(grafo.obtener_vertices_entrada("C"))
    #grafo.sacar_vertice("B")
    print(grafo.obtener_adyacentes("A"))
    print(grafo.obtener_adyacentes("D"))
    print(grafo.obtener_adyacentes("C"))
    print(grafo.obtener_vertices_entrada("A"))
    print(grafo.obtener_vertices_entrada("D"))
    print(grafo.obtener_vertices_entrada("C"))
    padre, distancia = grafo_lib.bfs(grafo, "A")
    print(padre)
    print(distancia)

    #print(grafo_lib.pagerank(grafo))
    print("prueba divulgar")
    k = grafo_lib.label_propagation(grafo)
    
    grafo = Grafo(True)
    aristas = [("A", "B",1), ("B", "C", 5), ("C", "A", 4), ("C", "D", 1), ("D", "E", 2), ("E", "F", 1), ("F", "D", 2), ("D", "S", 3),("S", "J", 1)]
    grafo.agregar_aristas(aristas)
    cfc(grafo)

    print(k)

main()