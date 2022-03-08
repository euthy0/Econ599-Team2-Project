import pandas as pd
import numpy as np
import csv
from IPython.display import display


US_CPI = pd.read_csv('US_CPI.csv')

# stack years and months
US_CPI = pd.melt(US_CPI, id_vars=['YEAR'], var_name=['Month'])
US_CPI['date'] = pd.to_datetime(US_CPI['YEAR'].astype(str) + '-' + US_CPI['Month'].astype(str))
US_CPI = US_CPI.sort_values(by=['date']).drop(columns=['Month', 'YEAR']).reset_index(drop=['index'])
US_CPI = US_CPI.rename(columns={'value': 'US_CPI'})


indices = pd.read_csv('599_data.csv')

# merge US CPI data and Indices return data into one dataframe
data = pd.concat([US_CPI, indices], axis=1)

# drop column
data = data.drop('Date', 1)

# isolate inflation periods
data = data[data.US_CPI > 0.035]
data.dropna()

for i in data:
    print(i)
# pd.set_option('display.max_rows',700)
data.to_csv('data_w_cpi.csv', index=False)
