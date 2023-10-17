from primitivas import segmentosInterceptam

# possíveis posições de um ponto em relação a um segmento
esquerda, direita = 0, 1

class EndPoint:
	"""Representa um ponto de varredura
	:param ponto: ponto de varredura
	:param posicao: posição do ponto em relação ao segmento (início ou fim)
	:param numSegmento: número do segmento ao qual o ponto pertence"""
	def __init__(self, ponto, posicao, numSegmento):
		self.ponto = ponto
		self.posicao = posicao
		self.numSegmento = numSegmento

class No:
	"""Representa um nó de uma árvore binária balanceada
	:param data: dado armazenado no nó
	:param esquerda: filho esquerdo
	:param direita: filho direito"""
	def __init__(self, data):
		self.data = data
		self.setaFilhos(None, None)

	def setaFilhos(self, esquerda, direita):
		self.esquerda = esquerda
		self.direita = direita

	def balanco(self):
		prof_esq = 0
		if self.esquerda:
			prof_esq = self.esquerda.profundidade()
		prof_dir = 0
		if self.direita:
			prof_dir = self.direita.profundidade()
		return prof_esq - prof_dir

	def profundidade(self):
		prof_esq = 0
		if self.esquerda:
			prof_esq = self.esquerda.profundidade()
		prof_dir = 0
		if self.direita:
			prof_dir = self.direita.profundidade()
		return 1 + max(prof_esq, prof_dir)

	def rotacaoEsquerda(self):
		self.data, self.direita.data = self.direita.data, self.data
		old_esquerda = self.esquerda
		self.setaFilhos(self.direita, self.direita.direita)
		self.esquerda.setaFilhos(old_esquerda, self.esquerda.esquerda)

	def rotacaoDireita(self):
		self.data, self.esquerda.data = self.esquerda.data, self.data
		old_direita = self.direita
		self.setaFilhos(self.esquerda.esquerda, self.esquerda)
		self.direita.setaFilhos(self.direita.direita, old_direita)

	def rotacaoEsquerdaDireita(self):
		self.esquerda.rotacaoEsquerda()
		self.rotacaoDireita()

	def rotacaoDireitaEsquerda(self):
		self.direita.rotacaoDireita()
		self.rotacaoEsquerda()

	def executaBalanco(self):
		bal = self.balanco()
		if bal > 1:
			if self.esquerda.balanco() > 0:
				self.rotacaoDireita()
			else:
				self.rotacaoEsquerdaDireita()
		elif bal < -1:
			if self.direita.balanco() < 0:
				self.rotacaoEsquerda()
			else:
				self.rotacaoDireitaEsquerda()

	def insere(self, data, func):
		"""Insere um nó na árvore binária de busca com base em uma função do tipo (data, data) -> bool"""
		if func(data, self.data):
			if not self.esquerda:
				self.esquerda = No(data)
			else:
				self.esquerda.insere(data, func)
		else:
			if not self.direita:
				self.direita = No(data)
			else:
				self.direita.insere(data, func)
		self.executaBalanco()
	
	def remove(self, data, func):
		"""Remove um nó da árvore binária de busca com base em uma função do tipo (data, data) -> bool"""
		if self.data == data:
			if self.esquerda:
				self.data = self.esquerda.maximo()
				self.esquerda.remove(self.data, func)
			elif self.direita:
				self.data = self.direita.minimo()
				self.direita.remove(self.data, func)
			else:
				self.data = None
		elif self.esquerda and func(data, self.data):
			self.esquerda.remove(data, func)
		elif self.direita and not func(data, self.data):
			self.direita.remove(data, func)
		self.executaBalanco()
	
	def acima(self, ponto):
		if self.data.ponto[1] <= ponto[1]:
			return self.data
		else:
			if self.esquerda:
				return self.esquerda.acima(ponto)
			else:
				return None
	
	def abaixo(self, ponto):
		if self.data.ponto[1] >= ponto[1]:
			return self.data
		else:
			if self.direita:
				return self.direita.abaixo(ponto)
			else:
				return None

	def imprimeArvore(self, indent = 0):
		print(" " * indent + str(self.data))
		if self.esquerda:
			self.esquerda.imprimeArvore(indent + 2)
		if self.direita:
			self.direita.imprimeArvore(indent + 2)

def varreduraLinear(segmentos):
	"""Verifica se há interseção entre segmentos em tempo O(n log n)
	:param segmentos: lista de segmentos de linha
	:return: True se há interseção, False caso contrário"""
	pontosVarredura = []
	for i in range(len(segmentos)):
		pontosVarredura.append(EndPoint(segmentos[i][0], esquerda, i))
		pontosVarredura.append(EndPoint(segmentos[i][1], direita, i))

	# ordena os pontos de varredura por x e pelo endpoint da esquerda em caso de empate
	pontosVarredura.sort(key=lambda endPoint: (endPoint.ponto[0], endPoint.posicao))

	# árvore binária de busca
	arvore = No(pontosVarredura[0])

	# varre os pontos de varredura
	for endpoint in pontosVarredura:
		cima = arvore.acima(endpoint.ponto)
		baixo = arvore.abaixo(endpoint.ponto)
		
		if endpoint.posicao == esquerda:
			arvore.insere(endpoint, lambda a, b: a.ponto[1] <= b.ponto[1])

			if cima != None and \
			segmentosInterceptam(segmentos[cima.numSegmento], segmentos[endpoint.numSegmento]):
				return True
			elif baixo != None and \
			segmentosInterceptam(segmentos[baixo.numSegmento], segmentos[endpoint.numSegmento]):
				return True
			
		if endpoint.posicao == direita:
			if cima != None and baixo != None:
				if segmentosInterceptam(segmentos[cima.numSegmento], segmentos[baixo.numSegmento]):
					return True
			arvore.remove(endpoint, lambda a, b: a.ponto[1] <= b.ponto[1])
	return False

def preparaSegmentos(envoltoria1, envoltoria2):
	"""formata as envoltórias para a varredura linear"""
	segmentos1 = [(envoltoria1[i], envoltoria1[(i+1)%len(envoltoria1)]) for i in range(len(envoltoria1))]
	segmentos2 = [(envoltoria2[i], envoltoria2[(i+1)%len(envoltoria2)]) for i in range(len(envoltoria2))]

	segmentos_varredura = segmentos1 + segmentos2
	return segmentos_varredura