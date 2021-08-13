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

	def conectados(self, vertice1, vertice2):
		return vertice2 in self.vertices[vertice1]

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
		if vertice1 == vertice2:
			return
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

	def __next__(self):
		if self.n >= self.cant:
			raise StopIteration
		result = self.lista_vertices[self.n]
		self.n += 1
		return result


