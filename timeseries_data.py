from pandas_datareader import wb
import geopandas
import pandas as pd
import matplotlib.pyplot as plt

#downloading data for only Africa
data=wb.download(indicator='FP.CPI.TOTL.ZG',
                 country= ('DZ', 'AO', 'BJ', 'BW', 'BF', 'BI', 'CM', 'CV', 'CF', 'TD', 'KM', 'CD', 'CG', 'CI', 'DJ', 'EG', 'GQ', 'ER', 'ET', 'GA', 'GM', 'GH', 'GN', 'GW', 'KE', 'LS', 'LR', 'LY', 'MG', 'MW', 'ML', 'MR', 'MU', 'MA', 'MZ', 'NA', 'NE', 'NG', 'RW', 'ST', 'SN', 'SC', 'SL', 'SO', 'ZA', 'SS', 'SD', 'SZ', 'TZ', 'TG', 'TN', 'UG', 'ZM', 'ZW')
                 ,start=2000, end=2020)

#resetting index for merging
data= data.reset_index(1)
data.columns = ['year','inflation']
pd.set_option('display.max_rows', None)


#finding countries with missing values
missing_columns = data['inflation'].isnull()
missing_row = data[missing_columns]
plt.show()
print(missing_row)
