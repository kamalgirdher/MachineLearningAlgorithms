#Code to read json & write to CSV
import pandas as pd
pd.read_json('inp.json').drop(columns=['Designation','Insured','Name']).to_excel('op.xls')
