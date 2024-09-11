import matplotlib.pyplot as plt

x = [0, 10]
y = [0, 10]

fig, ax = plt.subplots()


ax.plot(x, y, label='Línea ')

# Añadir etiquetas y título
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_title(' Línea ')
ax.legend()

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Mostrar el gráfico
plt.show()
