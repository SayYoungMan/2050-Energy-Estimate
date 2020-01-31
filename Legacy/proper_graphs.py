import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

eg1 = pd.read_excel('Graph Data/TEP - Graphs II.xlsx', sheet_name = 'ALL PLOTS', skiprows = 72, nrows = 15, usecols = 'H:AM')
em1 = pd.read_excel('Graph Data/TEP - Graphs II.xlsx', sheet_name = 'ALL PLOTS', skiprows = 92, nrows = 15, usecols = 'H:AM')
eg2 = pd.read_excel('Graph Data/TEP - Graphs II.xlsx', sheet_name = 'ALL PLOTS', skiprows = 168, nrows = 15, usecols = 'H:AM')
em2 = pd.read_excel('Graph Data/TEP - Graphs II.xlsx', sheet_name = 'ALL PLOTS', skiprows = 188, nrows = 15, usecols = 'H:AM')
eg3 = pd.read_excel('Graph Data/TEP - Graphs II.xlsx', sheet_name = 'ALL PLOTS', skiprows = 263, nrows = 15, usecols = 'H:AM')
em3 = pd.read_excel('Graph Data/TEP - Graphs II.xlsx', sheet_name = 'ALL PLOTS', skiprows = 283, nrows = 15, usecols = 'H:AM')
eg4 = pd.read_excel('Graph Data/TEP - Graphs II.xlsx', sheet_name = 'ALL PLOTS', skiprows = 359, nrows = 15, usecols = 'H:AM')
em4 = pd.read_excel('Graph Data/TEP - Graphs II.xlsx', sheet_name = 'ALL PLOTS', skiprows = 379, nrows = 15, usecols = 'H:AM')
em_total = pd.read_excel('Graph Data/TEP - Graphs II.xlsx', sheet_name = 'ALL PLOTS', skiprows = 408, nrows = 15, usecols = 'H:AM')
cap_total = pd.read_excel('Graph Data/TEP - Graphs II.xlsx', sheet_name = 'ALL PLOTS', skiprows = 416, nrows = 15, usecols = 'H:AM')

def eg_divide1(ds):
	coal = ds.loc[0].to_numpy().reshape(-1)
	coalccs = ds.loc[1].to_numpy().reshape(-1)
	gasct = ds.loc[2].to_numpy().reshape(-1)
	gascc = ds.loc[3].to_numpy().reshape(-1)
	solarpv = ds.loc[5].to_numpy().reshape(-1)
	solarcsp = ds.loc[6].to_numpy().reshape(-1)
	windon = ds.loc[7].to_numpy().reshape(-1)
	windoff = ds.loc[8].to_numpy().reshape(-1)
	nuc = ds.loc[9].to_numpy().reshape(-1)
	geo = ds.loc[10].to_numpy().reshape(-1)
	bio = ds.loc[11].to_numpy().reshape(-1)
	hydro = ds.loc[12].to_numpy().reshape(-1)
	other = ds.loc[13].to_numpy().reshape(-1)
	total = ds.loc[14].to_numpy().reshape(-1)

	return coal, coalccs, gasct, gascc, solarpv, solarcsp, windon, windoff, nuc, geo, bio, hydro, other, total

def eg_divide(ds):
	coal = ds.loc[0].to_numpy().reshape(-1)
	coalccs = ds.loc[1].to_numpy().reshape(-1)
	gasct = ds.loc[2].to_numpy().reshape(-1)
	gascc = ds.loc[3].to_numpy().reshape(-1)
	gascc_ccs = ds.loc[4].to_numpy().reshape(-1)
	solarpv = ds.loc[5].to_numpy().reshape(-1)
	solarcsp = ds.loc[6].to_numpy().reshape(-1)
	windon = ds.loc[7].to_numpy().reshape(-1)
	windoff = ds.loc[8].to_numpy().reshape(-1)
	nuc = ds.loc[9].to_numpy().reshape(-1)
	geo = ds.loc[10].to_numpy().reshape(-1)
	bio = ds.loc[11].to_numpy().reshape(-1)
	hydro = ds.loc[12].to_numpy().reshape(-1)
	other = ds.loc[13].to_numpy().reshape(-1)
	total = ds.loc[14].to_numpy().reshape(-1)

	return coal, coalccs, gasct, gascc, gascc_ccs, solarpv, solarcsp, windon, windoff, nuc, geo, bio, hydro, other, total

