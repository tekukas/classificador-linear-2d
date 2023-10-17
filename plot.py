import random
import math

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

		pontos.append((x, y))

	return pontos

def gera_pontos(num=200, intervalo=(50,100)):
	"""Gera pontos aleatórios dentro de um retângulo ou círculo"""
	pontos = []

	aleatorio = random.randint(0,1)

	if aleatorio == 0:
		pontos = geraRect(num, intervalo)
	else:
		pontos = geraCirc(num, intervalo)

	return pontos