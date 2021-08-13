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
	for v in grafo.obtener_adyacentes(vert):
		if not v in pr:
			pr[v] = 1 / grafo.cantidad()
		suma += pr[v] / grafo.obtener_grado_salida(v)
	pr[vert] += d * suma

def pagerank(grafo):
	pr = {}
	d = 0.85
	formula = (1 - d) / grafo.cantidad()
	for i in range(0, 11):
		for v in grafo:
			if not v in pr:
				pr[v] = formula
			_sumatoria(grafo, v, pr)
	return pr


def obtener_maximo(lista, diccionario):
	shuffle(lista)
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

	while not completos:
		# En 6 iteraciones deberia completarse el 95%
		completos = True
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


def _recorrido_dfs(grafo, vertice, faltan_visitar, lista_visitados, direccion):
	faltan_visitar.discard(vertice)
	for i in devolver_aristas(grafo, vertice, direccion) :
		if i in faltan_visitar:
			faltan_visitar, lista_visitados = _recorrido_dfs(grafo, i, faltan_visitar, lista_visitados, direccion)
	lista_visitados.append(vertice)
	return faltan_visitar, lista_visitados

def recorrido_dfs(grafo, vertice, direccion):	
	faltan_visitar = set(grafo.obtener_vertices())
	faltan_visitar.discard(vertice)
	lista_visitados = []
	return _recorrido_dfs(grafo, vertice, faltan_visitar, lista_visitados, direccion)



CONDICION_EXITO = 1
CONDICION_RECURSION = -1


def _backtraking(grafo, vertice, condicion, extra, visitados, camino, distancias):
	camino.append(vertice)
	condicion = condicion(vertice, distancias, extra)
	if condicion == CONDICION_EXITO:
		return visitados, camino, True
	
	elif condicion == CONDICION_RECURSION:
		for i in devolver_aristas(grafo, vertice, SALIENTE):
			if not i in visitados:
				visitados.add(i)
				distancias[i] = distancias[vertice] + 1 
				x, camino, exito =  _backtraking(grafo, i, condicion, extra, visitados, camino, distancias)
				if exito == True: return visitados, camino, exito
				else:
					camino.pop(-1)
	visitados.discard(vertice)
	return visitados, camino, False



def backtraking(grafo, vertice, condicion, extra):
	visitados = set({})
	camino = []
	distancias = {}
	distancias[vertice] = 0
	return _backtraking(grafo, vertice, condicion, extra, visitados, camino, distancias)












