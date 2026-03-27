import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import sklearn.linear_model as lm
import sklearn.metrics as sk

data = pd.read_csv('data_C02_emission.csv')
data.info()

input_var = ['Engine Size (L)', 
             'Cylinders', 
             'Fuel Consumption City (L/100km)', 
             'Fuel Consumption Hwy (L/100km)', 
             'Fuel Consumption Comb (L/100km)', 
             'Fuel Consumption Comb (mpg)']
output = ['CO2 Emissions (g/km)']
X = data[input_var]
y = data[output]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state =1 )

for i in range(len(input_var)):
    plt.figure()

    plt.scatter(X_train[input_var[i]], y_train, c ='Blue', label='Training data')
    plt.scatter(X_test[input_var[i]], y_test, c='Red', label='Testing data')

    plt.xlabel(input_var[i])
    plt.ylabel(output[0])
    plt.legend()
    plt.show()

scaler = MinMaxScaler()
X_train_n = scaler.fit_transform( X_train )
X_test_n = scaler.transform( X_test )

for i in range(len(input_var)):
    plt.figure()
    plt.subplot(1,2,1)
    plt.hist(X_train[input_var[i]], bins = 30, color = 'Blue')
    plt.title("Prije Standardizacije")

    plt.subplot(1,2,2)
    plt.hist(X_train_n[:,i], bins = 30, color = 'Red')
    plt.title("Poslije Standardizacije")

    plt.show()

linearModel = lm.LinearRegression ()
linearModel.fit( X_train_n , y_train )

print(f"Parametri modela: {linearModel.coef_}")

y_test_p = linearModel.predict ( X_test_n )
plt.scatter(y_test, y_test_p, alpha = 0.5)
plt.title("Odnos između stvarnih vrijednosti \n izlazne veličine i procjene dobivene modelom")
plt.xlabel("Stvarne vrijednosti")
plt.ylabel("Procjenjene vrijednosti")
plt.show()

MAE = sk.mean_absolute_error( y_test , y_test_p )
MSE = sk.mean_squared_error( y_test , y_test_p )
RMSE = sk.root_mean_squared_error( y_test , y_test_p )
MAPE = sk.mean_absolute_percentage_error( y_test , y_test_p )
R_squared = sk.r2_score( y_test , y_test_p )

print(f"MAE: {MAE}")
print(f"MSE: {MSE}")
print(f"RMSE: {RMSE}")
print(f"MAPE: {MAPE}")
print(f"R2: {R_squared}")