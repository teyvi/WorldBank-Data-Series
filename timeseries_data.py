from pandas_datareader import wb
from prettytable import PrettyTable
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

#downloading data for only Africa
data=wb.download(indicator='FP.CPI.TOTL.ZG',
                 country=("DZ", "AO", "BJ", "BW", "BF", "BI", "CV", "CM", "CF", "TD",
                          "KM", "CG", "CD", "CI", "DJ", "EG", "GQ", "ER", "SZ", "ET",
                          "GA", "GM", "GH", "GN", "GW", "KE", "LS", "LR", "LY", "MG",
                          "MW", "ML", "MR", "MU", "MA", "MZ", "NA", "NE", "NG", "RW",
                          "ST", "SN", "SC", "SL", "SO", "ZA", "SS", "SD", "TZ", "TG",
                          "TN", "UG", "ZM", "ZW")
                 ,start=2000, end=2020)

#resetting index for merging
data= data.reset_index(1)
data.columns = ['year','inflation']
pd.set_option('display.max_rows', None)

#Reading the world map
africa_map= gpd.read_file(r'/Users/angelateyvi/Documents/GitHub/WorldBank-Data-Series/worldmap/african_map.shp')

#replacing the data with different names
#africa_map.replace("Central African Rep." , "Central African Republic" , inplace = True)
africa_map.replace("Côte d'Ivoire" , "Cote d'Ivoire", inplace = True)
africa_map.replace("Democratic Republic of the Congo","Congo, Dem. Rep.", inplace = True)
africa_map.replace("Republic of Congo","Congo, Rep.", inplace = True)
africa_map.replace("Cape Verde","Cabo Verde", inplace = True)
#africa_map.replace("Egypt, Arab Rep.","Egypt", inplace = True)
#africa_map.replace("Gambia, The","Gambia", inplace = True)
#africa_map.replace("Equatorial Guinea","Eq. Guinea", inplace = True) y
#africa_map.replace("Mauritius","Eq. Guinea", inplace = True)
#africa_map.replace("South Sudan","S. Sudan", inplace = True) y
#africa_map.replace("Sao Tome and Principe","S. Sudan", inplace = True)
#africa_map.replace("Eswatini","eSwatini", inplace = True) y
#africa_map.replace["Seychelles","Djibouti", inplace = True)




#expanding the table
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)

#data cleaning- checking data for similar entries
for index, row in data.iterrows():
    if index not in africa_map['NAME_0'].to_list():
        print(index + ' is not in the list' )
    else:
        pass

#printing results
print(africa_map)
#print(africa_map)
print(data)
