from pandas_datareader import wb
import geopandas
import pandas as pd
import matplotlib.pyplot as plt

#downloading data for only Africa
data=wb.download(indicator='FP.CPI.TOTL.ZG',
                 country= ('DZ', 'AO', 'BJ', 'BW', 'BF', 'BI', 'CM', 'CV', 'CF', 'TD', 'KM', 'CD', 'CG', 'CI', 'DJ', 'EG', 'GQ', 'ER', 'ET', 'GA', 'GM', 'GH', 'GN', 'GW', 'KE', 'LS', 'LR', 'LY', 'MG', 'MW', 'ML', 'MR', 'MU', 'MA', 'MZ', 'NA', 'NE', 'NG', 'RW', 'ST', 'SN', 'SC', 'SL', 'SO', 'ZA', 'SS', 'SD', 'SZ', 'TZ', 'TG', 'TN', 'UG', 'ZM', 'ZW')
                 ,start=2000, end=2020)
#setting data index
data= data.reset_index(1)
data.columns = ['year','inflation']

#loading world map
world_map = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

#Removing other continents except Africa
africa_map = world_map[world_map['continent'].str.lower() == 'africa']

#Setting index for joining
africa_map=africa_map.set_index('name')
join_data= africa_map.join(data, how='outer')
pd.set_option('display.max_rows', None)
print(join_data)

#plotting the data
ax= join_data.plot(column= 'inflation',
               cmap = 'Greens',
               legend= True,
               scheme= 'user_defined',
               classification_kwds= {'bins':[10, 20, 50, 100, 500, 1000]},
               figsize= (100,10),
               )

#add title to the map
ax.set_title('Consumer Inflation in Africa',
             fontdict={'fontsize':20}, pad = 12.5)

#Removing axis
ax.set_axis_off()
plt.show()

#Moving legends
ax.get_legend().set_bbox_to_anchor(0.5,0.6)

#finding missing data
#print(data.isna())
#data.isna().sum().plot(kind='bar')
#plt.show()