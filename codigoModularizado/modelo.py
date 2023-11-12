import numpy as np

def pontos_mais_proximos(envoltoria1, envoltoria2):
  """Encontra os pontos mais próximos entre dois polígonos convexos."""

  distancia_minima = np.inf
  pontos_mais_proximos = None

  for i in range(len(envoltoria1)):
    for j in range(len(envoltoria2)):
      distancia = np.linalg.norm(np.array(envoltoria1[i]) - np.array(envoltoria2[j]))
      if distancia < distancia_minima:
        distancia_minima = distancia
        pontos_mais_proximos = (envoltoria1[i], envoltoria2[j])

  return pontos_mais_proximos

def calcula_ponto_medio(ponto1, ponto2):
  """Calcula o ponto médio entre dois pontos"""
  return ((ponto1[0] + ponto2[0]) / 2, (ponto1[1] + ponto2[1] ) / 2)

def linha_classificadora(envoltoria1, envoltoria2):
  """Calcula um modelo classificador entre duas envoltórias.
  Retorna: Equação da reta (inclinacao, b) que separa as envoltórias
  """
  # O caso em que os pontos sejam iguais não é tratado aqui

  ponto1, ponto2 = pontos_mais_proximos(envoltoria1, envoltoria2)

  dx = ponto2[0] - ponto1[0]
  dy = ponto2[1] - ponto1[1]

  ponto_medio = calcula_ponto_medio(ponto1, ponto2)

  if dx == 0:
    # A reta é vertical, então a tangente é horizontal
    inclinacao = 0
    b = ponto_medio[0]  # O valor de 'b' é a coordenada x do ponto médio
  else:
    inclinacao = dy / dx
    # calcula a inclinação e equação da reta tangente que passa sobre o ponto medio
  if inclinacao == 0:
    inclinacao += 0.0001
  inclinacao_tangente = -1 / inclinacao
  b_tangente = ponto_medio[1] - inclinacao_tangente * ponto_medio[0]

  return (inclinacao_tangente, b_tangente)