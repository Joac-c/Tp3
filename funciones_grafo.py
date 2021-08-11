from grafo import Grafo
from queue import PriorityQueue
from random import shuffle
"""
    Comando: min_seguimientos.
    Parámetros: origen y destino.
    Utilidad: nos imprime una lista con los delincuentes 
    (su código identificador) con los cuáles vamos del 
    delincuente origen al delincuente destino de la forma
    más rápida. En caso de no poder hacer el seguimiento 
    (i.e. no existe camino), imprimir Seguimiento imposible.
    Ejemplo:
    Entrada:

      min_seguimientos 10 4
      min_seguimientos 30 12

    Salida:

      10 -> 57 -> 4
      30 -> 36 -> 38 -> 20 -> 45 -> 12

"""

def _imprimir_camino(padres, destino, origen):
    if padres[destino] != origen: 
        _imprimir_camino(padres, padres[destino], origen)
        print("-> %d", destino)
    else:
        print("%d ", destino)
    return


def min_seguimientos(grafo, origen, destino):
    ##uso djstra
    dist = {}
    padres = {}
    heap = PriorityQueue()
    dist[origen] = 0    
    padres[origen] = none
    heap.put((distancia[origen], origen))
    padres[origen] = none

    while not heap.empty:
        dv, v = heap_desencolar(heap)
        for w in grafo.obtener_adyasentes(v):
            if not w in dist or (dv + 1) < dist[w]):
                dist[w] = dv + 1
                heap.put((dist[w], w))
                padres[w] = v
    if not destino in padres: print("Seguimiento imposible")
    _imprimir_camino(padres, destino, origen)


    







"""
    Usualmente nos gustaría determinar cuáles son los vértices 
    más importantes en un grafo en función de su centralidad exacta. 
    Teniendo en cuenta que se cuenta con demasiados delincuentes, 
    el cálculo exacto de la centralidad puede consumir una cantidad 
    excesiva de tiempo. Por lo tanto, se pide realizar una aproximación 
    para determinar los delincuentes más importantes. La forma sugerida 
    para realizar esto es utilizando el algoritmo PageRank.

    Por lo tanto, el comando pedido debe ser:

    Comando: mas_imp.
    Parámetros: cant.

    Utildad: Imprime, de mayor a menor importancia, los cant delincuentes más importantes.
    
    Ejemplo:
        Entrada:

            mas_imp 10

        Salida:

            20, 89, 42, 3, 49, 47, 56, 28, 22, 8

    Considerar que el “score” de pagerank no va a cambiar por más que se ejecute muchas veces diferentes, por lo que lo mejor será calcular únicamente la primera vez que se pidan, manteniendo guardado los scores para reutilizarlos si se vuelven a necesitar.
"""


def _sumatoria(grafo, vert, pr):
	suma = 0
	d = 0.85
	for v in grafo.obtener_vertices_entrada(vert):
		if not v in pr:
			pr[v] = 1 / grafo.cantidad()
		suma += pr[v] / grafo.obtener_grado_salida(v)
	pr[vert] += d * suma

def pagerank(grafo):
	pr = {}
	d = 0.85
	formula = (1 - d) / grafo.cantidad()
	for v in grafo:
		if not v in pr:
			pr[v] = formula
		_sumatoria(grafo, v, pr)
	return pr

print(pagerank(grafo))


def mas_imp(grafo, cant):
    grafo = Grafo()
    vertices = grafo.vertices()
    ranks = {}
    
    for vertice in vertices:
        ranks[vertice] = [0, 1]


    shuffle(vertices)
    for vertice in vertices:
        ranks[vertice][0] = ranks[vertice][1]
        adyasentes = grafo.obtener_adyasentes(vertice)
        for i in adyasentes:
            ranks[i] = ranks[i] + ranks[vertice] / len(adyasentes)



"""
    Comando: persecucion.
    Parámetros: delincuente1,delincuente2,...,delincuenteN y K.

    Utilidad: Dado cada uno de los delincuentes pasados 
    (agentes encubiertos), obtener cuál es el camino más corto 
    para llegar desde alguno de los delincuentes pasados por 
    parámetro, a alguno de los K delincuentes más importantes. 
    En caso de tener caminos de igual largo, priorizar los que vayan
    a un delincuente más importante.

    Ejemplo:

        Entrada:

        persecucion 10,14,17 5
        persecucion 19,11,7,12 3

        Salida:

        17 -> 35 -> 20
        19 -> 42

"""


def persecucion():







