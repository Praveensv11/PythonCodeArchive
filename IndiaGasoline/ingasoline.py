import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

gas = pd.read_csv('gasprice.csv')

# plt.figure(figsize=(8.5))

plt.title("Gasoline price in India", fontdict={'fontweight':'bold', 'fontsize':10})

plt.plot(gas.Year, gas.PetrolPrice, '--', label="Petrol")
plt.plot(gas.Year, gas.DieselPrice, '--', label="Diesel")

plt.xticks(gas.Year[::3])

plt.xlabel('Year')
plt.ylabel('Rs')

plt.legend()

plt.savefig('Gas_price_figure', dpi=300)
plt.show()