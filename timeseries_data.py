from pandas_datareader import wb
from prettytable import PrettyTable
import geopandas
import pandas as pd
import matplotlib.pyplot as plt

#downloading data for only Africa
data=wb.download(indicator='FP.CPI.TOTL.ZG',
                 country= ( 'DZA', 'AGO', 'BEN', 'BWA', 'BFA', 'BDI', 'CPV', 'CMR', 'CAF', 'TCD', 'COM', 'COG',
    'COD', 'DJI', 'EGY', 'GNQ', 'ERI', 'SWZ', 'ETH', 'ATF', 'GAB', 'GMB', 'GHA', 'GIN',
    'GNB', 'CIV', 'KEN', 'LSO', 'LBR', 'LBY', 'MDG', 'MWI', 'MLI', 'MRT', 'MUS', 'MYT',
    'MAR', 'MOZ', 'NAM', 'NER', 'NGA', 'REU', 'RWA', 'STP', 'SEN', 'SYC', 'SLE', 'SOM',
    'ZAF', 'SSD', 'SHN', 'SDN', 'TZA', 'TGO', 'TUN', 'UGA', 'ESH', 'ZMB', 'ZWE')
                 ,start=2000, end=2020)

#resetting index for merging
data= data.reset_index(1)
data.columns = ['year','inflation']
pd.set_option('display.max_rows', None)


#finding countries with missing values
missing_columns = data['inflation'].isnull()
missing_row = data[missing_columns]

#loading world map
world_map = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

#Removing other continents except Africa
africa_map = world_map[world_map['continent'].str.lower() == 'africa']

#replacing the data with different names
#africa_map.replace['Central African Republic','Central African Rep. ', inplace = True]
#africa_map.replace["Cote d'Ivoire","Côte d'Ivoire", inplace = True]
#africa_map.replace["Congo, Dem. Rep."," Dem. Rep. Congo", inplace = True]
#africa_map.replace["Egypt, Arab Rep.","Egypt", inplace = True]
#africa_map.replace["Gambia, The","Gambia", inplace = True]
#africa_map.replace["Equatorial Guinea","Eq. Guinea", inplace = True]
#africa_map.replace["Mauritius","Eq. Guinea", inplace = True]
#africa_map.replace["South Sudan","S. Sudan", inplace = True]
#africa_map.replace["Sao Tome and Principe","S. Sudan", inplace = True]
#africa_map.replace["Eswatini","eSwatini", inplace = True]
#africa_map.replace["Seychelles","eSwatini", inplace = True]




#expanding the table
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)

#data cleaning- checking data for similar entries
for index, row in data.iterrows():
    if index not in africa_map['name'].to_list():
        print(index + ' is not in the list of shapefile' )
    else:
        pass

#printing results
print(africa_map)
#ax = africa_map.plot(column= 'name')
#plt.show()
#print(data)
