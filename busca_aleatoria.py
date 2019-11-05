import random


# Quantidade de tentativas de gerar uma nova solução
iteracoes = 100

# listas com os dados para gerar o gráfico
func_objetivo = []
tentativas = []
valor_x = []

# contador de tentativas
i = 1

# Gera a solução inicial aleatoriamente respeitando os limites 
x = random.uniform(- 10.5, 10.5)

# calcula a qualidade da solucao
fo = funcao_objetivo(x)

# salva os dados para geração do gráfico
func_objetivo.append(fo)
valor_x.append(x)
tentativas.append(0)


# enquanto houver tentativas
while i < iteracoes:
  
  # geracao de uma nova solucao aleatoriamente, respeitando os limites
  temp = random.uniform(- 10.5, 10.5)
  
  # Calcula a qualidade da solução gerada
  temp_fo = funcao_objetivo(temp)
  
  # se a nova solucao for melhor, atualiza
  if( temp_fo < fo ):
    fo = temp_fo
    x = temp
  
  
  # salva os dados para geração do gráfico
  func_objetivo.append(fo)
  tentativas.append(i)
  valor_x.append(x)
  
  # contabiliza a tentativa
  i = i + 1

#############################################
## Geracao do gráfico  
#############################################
# Importação da biblioteca MatplotLib

y = func_objetivo
x = tentativas

# Biblioteca matplotlib
import matplotlib
matplotlib.use('Agg')
# Gera os gráficos
import matplotlib.pyplot as plt

# Utilizado para cálculos
import numpy as np

# Utilizado para exibir as imagens
from IPython.display import Image

# Dados que serão utilizados


# Gera o gráfico de linhas
plt.plot(x, y )

# Coloca o título
plt.title("Desempenho da busca aleatoria")

plt.ylabel("Valor da funcao objetivo")
plt.xlabel("Iteracoes")

# Salva a figura em um arquivo
plt.savefig('grafico_de_linha')

plt.close('all')

# Exibe a imagem
Image('grafico_de_linha.png')
