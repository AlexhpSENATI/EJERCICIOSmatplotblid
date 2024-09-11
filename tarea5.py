import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 21)

colors = {'linea': '#FAD02E', 'cuadrado': '#F28D35', 'triangulo': '#6D28D9'}

# Creamos la figura
plt.figure()

plt.plot(x, x-x, color=colors['linea'], linestyle='-', marker='o')           
plt.plot(x, x**2, color=colors['cuadrado'], linestyle='-', marker='s')      
plt.plot(x, x**3, color=colors['triangulo'], linestyle='-', marker='^')    

# Añadimos título y etiquetas
plt.title('Gráficos')
plt.xlabel('x')
plt.ylabel('y')

# Añadimos la leyenda y la cuadrícula
plt.legend()
plt.grid(True)

plt.show()