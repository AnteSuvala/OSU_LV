import pandas as pd
import numpy as np

data = pd.read_csv('LV3/data_C02_emission.csv')

def a_zadatak():
    print(len(data)) # 2212 mjerenja
    print('---------------------')
    print(data.info()) # int64(3), float64(4), str(5) -> category(5)
    print('---------------------')
    data.drop_duplicates() # brisanje dupliciranih vrijednosti
    print(data.isnull().sum()) # nema izostalih vrijednosti
    print('---------------------')
    data.dropna()
    data['Make'] = data['Make'].astype('category')
    data['Model'] = data['Model'].astype('category')
    data['Vehicle Class'] = data['Vehicle Class'].astype('category')
    data['Transmission'] = data['Transmission'].astype('category')
    data['Fuel Type'] = data['Fuel Type'].astype('category')
    print(data.info())

#a_zadatak()

def b_zadatak():
    biggest_consumption = data.nlargest(3, 'Fuel Consumption City (L/100km)')
    print(biggest_consumption[['Make','Model','Fuel Consumption City (L/100km)']])
    print('---------------------')
    least_consumption = data.nsmallest(3, 'Fuel Consumption City (L/100km)')
    print(least_consumption[['Make','Model','Fuel Consumption City (L/100km)']])
    
#b_zadatak()

def c_zadatak():
    co2_data = data[(data['Engine Size (L)'] > 2.5) & (data['Engine Size (L)'] < 3.5)]
    print(f"Broj vozila veličine motora između 2.5 i 3.5L: {len(co2_data)}")
    print('---------------------')
    print(f"Prosjecna CO2 emisija: {co2_data['CO2 Emissions (g/km)'].mean()}")

#c_zadatak()

def d_zadatak():
    audis = data[(data['Make'] == "Audi")]
    print(f"Broj vozila proizvođača Audi: {len(audis)}")
    print('---------------------')
    audis = audis[(audis['Cylinders'] == 4)]
    print(f"Prosjecna CO2 emisija: {audis['CO2 Emissions (g/km)'].mean()}")

#d_zadatak()

def e_zadatak():
    even_cylinders = data[(data['Cylinders'] % 2 == 0)]
    print(f"Broj vozila sa parnim brojem cilindara: {len(even_cylinders)}")
    print('---------------------')
    even_cylinders = even_cylinders.groupby('Cylinders')
    print(even_cylinders['CO2 Emissions (g/km)'].mean())

#e_zadatak()

def f_zadatak():
    diesels = data[(data['Fuel Type'] == 'D')]
    petrols = data[(data['Fuel Type'] == 'X')]

    print(f"Dizel:\nProsjek: {diesels['Fuel Consumption City (L/100km)'].mean()} - Medijan: {diesels['Fuel Consumption City (L/100km)'].median()}")
    print(f"Regularni benzin:\nProsjek: {petrols['Fuel Consumption City (L/100km)'].mean()} - Medijan: {petrols['Fuel Consumption City (L/100km)'].median()}")

#f_zadatak()

def g_zadatak():
    cars = data[(data['Cylinders'] == 4) & (data['Fuel Type'] == "D")]
    biggestCityConsumption = cars.nlargest(1, 'Fuel Consumption City (L/100km)')
    print(biggestCityConsumption[['Make', 'Model', 'Fuel Consumption City (L/100km)']])

#g_zadatak()

def h_zadatak():
    manual_transsmission = data[(data['Transmission'].str.startswith('M'))]
    print(f"Broj vozila sa manualnim mjenjačem: {len(manual_transsmission)}")

#h_zadatak()

def i_zadatak():
    print (data.corr( numeric_only = True ))

#i_zadatak()

b_zadatak()