def total_plot(ds, col, ylabel, title):
	s1 = ds.loc[0].to_numpy().reshape(-1)
	s2 = ds.loc[1].to_numpy().reshape(-1)
	s3 = ds.loc[2].to_numpy().reshape(-1)
	s4 = ds.loc[3].to_numpy().reshape(-1)
	year = np.arange(2019, 2051)
	plt.plot(year, s1, color = col[0], linewidth = 3)
	plt.plot(year, s2, color = col[1], linewidth = 3)
	plt.plot(year, s3, color = col[2], linewidth = 3)
	plt.plot(year, s4, color = col[3], linewidth = 3)
	plt.xlabel('Year', fontsize = 14)
	plt.ylabel(ylabel, fontsize = 14)
	#plt.title(title, fontsize = 18)
	plt.legend(['Scenario 1', 'Scenario 2', 'Scenario 3', 'Scenario 4'])
	plt.show()

def eg_plot1(ds):
	coal, coalccs, gasct, gascc, solarpv, solarcsp, windon, windoff, nuc, geo, bio, hydro, other, total = eg_divide1(ds)
	coal, coalccs, gasct, gascc, solarpv, solarcsp, windon, windoff, nuc, geo, bio, hydro, other =\
		coal/total, coalccs/total, gasct/total, gascc/total, solarpv/total, solarcsp/total, windon/total,\
		windoff/total, nuc/total, geo/total, bio/total, hydro/total, other/total
	year = np.arange(2019, 2051)
	plt.stackplot(year, coal, coalccs, gasct, gascc, solarpv, solarcsp, windon, windoff, nuc, geo, bio, hydro, other,\
		colors = ['#414141', '#787878', '#01977a', '#2bc4a3', '#ffd73e', '#d49b00', '#8874bd', '#96a7f3', '#c94a6a',\
		'#ff7b00', '#8ead47', '#2b46b1', '#bebebe'])
	plt.xlabel('Year', fontsize = 18)
	plt.ylabel('Percentage of Technology (%)', fontsize = 18)
	#plt.title('Electricity Generation - Scenario 1', fontsize = 24)
	plt.legend(['Coal', 'Coal with CCS', 'Gas - CT', 'Gas - CC', 'Solar - PV', 'Solar - CSP', 'Wind - Onshore',\
		'Wind - Offshore', 'Nuclear', 'Geothermal', 'Biomass', 'Hydroelectric', 'Others'], loc='center left', bbox_to_anchor=(1, 0.5),
          fancybox=True, fontsize = 16)
	plt.tick_params(labelsize = 18)
	plt.tight_layout()
	plt.show()

def eg_plot(ds):
	coal, coalccs, gasct, gascc, gascc_ccs, solarpv, solarcsp, windon, windoff, nuc, geo, bio, hydro, other, total = eg_divide(ds)
	coal, coalccs, gasct, gascc, gascc_ccs, solarpv, solarcsp, windon, windoff, nuc, geo, bio, hydro, other =\
		coal/total, coalccs/total, gasct/total, gascc/total, gascc_ccs/total, solarpv/total, solarcsp/total, windon/total,\
		windoff/total, nuc/total, geo/total, bio/total, hydro/total, other/total
	year = np.arange(2019, 2051)
	plt.stackplot(year, coal, coalccs, gasct, gascc, gascc_ccs, solarpv, solarcsp, windon, windoff, nuc, geo, bio, hydro, other,\
		colors = ['#414141', '#787878', '#01977a', '#2bc4a3', '#7ce7ce', '#ffd73e', '#d49b00', '#8874bd', '#96a7f3', '#c94a6a',\
		'#ff7b00', '#8ead47', '#2b46b1', '#bebebe'])
	plt.xlabel('Year', fontsize = 18)
	plt.ylabel('Percentage of Technology (%)', fontsize = 18)
	#plt.title(title, fontsize = 24)
	plt.legend(['Coal', 'Coal with CCS', 'Gas - CT', 'Gas - CC', 'Gas - CC with CCS', 'Solar - PV', 'Solar - CSP', 'Wind - Onshore',\
		'Wind - Offshore', 'Nuclear', 'Geothermal', 'Biomass', 'Hydroelectric', 'Others'], loc='center left', bbox_to_anchor=(1, 0.5),
          fancybox=True, fontsize = 16)
	plt.tick_params(labelsize = 18)
	plt.tight_layout()
	plt.show()

