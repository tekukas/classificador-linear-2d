from classificador import Classificador

from sklearn.datasets import load_iris, load_wine
from sklearn.decomposition import TruncatedSVD
import pandas as pd

# Dataset 1: Iris
iris = load_iris()
svd = TruncatedSVD(n_components=2)
iris_2d = svd.fit_transform(iris.data)
setosa_points = iris_2d[iris.target == 0]
versicolor_points = iris_2d[iris.target == 1]
virginica_points = iris_2d[iris.target == 2]

# Dataset 2: Wine
wine = load_wine()
svd = TruncatedSVD(n_components=2)
wine_2d = svd.fit_transform(wine.data)
wine_classe0 = wine_2d[wine.target == 0]
wine_classe1 = wine_2d[wine.target == 1]
wine_classe2 = wine_2d[wine.target == 2]

# Dataset 3: Page Blocks
url = 'https://github.com/juanmbraga/linear-classifier-with-computational-geometry/raw/main/databases/page-blocks-database.csv'
p_blocks = pd.read_csv(url)

svd = TruncatedSVD(n_components=2)
p_blocks_2d = svd.fit_transform(p_blocks[p_blocks.columns[:-1]])

# testes:
# teste 1:
teste1 = Classificador(setosa_points,versicolor_points,"setosa","versicolor")
teste1.exibir_metricas()

# teste 2:
teste2 = Classificador(virginica_points,versicolor_points,"virginica","versicolor")
teste2.exibir_metricas()

# teste 3:
teste3 = Classificador(setosa_points,virginica_points,"setosa","virginica")
teste3.exibir_metricas()

# teste 4:
teste4 = Classificador(wine_classe0, wine_classe1, "wine_0", "wine_1")
teste4.exibir_metricas()

# teste 5:
teste5 = Classificador(wine_classe0, wine_classe2, "wine_0", "wine_2")
teste5.exibir_metricas()

# teste 6:
teste6 = Classificador(wine_classe1, wine_classe2, "wine_1", "wine_2")
teste6.exibir_metricas()

# teste 7:
wine = load_wine()

wine_data = wine.data

wine_data = wine_data[:, [2,4,5,6,10]]

svd = TruncatedSVD(n_components=2)
wine_teste = svd.fit_transform(wine_data)

wine_teste_0 = wine_teste[wine.target == 0]
wine_teste_1 = wine_teste[wine.target == 1]
wine_teste_2 = wine_teste[wine.target == 2]

teste7 = Classificador(wine_teste_0, wine_teste_1, "wine_teste_0", "wine_teste_2")
teste7.exibir_metricas()

# teste 8:
teste8 = Classificador(wine_teste_0, wine_teste_1, "wine_teste_0", "wine_teste_1")
teste8.exibir_metricas()

# teste 9:
teste9 = Classificador(wine_teste_1, wine_teste_2, "wine_teste_1", "wine_teste_2")
teste9.exibir_metricas()

# teste 10:
teste10 = Classificador(wine_teste_1, wine_classe0, "wine_teste_1", "wine_classe0")
teste10.exibir_metricas()

# teste 11:
teste11 = Classificador(p_blocks_2d[p_blocks["Class"]==1], p_blocks_2d[p_blocks["Class"]==2], "classe1", "classe2")
teste11.exibir_metricas()