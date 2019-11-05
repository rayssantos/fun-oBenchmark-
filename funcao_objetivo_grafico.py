x = []
y = []
for i in range(-10,10):
  y.append(funcao_objetivo(i))
  x.append(i)
  
# Importação da biblioteca MatplotLib

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
plt.title("Função Quadrática x*x - x - 2")

plt.ylabel("Valor da funcao")
plt.xlabel("Valor de x")

# Salva a figura em um arquivo
plt.savefig('grafico_de_linha')

plt.close('all')

# Exibe a imagem
Image('grafico_de_linha.png')
