#Code to read data from Excel using pandas
import pandas as pd
df=pd.read_excel('inp.xls','Sheet1')
print(df.head(10))
print('-------------------------------------------------')
print(df.drop(columns=['Designation','Name']).head(10))
