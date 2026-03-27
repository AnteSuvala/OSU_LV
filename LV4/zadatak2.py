import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
import sklearn.linear_model as lm
import sklearn.metrics as sk

data = pd.read_csv('data_C02_emission.csv')
data.info()

input_var = ['Engine Size (L)', 
             'Cylinders', 
             'Fuel Type', 
             'Fuel Consumption City (L/100km)',
             'Fuel Consumption Hwy (L/100km)',
             'Fuel Consumption Comb (L/100km)',
             'Fuel Consumption Comb (mpg)',
             ]
output_var = ['CO2 Emissions (g/km)']
X = data[input_var]
y = data[output_var]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=1)

ohe = OneHotEncoder()
X_encoded_train = ohe.fit_transform(X_train[['Fuel Type']]).toarray()
X_encoded_test = ohe.fit_transform(X_test[['Fuel Type']]).toarray()

linearModel = lm.LinearRegression()
linearModel.fit(X_encoded_train, y_train)
y_test_p = linearModel.predict(X_encoded_test)

ME = sk.max_error(y_test, y_test_p)
print(f"Max Error: {ME}")

error = np.abs(y_test_p - y_test)
max_error_id = np.argmax(error)

max_error_model = data.iloc[max_error_id, 1]
print(f"Model with maximum error: {max_error_model}")