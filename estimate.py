import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from TFANN import ANNR

def data_preprep(data):
	data = np.reshape(data, (-1, 1))
	mean, std, data = normalise(data)
	return mean, std, data

def normalise(data):
	mean = np.mean(data)
	std = np.std(data)
	data = (data-mean)/std
	return mean, std, data

#Read CSV file
df = pd.read_csv('MER_T01_01.csv')
#Choose only desired consumption type
df = df.loc[df['MSN'] == 'TETCBUS']
df['YYYYMM'] = df['YYYYMM'].apply(str)
boolean_series = df['YYYYMM'].str.lower().str.endswith('13')
df = df[boolean_series]
df['YYYYMM'] = df['YYYYMM'].str[:-2].astype(int)
year = df['YYYYMM'].as_matrix()
year_mean, year_std, year_scaled = data_preprep(year)
consumption = df['Value'].as_matrix()
consumption_mean, consumption_std, consumption_scaled = data_preprep(consumption)
predyear = np.arange(1950, 2051)
predyear = np.reshape(predyear, (-1, 1))
predyear_scaled = (predyear-year_mean)/year_std
print('Finished Reading Data')

#Number of neurons in the input, output, and hidden layers
input = 1
output = 1
hidden = 50
#array of layers, 3 hidden and 1 output, along with the tanh activation function 
layers = [('F', hidden), ('AF', 'tanh'), ('F', hidden), ('AF', 'tanh'), ('F', hidden), ('AF', 'tanh'),('F', hidden), ('AF', 'tanh'), ('F', output)]
#construct the model and dictate params
mlpr1 = ANNR([input], layers, batchSize = 64, maxIter = 25000, tol = 0.025, reg = 1e-4, verbose = True)
mlpr2 = ANNR([input], layers, batchSize = 64, maxIter = 25000, tol = 0.022, reg = 1e-4, verbose = True)
mlpr3 = ANNR([input], layers, batchSize = 64, maxIter = 25000, tol = 0.02, reg = 1e-4, verbose = True)
print('Finished Building the Model')

#number of years for the hold-out period used to access progress
holdYears = 5
totalYears = len(year_scaled)
#fit the model to the data "Learning"
mlpr1.fit(year_scaled[0:(totalYears-holdYears)], consumption_scaled[0:(totalYears-holdYears)])
mlpr2.fit(year_scaled[0:(totalYears-holdYears)], consumption_scaled[0:(totalYears-holdYears)])
mlpr3.fit(year_scaled[0:(totalYears-holdYears)], consumption_scaled[0:(totalYears-holdYears)])
#Predict the stock price using the model
predict1 = mlpr1.predict(predyear_scaled)
predict2 = mlpr2.predict(predyear_scaled)
predict3 = mlpr3.predict(predyear_scaled)

predict1 = (predict1*consumption_std)+consumption_mean
predict2 = (predict2*consumption_std)+consumption_mean
predict3 = (predict3*consumption_std)+consumption_mean

#Display the predicted reuslts against the actual data
plt.plot(year, consumption)
plt.plot(predyear, predict1)
plt.plot(predyear, predict2)
plt.plot(predyear, predict3)
plt.xlabel('Year')
plt.ylabel('Total Primary Energy Consumption (Quadrillion Btu)')
plt.title('Estimation of Total Primary Energy Consumption')
plt.show()
plt.savefig('result.png')