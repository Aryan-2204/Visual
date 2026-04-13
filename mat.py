import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('default')
#2d plot : numericasl and categorical/both numerical or both categorical (eg:Time Series)

#simpple plotting
price=[10,20,30,40,50]
years=[2010,2011,2012,2013,2014]
plt.plot(years,price)
plt.show()


#plotting multiple plot
plt.plot(batsman['index'],batsman['v.kohli'])
plt.plot(batsman['index'],batsman['d.singh'])
plt.show()

#batsman is the dataset imported by batsman =pd.read_csv('data.csv'))

plt.plot(batsman['index'],batsman['v.kohli'])
plt.plot(batsman['index'],batsman['d.singh'])

plt.title("Batsman's performance")
plt.xlabel('season')
plt.ylabel('runs scored')
plt.show()