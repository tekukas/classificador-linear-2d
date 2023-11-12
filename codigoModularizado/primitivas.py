import numpy as np

def orientacao(p, q, r):
	"""Retorna a orientação do caminho P-Q-R
	:params p, q, r: pontos
	:return: 0 = colinear, 1 = sentido horário, 2 = sentido anti-horário
	"""
	val = (q[1] - p[1]) * (r[0] - q[0]) - \
		  (q[0] - p[0]) * (r[1] - q[1])

	if val == 0:
		return 0
	elif val > 0:
		return 1
	else:
		return 2

def distanciaQuadrada(ancora, ponto):
	"""Retorna o quadrado da distância entre o ponto âncora e o ponto dado"""
	dist_ancora_ponto = (ponto[0] - ancora[0])**2 + (ponto[1] - ancora[1])**2
	return dist_ancora_ponto

def estaNoSegmento(segment, point):
	"""Retorna True se o ponto está no segmento de linha"""
	if (point[0] <= max(segment[0][0], segment[1][0]) and \
		point[0] >= min(segment[0][0], segment[1][0]) and \
		point[1] <= max(segment[0][1], segment[1][1]) and \
		point[1] >= min(segment[0][1], segment[1][1])):
		return True
	return False

def segmentosInterceptam(seg1, seg2):
	"""Retorna True se os segmentos se interceptam"""

	# não considera interseção se os segmentos compartilham um vértice
	if np.array([seg1[0] == seg2[0], seg1[0] == seg2[1], seg1[1] == seg2[0], seg1[1] == seg2[1]]).any():
		return False

	d1 = orientacao(seg2[0], seg2[1], seg1[0])
	d2 = orientacao(seg2[0], seg2[1], seg1[1])
	d3 = orientacao(seg1[0], seg1[1], seg2[0])
	d4 = orientacao(seg1[0], seg1[1], seg2[1])

	if (d1==1 and d2==2) or (d1==2 and d2==1) and \
	   (d3==1 and d4==2) or (d3==2 and d4==1):
		return True
	elif (d1==0 and estaNoSegmento(seg2, seg1[0])) or \
		 (d2==0 and estaNoSegmento(seg2, seg1[1])) or \
		 (d3==0 and estaNoSegmento(seg1, seg2[0])) or \
		 (d4==0 and estaNoSegmento(seg1, seg2[1])):
		return True
	return False