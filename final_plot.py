import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

eg1 = pd.read_excel('Graph Data/TEP - Graphs II.xlsx', sheet_name = 'ALL PLOTS', skiprows = 72, nrows = 14, usecols = 'H:AM')
em1 = pd.read_excel('Graph Data/TEP - Graphs II.xlsx', sheet_name = 'ALL PLOTS', skiprows = 91, nrows = 13, usecols = 'H:AM')
eg2 = pd.read_excel('Graph Data/TEP - Graphs II.xlsx', sheet_name = 'ALL PLOTS', skiprows = 166, nrows = 15, usecols = 'H:AM')
em2 = pd.read_excel('Graph Data/TEP - Graphs II.xlsx', sheet_name = 'ALL PLOTS', skiprows = 186, nrows = 14, usecols = 'H:AM')
eg3 = pd.read_excel('Graph Data/TEP - Graphs II.xlsx', sheet_name = 'ALL PLOTS', skiprows = 261, nrows = 15, usecols = 'H:AM')
em3 = pd.read_excel('Graph Data/TEP - Graphs II.xlsx', sheet_name = 'ALL PLOTS', skiprows = 281, nrows = 14, usecols = 'H:AM')
eg4 = pd.read_excel('Graph Data/TEP - Graphs II.xlsx', sheet_name = 'ALL PLOTS', skiprows = 360, nrows = 16, usecols = 'H:AM')
em4 = pd.read_excel('Graph Data/TEP - Graphs II.xlsx', sheet_name = 'ALL PLOTS', skiprows = 381, nrows = 15, usecols = 'H:AM')
em_total = pd.read_excel('Graph Data/TEP - Graphs II.xlsx', sheet_name = 'ALL PLOTS', skiprows = 411, nrows = 4, usecols = 'H:AM')
cap_total = pd.read_excel('Graph Data/TEP - Graphs II.xlsx', sheet_name = 'ALL PLOTS', skiprows = 419, nrows = 4, usecols = 'H:AM')

year = np.arange(2019, 2051)

def divide(ds,no):
	divided = []
	for i in range(0,no):
		divided.append(ds.loc[i].to_numpy().reshape(-1))
	return divided

def eg_plot(ds,no):
	sources = divide(ds,no)
	total = sources[-1]
	sources.pop()
	sources = sources/total
	if no==14:
		col = ['#414141', '#787878', '#01977a', '#2bc4a3', '#ffd73e', '#d49b00', '#8874bd', '#96a7f3', '#c94a6a',\
			'#ff7b00', '#8ead47', '#2b46b1', '#bebebe']
		label = ['Coal', 'Coal with CCS', 'Gas - CT', 'Gas - CC', 'Solar - PV', 'Solar - CSP', 'Wind - Onshore',\
		'Wind - Offshore', 'Nuclear', 'Geothermal', 'Biomass', 'Hydroelectric', 'Others']
	if no==15:
		col = ['#414141', '#787878', '#01977a', '#2bc4a3', '#7ce7ce', '#ffd73e', '#d49b00', '#8874bd', '#96a7f3', '#c94a6a',\
		'#ff7b00', '#8ead47', '#2b46b1', '#bebebe']
		label = ['Coal', 'Coal with CCS', 'Gas - CT', 'Gas - CC', 'Gas - CC with CCS', 'Solar - PV', 'Solar - CSP', 'Wind - Onshore',\
		'Wind - Offshore', 'Nuclear', 'Geothermal', 'Biomass', 'Hydroelectric', 'Others']
	if no==16:
		col = ['#414141', '#787878', '#01977a', '#2bc4a3', '#7ce7ce', '#ffd73e', '#d49b00', '#8874bd', '#96a7f3', '#c94a6a',\
		'#ff7b00', '#8ead47', '#2b46b1', '#1D731D', '#bebebe']
		label = ['Coal', 'Coal with CCS', 'Gas - CT', 'Gas - CC', 'Gas - CC with CCS', 'Solar - PV', 'Solar - CSP', 'Wind - Onshore',\
		'Wind - Offshore', 'Nuclear', 'Geothermal', 'Biomass', 'Hydroelectric', 'BECCS', 'Others']
	plt.stackplot(year, sources, colors=col, labels=label)
	plt.xlabel('Year', fontsize = 18)
	plt.ylabel('Percentage of Technology (%)', fontsize = 18)
	plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fancybox=True, fontsize = 16)
	plt.tick_params(labelsize = 18)
	plt.tight_layout()
	plt.show()

def em_plot(ds, no):
	sources = divide(ds,no)
	if no==13:
		col = ['#414141', '#787878', '#01977a', '#2bc4a3', '#ffd73e', '#d49b00', '#8874bd', '#96a7f3', '#c94a6a',\
			'#ff7b00', '#8ead47', '#2b46b1', '#bebebe']
		label = ['Coal', 'Coal with CCS', 'Gas - CT', 'Gas - CC', 'Solar - PV', 'Solar - CSP', 'Wind - Onshore',\
		'Wind - Offshore', 'Nuclear', 'Geothermal', 'Biomass', 'Hydroelectric', 'Others']
	if no==14:
		col = ['#414141', '#787878', '#01977a', '#2bc4a3', '#7ce7ce', '#ffd73e', '#d49b00', '#8874bd', '#96a7f3', '#c94a6a',\
		'#ff7b00', '#8ead47', '#2b46b1', '#bebebe']
		label = ['Coal', 'Coal with CCS', 'Gas - CT', 'Gas - CC', 'Gas - CC with CCS', 'Solar - PV', 'Solar - CSP', 'Wind - Onshore',\
		'Wind - Offshore', 'Nuclear', 'Geothermal', 'Biomass', 'Hydroelectric', 'Others']
	plt.stackplot(year, sources, colors=col, labels=label)
	plt.xlabel('Year', fontsize = 18)
	plt.ylabel(r'Total Annual Emissions (MMt $CO_2e)$', fontsize = 18)
	plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fancybox=True, fontsize = 16)
	plt.tick_params(labelsize = 18)
	plt.tight_layout()
	plt.show()

def comparison_plot(ds, col, ylabel):
	scen = divide(ds,4)
	for i in range (0,4):
		plt.plot(year, scen[i], color = col[i], linewidth = 3)
	plt.xlabel('Year', fontsize = 14)
	plt.ylabel(ylabel, fontsize = 14)
	if col == ['#c1d4b7', '#99b880', '#769e4f','#5d8541']:
		plt.axhline(y=0, xmin=0, xmax=1, color='k', linestyle='--')
	plt.legend(['Scenario 1', 'Scenario 2', 'Scenario 3', 'Scenario 4'])
	plt.show()

#Generation Graphs
#eg_plot(eg1, 14)
#eg_plot(eg2, 15)
#eg_plot(eg3, 15)
#eg_plot(eg4, 16)

#Emission Graphs
em_plot(em1, 13)
em_plot(em2, 14)
em_plot(em3, 14)

#Comparison Graphs
#comparison_plot(em_total, ['#c1d4b7', '#99b880', '#769e4f','#5d8541'], r'Total Annual Emissions (MMt $CO_2e)$')
#comparison_plot(cap_total, ['#f8d18e', '#f6c042', '#daaa3a','#ba902f'], 'Cumulative Capital Investment (Billion USD)')