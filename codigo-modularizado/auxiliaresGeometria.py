import random
import math
import matplotlib.pyplot as plt

def geraRect(num, intervalo):
	"""Gera pontos aleatórios dentro de um retângulo"""
	pontos = []
	for _ in range(num):

		# Gera um ponto aleatório dentro do intervalo
		x = random.randint(intervalo[0], intervalo[1])
		y = random.randint(intervalo[0], intervalo[1])

		pontos.append((x,y))
	return pontos

def geraCirc(num, intervalo=(50,100)):
	"""Gera pontos aleatórios dentro de um círculo"""
	pontos = []

	# pega o menor valor do intervalo para usar como raio
	raio_maximo = min(intervalo)

	for _ in range(num):

		# Gera um ângulo aleatório entre 0 e 2*pi (360 graus)
		angulo = random.uniform(0, 2 * math.pi)

		# Gera um raio aleatório entre 0 e o raio máximo
		raio = random.uniform(0, raio_maximo)

		# Converte coordenadas polares em coordenadas cartesianas centradas no meio do intervalo
		x = raio * math.cos(angulo) + 1.5*intervalo[0]
		y = raio * math.sin(angulo) + 1.5*intervalo[0]

		pontos.append((int(x), int(y)))

	return pontos

def geraPontos(num=200, intervalo=(50,100)):
	"""Gera pontos aleatórios dentro de um retângulo ou círculo"""
	pontos = []

	aleatorio = random.randint(0,1)

	if aleatorio == 0:
		pontos = geraRect(num, intervalo)
	else:
		pontos = geraCirc(num, intervalo)

	return pontos

def plotaPontos(pontos):
	plt.scatter(*zip(*pontos), s=5, c='black')
	plt.show()

def desenha_pontos(points_1, points_2, label_1, label_2):
    # Defina cores personalizadas para cada classe
    colors = ['red', 'green']

    # Crie um gráfico de dispersão com cores mapeadas para os pontos das duas classes
    plt.scatter(points_1[:, 0], points_1[:, 1], c=colors[0], label=label_1)
    plt.scatter(points_2[:, 0], points_2[:, 1], c=colors[1], label=label_2)

    # Adicione a legenda com os rótulos descritivos e as cores correspondentes
    plt.legend()