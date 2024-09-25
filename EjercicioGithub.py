import numpy as np
import matplotlib.pyplot as plt

# 1. Cree un vector de size = 720 con valores aleatorios
vector = np.random.rand(720)

# 2. Hacer reshape de (120,6)
matriz = vector.reshape(120, 6)

# 3. Haga la transpuesta de la matriz y cree dos copias, una usando order F y otra usando order C.
matriz_transpuesta = matriz.T
copia_f = matriz_transpuesta.copy(order='F')
copia_c = matriz_transpuesta.copy(order='C')

# 4. Genere un subplot con 6 paneles, usando la versión a mano y con proporciones diferentes.
plt.figure(figsize=(12, 8))

# Gráfico de línea
plt.subplot(2, 3, 1) 
plt.plot(matriz_transpuesta[0], label='Línea')
plt.title('Gráfico de línea')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.legend(fontsize='small')

# Gráfico de dispersión
plt.subplot(2, 3, 2) 
plt.scatter(np.arange(len(matriz_transpuesta[1])), matriz_transpuesta[1], label='Datos de Dispersión')
plt.title('Gráfico de dispersión')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.legend(fontsize='small')

# Gráfico de pastel
plt.subplot(2, 3, 3) 
# Limitar el número de partes a mostrar
n_partes = 6
plt.pie(matriz_transpuesta[2][:n_partes], labels=[f'Parte {i+1}' for i in range(n_partes)])
plt.title('Gráfico de pastel')

# Gráfico de barras
plt.subplot(2, 3, 4)  
plt.bar(np.arange(len(matriz_transpuesta[3])), matriz_transpuesta[3], label='Datos de Barras')
plt.title('Gráfico de barras')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.legend(fontsize='small')

# Histograma
plt.subplot(2, 3, 5)  
plt.hist(matriz_transpuesta[4], label='Valores Histograma')
plt.title('Histograma')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.legend(fontsize='small')

# Diagrama de caja
plt.subplot(2, 3, 6)  
plt.boxplot(matriz_transpuesta[5])
plt.title('Diagrama de caja')
plt.ylabel('Valor')
plt.xlabel('Datos de Caja')  

plt.tight_layout()  
plt.show()