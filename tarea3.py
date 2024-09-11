import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

fig, ax = plt.subplots()

ax.plot([10, 20], [20, 40], color='b',)
ax.plot([20, 30], [40, 10], color='b',)

ax.plot([10, 20],[40,10], color='c')
ax.plot([20, 30],[10,30], color='c')

ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
# ax.set_title('')

ax.set_xlim(10, 30)
ax.set_ylim(10, 40)

ax.xaxis.set_major_locator(ticker.MultipleLocator(5))

plt.show()