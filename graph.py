import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Read CSV file
df = pd.read_csv('MER_T07_01.csv')
#Choose only desired consumption type
df = df.loc[df['MSN'] == 'ELETPUS']
df['YYYYMM'] = df['YYYYMM'].apply(str)
boolean_series = df['YYYYMM'].str.lower().str.endswith('13')
df = df[boolean_series]
df['YYYYMM'] = df['YYYYMM'].str[:-2].astype(int)
year = df['YYYYMM'].as_matrix()
consumption = df['Value'].as_matrix().astype(int)
np.savetxt("actual data.csv", consumption, delimiter=",")

predyear = np.arange(1951, 2051)
predyear = np.reshape(predyear, (-1, 1))
baseline = pd.read_csv('Baseline.csv').as_matrix()
low_demand = pd.read_csv('Low-demand.csv').as_matrix()
wma = pd.read_csv('Waxman-Markey Analysis.csv').as_matrix()

plt.plot(year, consumption)
plt.plot(predyear, baseline)
plt.plot(predyear, low_demand)
plt.plot(predyear, wma)
plt.xlabel('Year')
plt.ylabel('Total Net Electricity Generation (TWh)')
plt.title('Estimation of Total Net Electricity Generation')
plt.legend(['Actual Data', 'Baseline', 'Low-demand', 'Waxman-Markey'])
plt.show()