from queue import Queue

"""
class Grafo:
    def __init__(self):
        self.vertices = {}
        self.ultimo = None
        self.cantidad = 0


    def agregar(self, vertice, adyasente):
        # Esto es un grafo dirigido. Cada vertice es clave de los elementos a los que apunta
        self.vertices[vertice] = self.vertices.get(vertice, {})
        self.vertices[adyasente] = self.vertices.get(adyasente, {})
        self.vertices[vertice][adyasente] = None
        self.ultimo = vertice
        self.cantidad = self.cantidad + 1

    def adyasentes(self, vertice):
        return list(self.vertices[vertice])

    def cantidad(self):
        return self.cantidad

    def vertices(self):
        return list(self.vertices)
    def __recorrido_dfs(self, vertice, visitados, padres, ordenes, funcion):
        if funcion != None: funcion(vertice)
        ##if not vertice in self.vertices: return visitados, ordenes, padres
        for i in self.vertices[vertice]:
            if i not in visitados:
                visitados.add(i)
                ordenes[i] = ordenes[vertice] + 1
                padres[i] = vertice
                visitados, ordenes, padres = self.__recorrido_dfs(i, visitados, padres, ordenes, funcion)
        return visitados, ordenes, padres

    def recorrido_dfs(self, vertice, funcion):
        ##Algo a tener en cuenta, el contenido de los sets actua como punteros
        visitados = set({})
        ordenes = {}
        padres = {}
        visitados.add(vertice)
        ordenes[vertice] = 0
        padres[vertice] = None
        return self.__recorrido_dfs(vertice, visitados, padres, ordenes, funcion)

    def recorrido_bfs(self, vertice, funcion):
        cola = Queue()
        visitados = set({})
        ordenes = {}
        padres = {}
        visitados.add(vertice)
        ordenes[vertice] = 0
        padres[vertice] = None
        cola.put(vertice)

        while not cola.empty():
            vertice = cola.get()
            if funcion != None: funcion(vertice)
            ##if not vertice in self.vertices: continue
            for i in self.vertices[vertice]:
                if not i in visitados:
                    visitados.add(i)
                    padres[i] = vertice
                    ordenes[i] = ordenes[vertice] + 1
                    cola.put(i)
        return visitados, ordenes, padres


    def borrar(self, vertice):
        self.vertices.pop(vertice)
        for v in self.vertices:
            if vertice in self.vertices[v]:
                v.remove(vertice)


"""


import random
class Cola:
	def __init__(self):
		self.items = []
		self.cant = 0

	def esta_vacia(self):
		return self.cant == 0

	def encolar(self, x):
		self.items.append(x)
		self.cant += 1

	def desencolar(self):
		if self.esta_vacia():
			raise IndexError("L cola esta vacia.")
		self.cant -= 1
		return self.items.pop(0)

# class Heap:
# 	def __init__(self, comp):
# 		self.datos = []
# 		self.cant = 0
# 		self.cmp = comp
# 	def posicion_padre(self, pos_hijo):
# 		return (pos_hijo -1)/2

# 	def posicion_hijo(self, pos_padre):
# 		return (2 * pos_padre + 1, 2 * pos_padre + 2)

# 	def swap(self, x, y):
# 		aux = self.datos[x]
# 		self.datos[x] = self.datos[y]
# 		self.datos[y] = aux

# 	def encolar(self, elem):
# 		self.datos[self.cant] = elem
# 		pos_act = self.cant
# 		pos_padre = self.posicion_padre(pos_act)
# 		while (pos_padre > 0):
# 			if self.cmp == False and self.datos[pos_act] > self.datos[pos_padre]:
# 				self.swap(pos_act, pos_padre)
# 				pos_act = pos_padre
# 				pos_padre = self.posicion_padre(pos_act)
# 				continue
# 			if self.cmp == True and self.datos[pos_act][2] > self.datos[pos_padre][2]:
# 				self.swap(pos_act, pos_padre)
# 				pos_act = pos_padre
# 				pos_padre = self.posicion_padre(pos_act)
# 				continue
# 			break
# 		self.cant += 1

# 	def dowheap(self, )

# 	def desencolar(self):
# 		if 


