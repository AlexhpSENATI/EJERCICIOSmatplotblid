import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.plot([0, 2], [2, 4], color = 'b')

ax.plot([2, 3], [4, 0], color = 'b')

ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_title('Ejemplo de Línea Diagonal')
ax.legend()

ax.set_xlim(0, 3)
ax.set_ylim(0, 4)

# Mostrar el gráfico
plt.show()