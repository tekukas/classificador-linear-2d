# Classificador Linear 2D com Geometria Computacional
O trabalho sugerido foi a criação de um classificador linear que, ao ser alimentado com dados de treinamento com rótulos de duas categorias distintas, pode criar uma separação linear desses conjuntos (caso ela exista) e, em seguida, classificar novos dados sem rótulos.

## Etapas do projeto
O projeto foi dividido nas seguintes etapas:
1. Implementar um algoritmo de envoltória convexa de Graham;
1. Implementar o algoritmo de varredura linear para detecção de interseções em conjuntos de segmentos;
1. Implementar o método para verificação de separabilidade linear (encontrar interseções entre as duas envoltórias);
1. Implementar o método para construir o modelo, caso os dados sejam linearmente separáveis;
1. Implementar o classificador que recebe um conjunto de amostras desconhecidas e atribui rótulos a elas;
1. Implementar o método para computar as métricas de classificação para os 
experimentos;
1. Realizar os experimentos.

## Resultados
O projeto foi concluído e testado, com métricas de precisão, revocação e f1-score. No arquivo [ClassificadorLinear](ClassificadorLinear.ipynb) temos os testes e resultados, assim como o código detalhado. Na pasta [codigoModularizado](codigoModularizado/) está o mesmo código, porém em script Python para aplicação. 

## Grupo responsável pelo desenvolvimento do projeto:

| [<img src="https://avatars.githubusercontent.com/u/64935978?v=4" width=115><br><sub>Juan Braga</sub>](https://github.com/juanmbraga) |  [<img src="https://imgur.com/35uY87m.jpg" width=115><br><sub>Lucas Almeida</sub>](https://github.com/tekukas) |  [<img src="https://avatars.githubusercontent.com/u/48190640?v=4" width=115><br><sub>Luiz Romanhol</sub>](https://github.com/LuizRomanhol) |
| :---: | :---: | :---: