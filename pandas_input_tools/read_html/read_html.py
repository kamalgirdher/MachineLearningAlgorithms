#Code to Read table from Web Page

import pandas as pd
df=pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html',usecols=['Bank Name','City'])
print(df)