class Grafo:
	def __init__(self, dirigido = False):
		self.vertices = {}
		self.vertices_entrada = {}
		self.cant = 0
		self.adyacentes = {}
		self.grado_salida = {}
		self.grado_entrada = {}
		self.dirigido = dirigido
	def agregar_vertice(self, vertice):
		if vertice in self.vertices:
			return
		self.vertices[vertice] = {}
		self.vertices_entrada[vertice] = []
		self.grado_entrada[vertice] = 0
		self.grado_salida[vertice] = 0
		self.adyacentes[vertice] = []
		self.cant += 1

	def sacar_vertice(self, vertice):
		if not vertice in self.vertices:
			raise Exception("No se encuentra el vertice.")
		for v in self.vertices_entrada[vertice]:
			self.vertices[v].pop(vertice)
			self.grado_salida[v] -= 1
			self.adyacentes[v].remove(vertice)
		for v in self.vertices[vertice]:
			self.vertices_entrada[v].remove(vertice)
			self.grado_entrada[v] -= 1
		self.vertices.pop(vertice)
		self.vertices_entrada.pop(vertice)
		self.adyacentes.pop(vertice)
		self.grado_salida.pop(vertice)
		self.grado_entrada.pop(vertice)
		self.cant -= 1

	def pertenece(self, vertice):
		return vertice in self.vertices

	def cantidad(self):
		return self.cant

	def union(self, vertice1, vertice2):
		if not vertice1 in self.vertices or not vertice2 in self.vertices:
			return None
		return vertice1 in self.vertices[vertice2] and vertice2 in self.vertices[vertice1]

	def obtener_grado_salida(self, vertice):
		if not vertice in self.vertices:
			return None
		return self.grado_salida[vertice]

	def obtener_grado_entrada(self, vertice):
		if not vertice in self.vertices:
			return None
		return self.grado_entrada[vertice]

	def obtener_peso(self, vertice1, vertice2):
		if not vertice1 in self.vertices or not vertice2 in self.vertices:
			raise Exeption("No se encuentra la arista")
		return self.vertices[vertice1][vertice2]

	def agregar_arista(self, vertice1, vertice2, peso = None):
		if not vertice1 in self.vertices:
			self.agregar_vertice(vertice1)
		if not vertice2 in self.vertices:
			self.agregar_vertice(vertice2)
		if not self.dirigido:
			self.adyacentes[vertice2].append(vertice1)
			self.grado_entrada[vertice1] += 1
			self.grado_salida[vertice2] += 1
		self.vertices[vertice1][vertice2] = peso
		self.vertices_entrada[vertice2].append(vertice1)
		self.grado_entrada[vertice2] += 1
		self.grado_salida[vertice1] += 1
		self.adyacentes[vertice1].append(vertice2)

	def sacar_arista(self, vertice1, vertice2):
		if not vertice1 in self.vertices and not vertice2 in self.vertices:
			raise Exception("no esta en los vertices")
			
		if not self.dirigido:
			self.grado_salida[vertice2] -= 1
			self.grado_entrada[vertice1] -= 1
			self.adyacentes[vertice2].remove(vertice1)
		self.vertices_entrada[vertice2].remove(vertice1)
		self.vertices[vertice1].pop(vertice2)
		self.grado_entrada[vertice2] -= 1
		self.grado_salida[vertice1] -= 1
		self.adyacentes[vertice1].remove(vertice2)

	def agregar_vertices(self, lista):
		for vertice in lista:
			self.agregar_vertice(vertice)

	def agregar_aristas(self, lista):
		for v1, v2, p in lista:
			self.agregar_arista(v1, v2, p)

	def obtener_vertice_al_azar(self):
		if self.cantidad == 0:
			raise Exception()
		return list(self.vertices.keys())[0]

	def obtener_vertices(self):
		return list(self.vertices.keys())

	def obtener_vertices_entrada(self, vertice):
		if not vertice in self.vertices:
			raise Exception("No se encuentra el vertice")
		return self.vertices_entrada[vertice]

	def obtener_adyacentes(self, vertice):
		if not vertice in self.vertices:
			raise Exception("No se encuentra el vertice")
		return self.adyacentes[vertice]

	def __iter__(self):
		self.lista_vertices = list(self.vertices.keys())
		self.n = 0
		return self

	def conectados(self, vertice1, vertice2):
		if vertice2 in self.vertices[vertice1]: return True
		return False

	def __next__(self):
		if self.n >= self.cant:
			raise StopIteration
		result = self.lista_vertices[self.n]
		self.n += 1
		return result








    





        




            
            
    
