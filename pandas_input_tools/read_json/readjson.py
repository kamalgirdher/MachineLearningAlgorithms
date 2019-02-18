#Code to read json dataset using pandas
import pandas as pd
df=pd.read_json('inp.json',orient='table')
print(df)

print('----------------------------------------------------')
#Code to print If value is NA
print(df.isna())

print('----------------------------------------------------')
#Code to drop columns and print only (no update on df)
print(df.drop(columns=['Gender','Age']))

print('----------------------------------------------------')
#Code to remove NA and only print (no update on df)
print(df.dropna(axis='rows'))
print('----------------------------------------------------')
print(df.dropna(axis='columns'))

print('----------------------------------------------------')
#Code to fill NA values
print(df.fillna(method='ffill'))

print('----------------------------------------------------')
#Code to remove NA and update df
print(df.dropna(inplace=True))
