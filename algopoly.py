import grafo_lib
from grafo_lib import pagerank
from grafo import Grafo
from grafo import Cola
import sys


def main():
	redes = Grafo(True)
	dicc_pgr = {}
	lista_pgr = []
	ruta = "/home/joa/codigo/C/tp3/minimo.tsv"
	leer_archivo(ruta, redes)
	pruebas = []
	procesar_entrada(redes, dicc_pgr, lista_pgr)

	

def leer_archivo(ruta, redes):
	with open(ruta) as archivo:
		archivo.readline()
		for l in archivo:
			linea = l.rstrip("\n").split("\t")
			vertice1, vertice2 = linea[0], linea[1]

			if not redes.pertenece(vertice1):
				redes.agregar_vertice(vertice1)
			if not redes.pertenece(vertice2):
				redes.agregar_vertice(vertice2)
			if not redes.conectados(vertice1, vertice2):
				redes.agregar_arista(vertice1, vertice2)

def procesar_entrada(redes, dicc_pgr, lista_pgr):
	for linea in sys.stdin:
		linea = linea.rstrip()
		linea = linea.split(" ")
		comando = linea[0]
		parametros = linea[1:]
		procesar_comando(redes, comando, parametros, dicc_pgr, lista_pgr)

def camino_minimo(redes, origen, destino):
	if not redes.vertice_pertenece(origen) or not redes.vertice_pertenece(destino):
		print("Seguimiento imposible")
		return 
	padres, __ = bfs(redes, origen)
	if not destino in padres:
		print("Seguimiento imposible")
		return
	result = ""
	while not destino is None:
		result = destino + result
		destino = padres[destino]
		if not destino is None:
			result = " -> " + result
	print(result)

def reconstruir_camino(padres, destino):
	recorrido = []
	while not destino is None:
		recorrido.append(destino,)
		destino = padres[destino]
	return recorrido[::-1] #sale la lista al revez

def imprimir_camino(camino):
	result = camino[0]
	for v in camino[1:]:
		result += " -> " + v
	print(result)

def camino_a_mas_importante(redes, delincuentes_encubiertos, delincuentes_importantes):
	camino_corto = None
	for delinc in delincuentes_encubiertos:
		padres, orden = grafo_lib.bfs(redes, delinc)
		mas_cerca = None
		for i, imp in enumerate(delincuentes_importantes):
			if not imp in padres:
				continue
			if mas_cerca is None or orden[imp] < orden[mas_cerca]:
				mas_cerca = imp
		if mas_cerca is None or orden[mas_cerca] < camino_corto[1]:
			camino_corto = (reconstruir_camino(padres, mas_cerca), orden[mas_cerca])
			continue
	if camino_corto is None :
		return
	imprimir_camino(camino_corto[0])


#Comunidades



def imprimir_lista(lista):
	for i in range(0, len(lista) - 1):
		print("{}, ".format(lista[i]), end='')
	print(lista[len(lista) - 1])

def imprimir_comunidad(numero, lista):
	print("Comunidad {}: ".format(numero), end='')
	imprimir_lista(lista)

def imprimir_comunidades(comunidades, n):
	i = 1
	for c in comunidades:
		if len(comunidades[c]) >= n:
			imprimir_comunidad(i, comunidades[c]) #aca salta un error de suscripcion de int ???
			i = i + 1

def comunidades(grafo, n):
	comunidades = grafo_lib.label_propagation(grafo)
	imprimir_comunidades(comunidades, n)



#divulgar

#Para esta funcion hay que ver como reutilizar el bfs usado en min_seguimientos

def divulgar(grafo, delincuente, n):
		cola = Cola()
		visitados = set({})
		distancias = {}
		visitados.add(delincuente)
		distancias[delincuente] = 0
		cola.encolar(delincuente)

		while not cola.esta_vacia():
			vertice = cola.desencolar()
			for i in grafo.obtener_adyacentes(vertice):
				if not i in visitados:
					visitados.add(i)
					distancias[i] = distancias[vertice] + 1
					if distancias[i] < n: cola.encolar(i)
		visitados.discard(delincuente)
		imprimir_lista(list(visitados))




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




## divulgacion de Ciclo

def condicion(vertice, distancias, extra):
	if extra[0] == vertice and distancias[vertice] == extra[1] : return True
	else: return False


def divulgar_ciclo(redes, delincuente, n):
	extra = (delincuente, n)
	visitados, camino, exito = grafo_lib.backtraking(redes, delincuente, condicion, extra)
	if not exito: print("No se encontro recorrido")
	else: imprimir_camino(camino)



## Procesar Comando


def procesar_comando(redes, comando, parametros, dicc_pgr, lista_pgr):
	if comando == "min_seguimientos":
		origen, destino = parametros[0], parametros[1]
		camino_minimo(redes, origen, destino)

	elif comando == "mas_imp":
		cant = int(parametros[0])
		if len(dicc_pgr) == 0:
			for __ in range(9):
				dicc_pgr = pagerank(redes)
			for nombre in dicc_pgr:
				lista_pgr.append((nombre, dicc_pgr[nombre]))
			lista_pgr.sort(reverse = True) 
		result = ""
		cont = 0
		for nombre, __ in lista_pgr:
			result += f'{nombre}, '
			cont += 1 
			if cont == cant:
				break
		print(result[:-2])

	elif comando == "persecucion":
		delincuentes = parametros[0].split(",")
		k = int(parametros[1])
		if len(dicc_pgr) == 0:
			for __ in range(11):
				dicc_pgr = grafo_lib.PageRank(redes)
			for nombre in dicc_pgr:
				lista_pgr.append((nombre, dicc_pgr[nombre]))
			lista_pgr.sort(reverse = True) 
		camino_a_mas_importante(redes, delicuentes, lista_pgr[0:k])

	elif comando == "comunidades":
		n = int(parametros[0])
		comunidades(redes, n)
		pass
	elif comando == "divulgar":
		delincuente = parametros[0]
		n = int(parametros[1])
		divulgar(redes, delincuente, n)
		pass
	elif comando == "divulgar_ciclo":
		delincuente = parametros[0]
		n = int(parametros[1])
		divulgar_ciclo(redes, delincuente, n)
		pass
	elif comando == "cfc":
		cfc(redes)
		pass


main()

