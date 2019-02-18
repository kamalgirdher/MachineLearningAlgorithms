import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datasets\indiapopulation.csv',skipinitialspace=True,usecols=['Value'])

df['MA']=df.rolling(2,win_type='triang').sum()

df['Deviation']=df['Value']-df['MA']

print(df.head(5))

plt.plot(df['MA'])