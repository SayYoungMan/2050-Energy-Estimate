import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

co2 = pd.read_excel('Graph Data/CO2-comparison-final.xlsx', skiprows = 3, nrows = 4, usecols = 'D:AI')

def divide(ds):
	scen = []
	for i in range(0,4):
		scen.append(ds.loc[i].to_numpy().reshape(-1))
	return scen

scen = divide(co2)
year = np.arange(2019, 2051)
col = ['#c1d4b7', '#99b880', '#769e4f','#5d8541']
for i in range (0,4):
	plt.plot(year, scen[i], color = col[i], linewidth = 3)
plt.xlabel('Year', fontsize = 14)
plt.ylabel(r'Total Annual Emissions (MMt $CO_2e)$', fontsize = 14)
plt.legend(['Scenario 1', 'Scenario 2', 'Scenario 3', 'Scenario 4'])
plt.show()