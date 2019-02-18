#Code to read csv file using Pandasa

import pandas as pd

df=pd.read_csv('inp.csv')
               
#df=pd.read_csv('inp.csv', usecols=['Age','Name'])

#df=pd.read_csv('https://ed-public-download.app.cloud.gov/downloads/Most-Recent-Cohorts-Scorecard-Elements.csv')

#df=pd.read_csv('inp.csv',comment="#",skip_blank_lines=True)

print(df.head(15))