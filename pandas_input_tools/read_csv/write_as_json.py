#Code to read from csv and write to json
import pandas as pd
pd.read_csv('inp.csv',usecols=['Name','Age']).to_json('op.json')