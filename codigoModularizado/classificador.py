from envoltoria import envoltoriaConvexa, desenhaEnvoltoria, desenha_pontos
from varreduraLinear import varreduraLinear, preparaSegmentos
from modelo import pontos_mais_proximos, calcula_ponto_medio, linha_classificadora

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

class Classificador:
    def __init__(self, classe1, classe2, label1, label2, test_size=0.2, random_state=None, rodar_automaticamente=True):
        self.classe1 = classe1
        self.classe2 = classe2
        self.label1 = label1
        self.label2 = label2
        self.centroide_classe1 = None
        self.centroide_classe2 = None
        self.treino_classe1 = None
        self.teste_classe1 = None
        self.treino_classe2 = None
        self.teste_classe2 = None
        self.reta_perpendicular = None
        self.intersecao = False

        if rodar_automaticamente:

            # Separar conjuntos de treino e teste
            self.separar_treino_teste(test_size, random_state)

            # Treinar com os conjuntos de treino
            self.treinar()

            if self.intersecao:
              print("Os dados de treinamento de", self.label1, "e", self.label2, "não são separáveis")
            else:
              # Mostra o gráfico
              self.desenha_grafico()

    def setar_treino_teste(self, treino_classe1, teste_classe1, treino_classe2, teste_classe2):
      self.treino_classe1 = treino_classe1
      self.teste_classe1 = teste_classe1
      self.treino_classe2 = treino_classe2
      self.teste_classe2 = teste_classe2

    def separar_treino_teste(self, test_size=0.3, random_state=None):
        self.treino_classe1, self.teste_classe1 = train_test_split(self.classe1, test_size=test_size, random_state=random_state)
        self.treino_classe2, self.teste_classe2 = train_test_split(self.classe2, test_size=test_size, random_state=random_state)

    def treinar(self):
        envoltoria1 = envoltoriaConvexa(self.treino_classe1)
        envoltoria2 = envoltoriaConvexa(self.treino_classe2)

        self.intersecao = varreduraLinear(preparaSegmentos(envoltoria1, envoltoria2))

        self.centroide_classe1 = np.mean(envoltoria1, axis=0)
        self.centroide_classe2 = np.mean(envoltoria2, axis=0)

        self.linha_classificadora = linha_classificadora(envoltoria1, envoltoria2)

    def classificar(self, ponto):
        if self.centroide_classe1 is None or self.centroide_classe2 is None or self.linha_classificadora is None:
            raise ValueError("Os centroides ou a linha classificadora ainda não foram calculados. Execute treinar() primeiro.")

        inclinacao_tangente, b_tangente = self.linha_classificadora

        # Calcular o valor da reta no ponto dado
        valor_da_reta = ponto[1] - (inclinacao_tangente * ponto[0] + b_tangente)

        # Comparar as alturas dos centroides
        altura_centroide_classe1 = self.centroide_classe1[1]
        altura_centroide_classe2 = self.centroide_classe2[1]

        if altura_centroide_classe1 > altura_centroide_classe2:
            return self.label1 if valor_da_reta > 0 else self.label2
        else:
            return self.label2 if valor_da_reta > 0 else self.label1

    def desenha_grafico(self):
        # Calcule as envoltórias convexas
        env1 = envoltoriaConvexa(self.treino_classe1)
        env2 = envoltoriaConvexa(self.treino_classe2)

        # Desenhe as envoltórias convexas
        desenhaEnvoltoria(env1)
        desenhaEnvoltoria(env2)

        # Desenhe os conjuntos de pontos
        desenha_pontos(self.classe1,self.classe2,self.label1, self.label2)

        if not self.intersecao:
          # Desenha a linha classificadora apenas caso os dados sejam separáveis
          original_xlim = plt.gca().get_xlim()
          original_ylim = plt.gca().get_ylim()

          pontos = pontos_mais_proximos(env1, env2)
          ponto_medio = calcula_ponto_medio(pontos[0], pontos[1])
          linha = linha_classificadora(env1, env2)

          plt.scatter(*zip(*pontos), s=50, c='black')
          plt.scatter(*ponto_medio, s=50, c='black')
          plt.plot([pontos[0][0], pontos[1][0]], [pontos[0][1], pontos[1][1]], c='red')
          plt.plot([pontos[0][0]-100, pontos[1][0]+100], [linha[0] * (pontos[0][0]-100) + linha[1], linha[0] * (pontos[1][0]+100) + linha[1]], c='black')

          plt.xlim(original_xlim)
          plt.ylim(original_ylim)

        plt.xlabel('Componente 1')
        plt.ylabel('Componente 2')
        plt.title('Iris dataset com 2 componentes')

        plt.show()

    def exibir_metricas(self):
        if self.intersecao:
          print("Não há como realizar métricas pois os dados de treinamento das classes", self.label1, "e", self.label2, "não são separáveis")
          print("")
          return

        acertos_treino = 0
        erros_treino = 0
        acertos_teste = 0
        erros_teste = 0

        if self.treino_classe1 is not None and self.treino_classe2 is not None:
            for ponto in self.treino_classe1:
                if self.classificar(ponto) == self.label1:
                    acertos_treino += 1
                else:
                    erros_treino += 1
            for ponto in self.treino_classe2:
                if self.classificar(ponto) == self.label2:
                    acertos_treino += 1
                else:
                    erros_treino += 1

        if self.teste_classe1 is not None and self.teste_classe2 is not None:
            for ponto in self.teste_classe1:
                if self.classificar(ponto) == self.label1:
                    acertos_teste += 1
                else:
                    erros_teste += 1
            for ponto in self.teste_classe2:
                if self.classificar(ponto) == self.label2:
                    acertos_teste += 1
                else:
                    erros_teste += 1

        total_acertos = acertos_treino + acertos_teste
        total_erros = erros_treino + erros_teste

        # Calcular os verdadeiros positivos, falsos positivos e falsos negativos
        verdadeiros_positivos = acertos_teste
        falsos_positivos = erros_teste  # Supondo que tudo o que foi classificado como classe 2 e era classe 1 seja um falso positivo
        falsos_negativos = erros_treino  # Supondo que tudo o que não foi classificado como classe 2 e era classe 1 seja um falso negativo

        # Calcular precisão e revocação
        precisao = verdadeiros_positivos / (verdadeiros_positivos + falsos_positivos)
        revocacao = verdadeiros_positivos / (verdadeiros_positivos + falsos_negativos)

        indice_acerto = total_acertos / (total_acertos + total_erros) * 100

        print("Para a classificação entre", self.label1, "e", self.label2, "temos que:")

        print("Se interceptam:", self.intersecao)

        print("Porcentagem de acertos (treino):", (acertos_treino / (acertos_treino + erros_treino)) * 100)
        print("Porcentagem de erros (treino):", (erros_treino / (acertos_treino + erros_treino)) * 100)
        print("Porcentagem de acertos (teste):", (acertos_teste / (acertos_teste + erros_teste)) * 100)
        print("Porcentagem de erros (teste):", (erros_teste / (acertos_teste + erros_teste)) * 100)
        print("Índice de acerto:", indice_acerto, "%")
        print("Precisão:", precisao)
        print("Revocação:", revocacao)
        print("")