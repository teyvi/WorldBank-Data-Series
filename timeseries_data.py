import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from pandas_datareader import wb

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
africa_map.replace("Egypt","Egypt, Arab Rep.", inplace = True)
africa_map.replace("Gambia" , "Gambia, The", inplace = True)
africa_map.replace("Swaziland","Eswatini", inplace = True)

#merging the data with africa map
merge= africa_map.join(data, on = "NAME_0" , how = 'right')
#expanding the table
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)

#creating a for loop to iterete the dates

#plot
ax = merge.plot(column = 'inflation',
                legend = True,
                scheme = 'user_defined',
                classification_kwds = { 'bins': [-5,0,5,10,15,20,25,30,35,40,45,50,55]}
                )

#adding a title to the map
ax.set_title ('Inflation in Countries at')
#removing the axis
ax.set_axis_off()

#move legend
ax.get_legend().set_bbox_to_anchor((0.18,0.6))


#data cleaning- checking data for similar entries
#for index, row in data.iterrows():
#    if index not in africa_map['NAME_0'].to_list():
#        print(index + ' is not in the list' )
#   else:
#      pass

#printing results
#print(africa_map)
#print(africa_map)
#print(data)
