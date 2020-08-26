import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

##Import the data 
df = pd.read_excel(r'C:\Users\Jhona\OneDrive\Área de Trabalho\PRBR11.xlsx', index_col=0, parse_dates=['Data'])

##Create returns
returns = pd.DataFrame()
for i in df:
    returns[i] = df[i].pct_change().dropna()

weights = [0.0479, 0.3773, 0.5092, 0.657, 0.0, 0.0]
returns['PRBR11'] = returns.dot(weights)

cumulative_returns = pd.DataFrame()
for i in returns:
    cumulative_returns[i] = ((1+returns[i]).cumprod()-1)*100

##Ploting data
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(cumulative_returns.index, cumulative_returns)
ax.set_xlabel('Data')
ax.set_ylabel('Retornos')
plt.legend(['CPLE6', 'SAPR11', 'KLBN11', 'RAIL3', 'POSI3', 'BTTL3', 'PRBR11'])
plt.show()

##Ploting correlation
correl = returns.corr()
sns.heatmap(correl, annot=True, cbar=False, cmap='RdBu_r')
plt.yticks(rotation=0)
plt.xticks(rotation=90)
plt.show()

#Rolling correlation
roll_corrl = pd.DataFrame()
for i in returns:
    roll_corrl[i] = returns[i].rolling(60).corr(returns['PRBR11'])

plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(roll_corrl.index, roll_corrl)
ax.set_xlabel('Data')
ax.set_ylabel('Correlação')
plt.legend(['CPLE6', 'SAPR11', 'KLBN11', 'RAIL3', 'POSI3', 'BTTL3', 'PRBR11'])
plt.show()

def vol (x):
    vol = np.std(returns[x])*252**0.5
    return vol*100

vol('PRBR11')