import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

##Import the data 
df = pd.read_excel(r'C:\Users\Jhona\OneDrive\Área de Trabalho\PRBR11.xlsx', index_col=0)

##Create returns
returns = pd.DataFrame()
for i in df:
    returns[i] = df[i].pct_change().dropna()

weights = [0.0479, 0.3773, 0.5092, 0.657, 0.0, 0.0]
returns['PRBR11'] = returns.dot(weights)