def em_plot1(ds, hist):
	coal, coalccs, gasct, gascc, solarpv, solarcsp, windon, windoff, nuc, geo, bio, hydro, other, total = eg_divide1(ds)
	year = np.arange(2019, 2051)
	prvyear = np.arange(2005, 2020)
	prvemit = np.array([2416, 2358, 2425, 2373, 2158, 2270, 2170, 2034, 2050, 2050, 1913, 1821, 1743, 1764, total[0]])
	plt.stackplot(year, coal, coalccs, gasct, gascc, solarpv, solarcsp, windon, windoff, nuc, geo, bio, hydro, other,\
		colors = ['#414141', '#787878', '#01977a', '#2bc4a3', '#ffd73e', '#d49b00', '#8874bd', '#96a7f3', '#c94a6a',\
		'#ff7b00', '#8ead47', '#2b46b1', '#bebebe'])
	plt.xlabel('Year', fontsize = 18)
	plt.ylabel(r'Total Annual Emissions (MMt $CO_2e)$', fontsize = 18)
	#plt.title('Total Emissions - Scenario 1', fontsize = 24)
	plt.tick_params(labelsize = 18)
	if hist==True:
		plt.plot(prvyear, prvemit)
		plt.legend(['Actual Data', 'Coal', 'Coal with CCS', 'Gas - CT', 'Gas - CC', 'Solar - PV', 'Solar - CSP', 'Wind - Onshore',\
		'Wind - Offshore', 'Nuclear', 'Geothermal', 'Biomass', 'Hydroelectric', 'Others'], loc='center left', bbox_to_anchor=(1, 0.5),
          fancybox=True, fontsize = 16)
		plt.axvline(2019, linestyle='--')
	else:
		plt.legend(['Coal', 'Coal with CCS', 'Gas - CT', 'Gas - CC', 'Solar - PV', 'Solar - CSP', 'Wind - Onshore',\
		'Wind - Offshore', 'Nuclear', 'Geothermal', 'Biomass', 'Hydroelectric', 'Others'], loc='center left', bbox_to_anchor=(1, 0.5),
          fancybox=True, fontsize = 16)
	plt.tight_layout()
	plt.show()

def em_plot(ds, hist):
	coal, coalccs, gasct, gascc, gascc_ccs, solarpv, solarcsp, windon, windoff, nuc, geo, bio, hydro, other, total = eg_divide(ds)
	year = np.arange(2019, 2051)
	prvyear = np.arange(2005, 2020)
	prvemit = np.array([2416, 2358, 2425, 2373, 2158, 2270, 2170, 2034, 2050, 2050, 1913, 1821, 1743, 1764, total[0]])
	plt.stackplot(year, coal, coalccs, gasct, gascc, gascc_ccs, solarpv, solarcsp, windon, windoff, nuc, geo, bio, hydro, other,\
		colors = ['#414141', '#787878', '#01977a', '#2bc4a3', '#7ce7ce', '#ffd73e', '#d49b00', '#8874bd', '#96a7f3', '#c94a6a',\
		'#ff7b00', '#8ead47', '#2b46b1', '#bebebe'])
	plt.xlabel('Year', fontsize = 18)
	plt.ylabel(r'Total Annual Emissions (MMt $CO_2e)$', fontsize = 18)
	#plt.title(title, fontsize = 24)
	plt.tick_params(labelsize = 18)
	if hist==True:
		plt.plot(prvyear, prvemit)
		plt.legend(['Actual Data', 'Coal', 'Coal with CCS', 'Gas - CT', 'Gas - CC', 'Gas - CC with CCS', 'Solar - PV', 'Solar - CSP', 'Wind - Onshore',\
		'Wind - Offshore', 'Nuclear', 'Geothermal', 'Biomass', 'Hydroelectric', 'Others'], loc='center left', bbox_to_anchor=(1, 0.5),
          fancybox=True, fontsize = 16)
		plt.axvline(2019, linestyle='--')
	else:
		plt.legend(['Coal', 'Coal with CCS', 'Gas - CT', 'Gas - CC', 'Gas - CC with CCS', 'Solar - PV', 'Solar - CSP', 'Wind - Onshore',\
		'Wind - Offshore', 'Nuclear', 'Geothermal', 'Biomass', 'Hydroelectric', 'Others'], loc='center left', bbox_to_anchor=(1, 0.5),
          fancybox=True, fontsize = 16)
	plt.tight_layout()
	plt.show()


eg_plot1(eg1)
eg_plot(eg2)
eg_plot(eg3)


em_plot1(em1, hist = False)
em_plot(em2,  hist = False)
em_plot(em3,  hist = False)

total_plot(em_total, ['#c1d4b7', '#99b880', '#769e4f','#5d8541'], r'Total Annual Emissions (MMt $CO_2e)$', 'Comparison of Emissions')
total_plot(cap_total, ['#f8d18e', '#f6c042', '#daaa3a','#ba902f'], 'Cumulative Capital Investment (Billion USD)', 'Comparison of CapEx')