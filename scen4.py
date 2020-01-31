import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

gen = pd.read_excel('Graph Data/Scenario-4-to-plot.xlsx', skiprows = 1, nrows = 15, usecols = 'C:AH')
em = pd.read_excel('Graph Data/TEP - Graphs II.xlsx', sheet_name = 'ALL PLOTS', skiprows = 381, nrows = 16, usecols = 'H:AM')

def divide_source(ds):
	energy = []
	for i in range(0,16):
		energy.append(ds.loc[i].to_numpy().reshape(-1))
	return energy

year = np.arange(2019, 2051)

'''
gen_sources = divide_source(gen)
total = np.zeros(32)
for i in range (0,14):
	total = total + gen_sources[i]
gen_sources = gen_sources/total
col = ['#414141', '#787878', '#01977a', '#2bc4a3', '#7ce7ce', '#ffd73e', '#d49b00', '#8874bd', '#96a7f3', '#c94a6a',\
		'#ff7b00', '#8ead47', '#2b46b1', '#1D731D', '#bebebe']
plt.stackplot(year, gen_sources, colors=col)
plt.legend(['Coal', 'Coal with CCS', 'Gas - CT', 'Gas - CC', 'Gas - CC with CCS', 'Solar - PV', 'Solar - CSP', 'Wind - Onshore',\
		'Wind - Offshore', 'Nuclear', 'Geothermal', 'Biomass', 'Hydroelectric', 'BECCS', 'Others'], loc='center left', bbox_to_anchor=(1, 0.5),
          fancybox=True, fontsize = 16)
plt.tick_params(labelsize = 18)
plt.tight_layout()
plt.show()'''


em_sources = divide_source(em)
no_beccs = em_sources[0:12]+em_sources[14]
beccs = em_sources[13]
total = em_sources[15]
print(beccs)
col = ['#414141', '#787878', '#01977a', '#2bc4a3', '#7ce7ce', '#ffd73e', '#d49b00', '#8874bd', '#96a7f3', '#c94a6a',\
		'#ff7b00', '#8ead47', '#2b46b1', '#bebebe']
plt.stackplot(year, no_beccs, colors=col, labels=['Coal', 'Coal with CCS', 'Gas - CT', 'Gas - CC', 'Gas - CC with CCS', 'Solar - PV', 'Solar - CSP', 'Wind - Onshore',\
		'Wind - Offshore', 'Nuclear', 'Geothermal', 'Biomass', 'Hydroelectric', 'Others'])
plt.plot(year, total, 'k--', label = 'Net', linewidth=3)
plt.stackplot(year, beccs, colors=['#1D731D'], labels=['BECCS'])
plt.axhline(y=0, xmin=0, xmax=1, color='k')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fancybox=True, fontsize = 16)
plt.tick_params(labelsize = 18)
plt.tight_layout()
plt.show()