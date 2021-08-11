from grafo import Grafo


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
    grafo.sacar_vertice("B")
    print(grafo.obtener_adyacentes("A"))
    print(grafo.obtener_adyacentes("D"))
    print(grafo.obtener_adyacentes("C"))
    print(grafo.obtener_vertices_entrada("A"))
    print(grafo.obtener_vertices_entrada("D"))
    print(grafo.obtener_vertices_entrada("C"))
    padre, distancia = bfs(grafo, "B")
    print(padre)
    print(distancia)

main()