from grafo import Grafo
from grafo import Cola
from random import shuffle





def bfs(grafo, origen):
	visitados = set()
	padres = {}
	orden = {}
	padres[origen] = None
	orden[origen] = 0
	visitados.add(origen)
	q = Cola()
	q.encolar(origen)
	while not q.esta_vacia():
		v = q.desencolar()
		for w in grafo.obtener_adyacentes(v):
			if not w in visitados:
				padres[w] = v
				orden[w] = orden[v] + 1
				visitados.add(w)
				q.encolar(w)
	return padres, orden




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


def obtener_maximo(lista, diccionario):
    etiquetas = {}
    for x in lista:
        etiquetas[diccionario[x]] = etiquetas.get(diccionario[x], 0) + 1
    maximo = None
    for i in etiquetas:
        if not maximo or etiquetas[i] > etiquetas[maximo]: maximo = i
    
    return maximo

def label_propagation(grafo):
    
    #Se supone que debeira inicializar (O(v)) y recorrer las aristas(O(e)). 
    #Esto ultimo sucede en promedio 6-8 veces.
    
    #entradas = {}
    etiquetas = {}
    vertices = grafo.obtener_vertices()
    #inicializamos
    i = 0
    for v in vertices:
        #para los vertices vamos a armar una lista
        etiquetas[v] = i
        i += 1
    #iteraciones
    completos = False
    k = 0
    while not completos:
        shuffle(vertices)
        for vertice in vertices:
            e = None
            if grafo.obtener_grado_entrada(vertice) != 0:
                entradas = grafo.obtener_vertices_entrada(vertice)
                entradas.append(vertice) 
                e = obtener_maximo(entradas, etiquetas)
            if e and e != etiquetas[vertice]:
                completos = False
                etiquetas[vertice] = e
            else: completos = True
        k += 1
        if k == 10: completos = True

    comunidades = {}
    for v in etiquetas:
        if not etiquetas[v] in comunidades: comunidades[etiquetas[v]] = comunidades.get(etiquetas[v], [])
        comunidades[etiquetas[v]].append(v)
    return comunidades
    
    

    

ENTRANTE = 1
SALIENTE = 0

def devolver_aristas(grafo, vertice, direccion):
    if ENTRANTE == direccion:
        return grafo.obtener_vertices_entrada(vertice)
    if SALIENTE == direccion:
        return grafo.obtener_adyacentes(vertice)


def _recorrido_dfs(grafo, vertice, antivisitados, lista_visitados, direccion):
    for i in devolver_aristas(grafo, vertice, direccion) :
        if i in antivisitados:
            antivisitados.discard(i)
            antivisitados, lista_visitados = _recorrido_dfs(grafo, i, antivisitados, lista_visitados, direccion)
            lista_visitados.append(i)

    return antivisitados, lista_visitados

def recorrido_dfs(grafo, vertice, direccion):
        
    
    antivisitados = set(grafo.obtener_vertices())
    antivisitados.discard(vertice)
    lista_visitados = []
    return _recorrido_dfs(grafo, vertice, antivisitados, lista_visitados, direccion)






