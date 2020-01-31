import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dcf = pd.read_excel('Graph Data/Discount-rate.xlsx', skiprows = 2, nrows = 5, usecols = 'C:AH')
ct = pd.read_excel('Graph Data/Sensitivity-analysis.xlsx', skiprows = 1, nrows = 15, usecols = 'C:AH')
pl = pd.read_excel('Graph Data/Proportion-Limit.xlsx', skiprows = 1, nrows = 5, usecols = 'C:AH')
miten = pd.read_excel('Graph Data/TEP - Graphs II.xlsx', sheet_name = 'CapEx Sensitivity', skiprows = 5, nrows = 13, usecols = 'C:AH')
plten = pd.read_excel('Graph Data/TEP - Graphs II.xlsx', sheet_name = 'CapEx Sensitivity', skiprows = 23, nrows = 13, usecols = 'C:AH')
ct_2050 = pd.read_excel('Graph Data/Sensitivity-analysis.xlsx', skiprows = 1, nrows = 11, usecols = 'AH').to_numpy().reshape(-1)

def divide_five(ds):
	first = ds.loc[0].to_numpy().reshape(-1)
	second = ds.loc[1].to_numpy().reshape(-1)
	third = ds.loc[2].to_numpy().reshape(-1)
	fourth = ds.loc[3].to_numpy().reshape(-1)
	fifth = ds.loc[4].to_numpy().reshape(-1)
	return first, second, third, fourth, fifth

def divide_fifteen(ds):
	first = ds.loc[0].to_numpy().reshape(-1)
	second = ds.loc[1].to_numpy().reshape(-1)
	third = ds.loc[2].to_numpy().reshape(-1)
	fourth = ds.loc[3].to_numpy().reshape(-1)
	fifth = ds.loc[4].to_numpy().reshape(-1)
	sixth = ds.loc[5].to_numpy().reshape(-1)
	seventh = ds.loc[6].to_numpy().reshape(-1)
	eighth = ds.loc[7].to_numpy().reshape(-1)
	nineth = ds.loc[8].to_numpy().reshape(-1)
	tenth = ds.loc[9].to_numpy().reshape(-1)
	eleventh = ds.loc[10].to_numpy().reshape(-1)
	twelveth = ds.loc[11].to_numpy().reshape(-1)
	thirteenth = ds.loc[12].to_numpy().reshape(-1)
	fourteenth = ds.loc[13].to_numpy().reshape(-1)
	fifteenth = ds.loc[14].to_numpy().reshape(-1)

	return first, second, third, fourth, fifth, sixth, seventh, eighth, nineth, tenth, eleventh, twelveth, thirteenth, fourteenth, fifteenth


def divide_source(ds):
	energy = []
	for i in range(0,13):
		energy.append(ds.loc[i].to_numpy().reshape(-1))
	return energy

def capex_plot(ds1, ds2):
	sources1 = divide_source(ds1)
	sources2 = divide_source(ds2)
	year = np.arange(2019, 2051)
	col = ['#414141', '#787878', '#01977a', '#2bc4a3', '#7ce7ce', '#ffd73e', '#d49b00', '#8874bd', '#96a7f3', '#c94a6a',\
		'#ff7b00', '#8ead47', '#2b46b1', '#bebebe']
	for i in [4, 5, 7, 12]:
		plt.plot(year, sources1[i], color = col[i], linewidth = 2)
	for i in [4, 5, 7, 12]:
		plt.plot(year, sources2[i], color = col[i], linewidth = 2)

	plt.xlabel('Year', fontsize = 14)
	plt.ylabel('Cumulative Capital Investment (Billion USD)', fontsize = 14)
	plt.legend(['Gas - CC with CCS', 'Solar - PV', 'Wind - Onshore', 'Hydroelectric'], loc='upper left')
	plt.tick_params(labelsize = 18)
	plt.tight_layout()
	plt.show()



threep, fivep, sevenp, ninep, elevenp = divide_five(dcf)
year = np.arange(2019, 2051)
col = plt.cm.jet(np.linspace(0,1,5))
plt.plot(year, threep, color = col[0], linewidth = 1)
plt.plot(year, fivep, color = col[1], linewidth = 1)
plt.plot(year, sevenp, color = col[2], linewidth = 1)
plt.plot(year, ninep, color = col[3], linewidth = 1)
plt.plot(year, elevenp, color = col[4], linewidth = 1)
plt.xlabel('Year', fontsize = 14)
plt.ylabel(r'Total Annual Emissions (MMt $CO_2e)$', fontsize = 14)
plt.legend(['-4%', '-2%', '0%', '2%', '4%'])
plt.show()

'''
a, b, c, d, e,f,g,h,i,j,k,l,m,n,o = divide_fifteen(ct)
year = np.arange(2019, 2051)
col = plt.cm.jet(np.linspace(0,1,10))
plt.plot(year, a, color = col[0], linewidth = 1)
plt.plot(year, b, color = col[1], linewidth = 1)
plt.plot(year, c, color = col[2], linewidth = 1)
plt.plot(year, d, color = col[3], linewidth = 1)
plt.plot(year, e, color = col[4], linewidth = 1)
plt.plot(year, f, color = col[5], linewidth = 1)
plt.plot(year, g, color = col[6], linewidth = 1)
plt.plot(year, h, color = col[7], linewidth = 1)
plt.plot(year, i, color = col[8], linewidth = 1)
plt.plot(year, j, color = col[9], linewidth = 1)
plt.plot(year, k, color = col[10], linewidth = 1)
plt.xlabel('Year', fontsize = 14)
plt.ylabel(r'Total Emissions at 2050 (MMt $CO_2e)$', fontsize = 14)
plt.legend(['$0/tCOe', '$15/tCOe', '$20/tCOe', '$25/tCOe', '$30/tCOe', '$50/tCOe', '$70/tCOe', '$90/tCOe', '$110/tCOe', '$130/tCOe', '$150/tCOe'])
plt.show()'''


a,b,c,d,e = divide_five(pl)
year = np.arange(2019, 2051)
col = plt.cm.jet(np.linspace(0,1,5))
plt.plot(year, a, linewidth = 2)	
plt.plot(year, b, linewidth = 2)
plt.plot(year, c, linewidth = 2)
plt.plot(year, d, linewidth = 2)
plt.plot(year, e, linewidth = 2)
plt.xlabel('Year', fontsize = 14)
plt.ylabel(r'Total Annual Emissions (MMt $CO_2e)$', fontsize = 14)
plt.legend(['10%', '30%', '50%', '70%', '90%'])
plt.show()

#capex_plot(miten, plten)


cp = np.array([0, 15, 20, 25, 30, 50, 70, 90, 110, 130, 150]).reshape(-1)
plt.plot(cp, ct_2050, linewidth = 3)
plt.xlabel(r'Carbon Tax ($\$/tCO_2e$)', fontsize = 14)
plt.ylabel(r'Total Emissions at 2050 (MMt $CO_2e)$', fontsize = 14)
plt.show()