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
year = df['YYYYMM'].to_numpy()
year = year
consumption = df['Value'].to_numpy().astype(int)

predyear = np.arange(2018, 2051)
total = pd.read_excel('retirement.xlsx', skiprows = 2, usecols = 'D').to_numpy().reshape(-1)
coal = pd.read_excel('retirement.xlsx', skiprows = 2, usecols = 'G').to_numpy().reshape(-1)
ng = pd.read_excel('retirement.xlsx', skiprows = 2, usecols = 'M').to_numpy().reshape(-1)
re = pd.read_excel('retirement.xlsx', skiprows = 2, usecols = 'P').to_numpy().reshape(-1)
nc = pd.read_excel('retirement.xlsx', skiprows = 2, usecols = 'S').to_numpy().reshape(-1)
#start = pd.read_excel('retirement.xlsx', skiprows = 2, usecols = 'Q').to_numpy().reshape(-1)
etc = total - coal - ng - re - nc

demand_year = np.arange(1951, 2051)
demand_year = np.reshape(demand_year, (-1, 1))
baseline = pd.read_csv('Baseline.csv').to_numpy()
low_demand = pd.read_csv('Low-demand.csv').to_numpy()
wma = pd.read_csv('Waxman-Markey Analysis.csv').to_numpy()

plt.plot(year, consumption)
plt.plot(predyear, total)
plt.plot(demand_year, low_demand)
#No individual plot but stackplot instead
'''
plt.plot(predyear, coal)
plt.plot(predyear, ng)
plt.plot(predyear, re)
plt.plot(predyear, nc)
'''
plt.stackplot(predyear, re, ng, nc, coal, etc)

plt.xlabel('Year')
plt.ylabel('Net Electricity Generation (TWh)')
plt.title('Estimation of Effect of Retirement')
plt.legend(['Actual Data', 'Total Supply', 'Total Demand', 'Renewable', 'Natural Gas', 'Nuclear', 'Coal', 'Others'])
plt.axvline(2018, linestyle='--')
plt.show()
