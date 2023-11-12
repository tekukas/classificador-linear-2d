import functools
import matplotlib.pyplot as plt
from primitivas import orientacao, distanciaQuadrada

def desenhaEnvoltoria(envoltoria, pontos=None, show=False):
	"""
	Plota os pontos, e os segmentos da envoltória em vermelho
	:param pontos: Lista de pontos
	:param envoltoria: Lista de pontos que formam a envoltória convexa
	:param show: Se False, apenas gera o plot. Se True, gera o plot e mostra
	:return: None
	"""
	if pontos is None:
			pontos = envoltoria

	x, y = zip(*pontos)
	plt.scatter(x, y, s=5, c='black')

	# plt.xlim(0, 1.5*max(x))
	# plt.ylim(0, 1.5*max(y))

	for i in range(len(envoltoria)):
		x = (envoltoria[i][0], envoltoria[(i + 1) % len(envoltoria)][0])
		y = (envoltoria[i][1], envoltoria[(i + 1) % len(envoltoria)][1])

		# plota o segmento de linha entre o ponto atual e o próximo ponto
		plt.plot(x, y, color='red')

	if show:
		plt.show()

def envoltoriaConvexa(pontos):
	"""
	Calcula a envoltória convexa de uma lista de pontos.
	:return: Lista de pontos que formam a envoltória convexa
	"""
	# Faz com que a entrada seja uma lista se for dada uma instância de np.array
	pontos = list(pontos)

	# Se houver menos de 3 pontos, não há envoltória convexa
	if len(pontos) <= 3:
		return None

	# Encontre o ponto âncora com a menor coordenada y (e menor x se houver empate)
	ponto_ancora = min(pontos, key=lambda p: (p[1], p[0]))

	# Função dentro do escopo de envoltoriaConvexa() para acessar a variável ponto_ancora
	def comparaAngulos(p1, p2):
		"""Função auxiliar para ordenar os pontos por ângulo polar"""
		direcao = orientacao(ponto_ancora, p1, p2)
		if direcao == 0:
			if distanciaQuadrada(ponto_ancora, p2) >= distanciaQuadrada(ponto_ancora, p1):
				return -1
			else:
				return 1
		elif direcao == 2:
			return -1
		else:
			return 1

	# Ordena os pontos por ângulo polar em relação ao ponto âncora (e maior distância se houver empate)
	pontos = sorted(pontos, key=functools.cmp_to_key(comparaAngulos))

	# move o ancora para o inicio da lista (a função sortnão garante permanência de elementos empatados)
	pontos.remove(ponto_ancora)
	pontos.insert(0, ponto_ancora)

	# cria uma pilha e insere os três primeiros pontos nela
	pilha = []
	pilha.append(pontos[0])
	pilha.append(pontos[1])
	pilha.append(pontos[2])

	for i in range(3, len(pontos)):
		# continue removendo o topo enquanto o último ponto e o ponto atual fazem um ângulo horário ou são colineares
		while len(pilha) > 1 and orientacao(pilha[-2], pilha[-1], pontos[i]) != 2:
			pilha.pop()
		pilha.append(pontos[i])

	return pilha

def desenha_pontos(points_1, points_2, label_1, label_2):
    # Defina cores personalizadas para cada classe
    colors = ['red', 'green']

    # Crie um gráfico de dispersão com cores mapeadas para os pontos das duas classes
    plt.scatter(points_1[:, 0], points_1[:, 1], c=colors[0], label=label_1)
    plt.scatter(points_2[:, 0], points_2[:, 1], c=colors[1], label=label_2)

    # Adicione a legenda com os rótulos descritivos e as cores correspondentes
    plt.legend()