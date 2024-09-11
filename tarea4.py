import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

fig, ax = plt.subplots()

# ax.plot([10, 20], [20, 40], color='b', label='Linea 1')
# ax.plot([20, 30], [40, 10], color='b', label='Linea 1')

ax.plot([1, 4],[2,6], marker='o', color='b', linestyle='--')
ax.plot([5, 4],[3,6], marker='o', color='b', linestyle='--')

ax.plot([5, 6],[3,6], marker='o', color='b', linestyle='--')
ax.plot([6, 7],[6,3], marker='o', color='b', linestyle='--')


ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
# ax.set_title('Ejemplo de Líneas Diagonales')

ax.set_xlim(1, 8)
ax.set_ylim(1, 8)

ax.xaxis.set_major_locator(ticker.MultipleLocator(1))

ax.legend()

plt.show()