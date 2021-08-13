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