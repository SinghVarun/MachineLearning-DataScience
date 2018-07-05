#What is the relationship between the GDP per capita and life expectancy in Venezuela?

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib.gridspec as gridspec
import pylab
import matplotlib.ticker as ticker

#Abriendo los XLS
GDP_df = pd.read_excel('GDPPCapita.xls', skiprows = 3)
life_df = pd.read_excel('lifeExpectancy.xls', skiprows=3)

#Especificando las columnas que quiero para GDP
years = [x for x in GDP_df.columns[4:]]
columns_to_keep = ['Country Name']+years
GDP_df = GDP_df[columns_to_keep]

#Especificando el pais con el que trabajare para GDP
GDP_venezuela = GDP_df[GDP_df['Country Name'] == 'Venezuela, RB']
GDP_venezuela = GDP_venezuela.set_index('Country Name')

#Especificando los paises con los que lo comparare
south_america = ['Colombia', 'Ecuador', 'Brazil', 'Peru', 'Argentina', 'Uruguay', 'Chile', 'Bolivia', 'Paraguay']
GDP_samerica = GDP_df[(GDP_df['Country Name'] == 'Colombia') | (GDP_df['Country Name'] == 'Ecuador') | (GDP_df['Country Name'] == 'Brazil') | (GDP_df['Country Name'] == 'Peru') | (GDP_df['Country Name'] == 'Argentina') | (GDP_df['Country Name'] == 'Uruguay') | (GDP_df['Country Name'] == 'Chile') | (GDP_df['Country Name'] == 'Bolivia') | (GDP_df['Country Name'] == 'Bolivia')]
GDP_samerica = GDP_samerica.set_index('Country Name')
GDP_samerica = GDP_samerica.agg(np.mean, axis = 0)

#transformandolo serie para poder plottearlo. Ya que uno plotea es la columna
GDP_venezuela = GDP_venezuela.iloc[0]
GDP_venezuela = pd.to_numeric(GDP_venezuela, errors = 'coerce')

#Especificando las columnas que quiero para life_df
life_df = life_df[columns_to_keep]

#Especificamos el país con el que trabajare para life_df
life_venezuela = life_df[life_df['Country Name'] == 'Venezuela, RB']
life_venezuela = life_venezuela.set_index('Country Name')

#Especificando los paises con los que lo comparare
life_samerica = life_df[(life_df['Country Name'] == 'Colombia') | (life_df['Country Name'] == 'Ecuador') | (life_df['Country Name'] == 'Brazil') | (life_df['Country Name'] == 'Peru') | (life_df['Country Name'] == 'Argentina') | (life_df['Country Name'] == 'Uruguay') | (life_df['Country Name'] == 'Chile') | (life_df['Country Name'] == 'Bolivia') | (life_df['Country Name'] == 'Bolivia')]
life_samerica = life_samerica.set_index('Country Name')
life_samerica = life_samerica.agg(np.mean, axis = 0)

#transformandolo serie para poder plotearlo
life_venezuela = life_df.iloc[0]
life_venezuela = pd.to_numeric(life_venezuela, errors = 'coerce') #para transformar de objeto a float y graficar


#-----------------------------------------------------------------------------------------------------#
#Creamos la figura
fig = plt.figure()
gspec = gridspec.GridSpec(12, 10)
top_left = plt.subplot(gspec[0:3,0:5])
top_right = plt.subplot(gspec[0:3, 5:10])
bot_left = plt.subplot(gspec[4:7, 0:5])
bot_right = plt.subplot(gspec[4:7, 5:10])
bottom = plt.subplot(gspec[8:12, 0:10])

#boxplot GDP
top_left.boxplot([GDP_venezuela.dropna(), GDP_samerica.dropna()], whis = 'range', labels = ['Venezuela', 'South America'])
top_left.text(0.88, 17000, 'GDP Per Capita Global Historical Comparison (1960-2013)', weight = 'black')
top_left.set_ylabel('Billions US$')

