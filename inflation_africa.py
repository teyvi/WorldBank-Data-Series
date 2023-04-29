from pandas_datareader import wb
import geopandas
import pandas as pd
import matplotlib.pyplot as plt
data=wb.download(indicator='FP.CPI.TOTL.ZG',
                 country= ('DZ', 'AO', 'BJ', 'BW', 'BF', 'BI', 'CM', 'CV', 'CF', 'TD', 'KM', 'CD', 'CG', 'CI', 'DJ', 'EG', 'GQ', 'ER', 'ET', 'GA', 'GM', 'GH', 'GN', 'GW', 'KE', 'LS', 'LR', 'LY', 'MG', 'MW', 'ML', 'MR', 'MU', 'MA', 'MZ', 'NA', 'NE', 'NG', 'RW', 'ST', 'SN', 'SC', 'SL', 'SO', 'ZA', 'SS', 'SD', 'SZ', 'TZ', 'TG', 'TN', 'UG', 'ZM', 'ZW')
                 ,start=2000, end=2020)
data= data.reset_index(1)
data.columns = ['year','inflation']

#loading the African map
world_map = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
africa_map = world_map[world_map['continent'].str.lower() == 'africa']
africa_map=africa_map.set_index('name')
data= africa_map.join(data, how='outer')
#setting columns
pd.set_option('display.max_columns',10)
pd.set_option('display.max_rows',300)
pd.set_option('display.width',1000)
print(data)

#finding missing data
print(data.isna())
data.isna().sum().plot(kind='bar')
plt.show()