"""Para implementar esto, utilizaremos el algoritmo de Label Propagation para detectar comunidades.

    Comando: comunidades.
    Parámetros: n.
    Utilidad: Imprime un listado de comunidades de al menos n integrantes.
    Ejemplo:
    Entrada:

    comunidades 10

    Salida:

    Comunidad 1: 0, 39, 59, 1, 47, 62, 2, 20, 3, 37, 31, 96, 16, 32, 80, 14, 40, 13, 89, 64, 72, 21, 15, 50, 97, 4, 17, 67, 6, 74, 54, 73, 93, 11, 65, 57, 70, 75, 7, 29, 8, 19, 55, 69, 33, 78, 44, 84, 43, 9, 42, 10, 53, 58, 35, 48, 45, 12, 25, 52, 71, 66, 36, 41, 79, 99, 92, 28, 56, 23, 18, 91, 34, 86, 30, 81, 38, 51, 87, 88, 22, 46, 63, 24, 95, 82, 49, 26, 27, 83, 90, 68, 94, 98, 61, 85, 76, 77, 60

Tener en cuenta que siendo un archivo generado de forma aleatoria, los resultados obtenibles para este punto tienen muy poco sentido con la realidad.
"""









def obtener_maximo(diccionario):
    maximo = max(diccionario, key = lambda k: diccionario[k])


def imprimir_lista(lista):
    for i in range(0, len(lista) - 2):
        print("%s, " lista[i])
    print("%s\n" lista[len(lista) - 1])

def imprimir_comunidad(numero, lista):
    print("Comunidad %d:", numero)
    imprimir_lista(lista)
    print("%s\n" lista[len(lista) - 1])
        

def comunidades(grafo, n):
    etiquetas = {}
    #Se supone que debeira inicializar (O(v)) y recorrer las aristas(O(e)). 
    #Esto ultimo sucede en promedio 6-8 veces.
    entradas = {}
    i = 0

    vertices = grafo.obtener_vertices()

    #inicializamos
    for v in vertices:
        #para los vertices vamos a armar una lista
        etiquetas[v] = i
        for e in grafo.obtener_adyasentes(v):
            entradas[e] = entradas.get(e, {})
            entradas[e][i] = entradas[e].get(i, 0) + 1
        i = i + 1

    #iteraciones
    completos = False
    while not completos:
        #Necesito buscar un iterador random
        shuffle(vertices)
        for vertice in vertices:
            e = obtener_maximo(entradas[vertice])
            antiguo = etiquetas[vertice]
            etiquetas[vertice] = e
            if antiguo == e: completos = True
            else completos = False
            for i in grafo.obtener_adyasentes[v]:
                entradas[vertice][antiguo] = entradas[vertice][antiguo] - 1
                entradas[vertice][i] = entradas[e].get(i, 0) + 1
    
    comunidades = {}
    for v in etiquetas:
        comunidades[etiquetas[v]] = comunidades.get(etiquetas[v], [0, []])
        comunidades[etiquetas[v]][0] = comunidades[etiquetas[v]][0] + 1
        comunidades[etiquetas[v]][1].append(v)
    i = 0
    for c in comunidades:
        if c[0] >= n: imprimir_comunidad(i, c[1])
        i = i + 1



"""Divulgación de rumor

    Comando: divulgar.
    Parámetros: delincuente y n.
    Utilidad: Imprime una lista con todos los delincuentes a los cuales les termina llegando un rumor que comienza 
    en el delincuente pasado por parámetro, y a lo sumo realiza n saltos (luego, se empieza a tergiversar el mensaje), teniendo en cuenta que todos los delincuentes transmitirán el rumor a sus allegados.
    Ejemplo:
    Entrada

    divulgar 30 4
    divulgar 30 1

    Salida:

    36, 79, 84, 38, 71, 48, 13, 76, 77, 20, 64, 72, 57, 23, 7, 24, 85, 61, 47, 19, 25, 40, 37, 52, 56, 74, 66, 1, 18, 27, 26, 80, 62, 97, 86, 15, 53, 31, 78, 99, 81, 6, 29, 11, 33, 45, 51, 65, 87, 42, 50, 93, 41, 90, 4, 70, 92, 67, 95, 0, 82, 63, 60, 5, 9, 68, 59, 89, 34, 8, 14, 73, 28, 16, 49, 43, 83, 75, 39, 21, 32, 54, 55, 17, 91, 46
    36, 79, 84

""""

def imprimir_visitados(visitados):
    for i in range(0, len(visitados) - 2):



def divulgar(grafo, delincuente, n):
        cola = Queue()
        visitados = set({})
        distancias = {}
        visitados.add(delincuente)
        distancias[delincuente] = 0
        cola.put(delincuente)

        while not cola.empty():
            vertice = cola.get()
            if distancias[vertice] < n:
                for i in self.vertices[vertice]:
                    if not i in visitados:
                        visitados.add(i)
                        distancias[i] = distancias[vertice] + 1
                        if distancias[i] < n: cola.put(i)
        imprimir_lista(list(visitados))
    
    

            

    