#boxplot life
top_right.boxplot([life_venezuela.dropna(), life_samerica.dropna()], whis = 'range', labels = ['Venezuela', 'South America'])
top_right.text(0.93, 77.5, 'Life Expectancy Global Historical Comparison (1960-2013)', weight = 'black')
#pasamos los yticks a la derecha
top_right.tick_params(labelright = True, right = True, labelleft = False, left = False) #labelright para que salga el label y el right es para que salgan los ticks
#Cambiamos el numero de ticks y sus labels
position_list = np.arange(55, 80, 10)
age_list = ['55', '65', '75']
top_right.yaxis.set_major_locator(ticker.FixedLocator(position_list))
top_right.yaxis.set_major_formatter(ticker.FixedFormatter(age_list))
#Colocamos label name
top_right.set_ylabel('Years-old')
top_right.yaxis.set_label_position('right')

#line plot
bot_left.plot(GDP_venezuela, 'red', GDP_samerica, 'blue')
#Cambiamos el numero de ticks a mostrar (ya que se sobreponian)
pos_list = np.arange(0, 60, 10)
year_list = ['1960', '1970', '1980', '1990', '2000', '2010']
bot_left.xaxis.set_major_locator(ticker.FixedLocator(pos_list)) #numero de ticks que apareceran
bot_left.xaxis.set_major_formatter(ticker.FixedFormatter(year_list)) #el nombre de cada tick
#titulo
bot_left.text(1980, 17000, 'GDP Per Capita (1960-2013)', weight = 'black')
bot_left.legend(['Venezuela', 'South America'], loc = 2, frameon = False) #frameon para borrar el recuadro
bot_left.set_ylabel('Billions US$')


#lineplot
bot_right.plot(life_venezuela, 'red', life_samerica, 'blue')
bot_right.legend(['Venezuela', 'South America'], loc = 4, frameon = False)
#Pasamos los yticks a la derecha
bot_right.tick_params(labelright = True, right = True, labelleft = False, left = False)
#Cambiamos el numero de xticks labels a mostrar (ya que se sobreponian)
bot_right.xaxis.set_major_locator(ticker.FixedLocator(pos_list))
bot_right.xaxis.set_major_formatter(ticker.FixedFormatter(year_list))
#Cambiamos el numero de yticks labels a mostrar
bot_right.yaxis.set_major_locator(ticker.FixedLocator(position_list))
bot_right.yaxis.set_major_formatter(ticker.FixedFormatter(age_list))
#titulo
bot_right.text(1976, 77.5, 'Life Expectancy at Birth (1960-2013)', weight = 'black')
bot_right.set_ylabel('Years-old')
bot_right.yaxis.set_label_position('right')
#fill_between
bot_right.fill_between(range(len(life_samerica)), life_venezuela[1:], life_samerica, color = 'grey', alpha=0.1)


#scatterplot Piensa que colocar aca
bottom.scatter(GDP_venezuela, life_venezuela[1:], marker = ".", alpha = 0.5)
idx = np.isfinite(GDP_venezuela) & np.isfinite(life_venezuela) #polyfit necesita que se eliminen los NaN
#linear fit
model = pylab.polyfit(GDP_venezuela[idx], life_venezuela[1:][idx], deg = 1)
yVals = pylab.polyval(model, GDP_venezuela[idx])
#bottom.plot(GDP_venezuela[idx], yVals, 'k')
#logaritmic fit
modellog = pylab.polyfit(np.log(GDP_venezuela[idx]), life_venezuela[1:][idx], deg = 1)
yVals = pylab.polyval(modellog, np.log(GDP_venezuela[idx]))
bottom.plot(GDP_venezuela[idx], yVals, 'k', linewidth = 1)
bottom.text(5250, 78, 'Relationship between GDP Per Capita and Life expectancy in Venezuela', weight = 'black')
bottom.set_xlabel('GDP Per Capita (Billions US$)')
bottom.set_ylabel('Life Expectancy (Years)')
bottom.text(13500, 67, '$y$' + '$=$' + '$3.084*log(x)$' + '$+$' + '$47.306$', bbox=dict(facecolor='grey', alpha=0.15))