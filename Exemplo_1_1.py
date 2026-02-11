#Exemplo  1-1
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
from prepare_country_stats import prepare_country_stats

#Carregue os dados
oecd_bli = pd.read_csv("oecd_bli_2015.csv", thousands=',')

gdp_per_capita = pd.read_csv("gdp_per_capita.csv", thousands=',',delimiter='\t', encoding='latin1', na_values="n/a")

#Prepare os dados
country_stats = prepare_country_stats(oecd_bli, gdp_per_capita)
X = np.c_[country_stats["GDP per capita"]]
y = np.c_[country_stats["Life satisfaction"]]

#Visualize os dados
country_stats.plot(kind='scatter', x="GDP per capita", y='Life satisfaction')
#plt.show()

#Selecione um modelo linear
model = sklearn.linear_model.LinearRegression()

#Treine o modelo
model.fit(X,y)

#Faça uma predição para o Cyprus
X_new = [[22587]] #Cyprus' GDP per capita
print(model.predict(X_new)) # outputs [[5.96242338]]

print("Finalizou")

