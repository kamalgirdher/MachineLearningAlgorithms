#Code to read csv file using Pandasa

import pandas as pd
df=pd.read_csv('https://ed-public-download.app.cloud.gov/downloads/Most-Recent-Cohorts-Scorecard-Elements.csv')
print(df.head(5))