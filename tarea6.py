import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import matplotlib.ticker as ticker

fig, ax = plt.subplots()

start_date = datetime(2016, 10, 3)
dates = [start_date + timedelta(days=i) for i in range(5)] 

# Plots con fechas en el eje X
ax.plot([dates[0], dates[1]], [772.5, 776.5], marker='o', color='r')
ax.plot([dates[1], dates[2]], [776.5, 776.5], marker='o', color='r')
ax.plot([dates[2], dates[3]], [776.5, 777.0], marker='o', color='r')
ax.plot([dates[3], dates[4]], [777.0, 775.0], marker='o', color='r')

ax.set_ylabel('Eje Y')
ax.set_xlim(dates[0], dates[-1]) 
ax.set_ylim(772.5, 777.0)

ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))  
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  

ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))

plt.xticks(rotation=45)


ax.legend()

plt.tight_layout()


plt.show()
