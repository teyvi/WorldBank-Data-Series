import geopandas as gpd
import pandas as pd
from pandas_datareader import wb
import matplotlib.pyplot as plt
import mapclassify

from inflation_africa import ax

# downloading data for only Africa
data= wb.download(indicator='FP.CPI.TOTL.ZG',
                 country =("DZ", "AO", "BJ", "BW", "BF", "BI", "CV", "CM", "CF", "TD",
                           "KM", "CG", "CD", "CI", "DJ", "EG", "GQ", "ER", "SZ", "ET",
                           "GA", "GM", "GH", "GN", "GW", "KE", "LS", "LR", "LY", "MG",
                           "MW", "ML", "MR", "MU", "MA", "MZ", "NA", "NE", "NG", "RW",
                           "ST", "SN", "SC", "SL", "SO", "ZA", "SS", "SD", "TZ", "TG",
                           "TN", "UG", "ZM", "ZW"),
                  start=2000, end=2020)

# resetting index for merging
data = data.reset_index(1)
data.columns = ['year', 'inflation']

# Reading the world map
africa_map = gpd.read_file(r'/Users/angelateyvi/Documents/GitHub/WorldBank-Data-Series/worldmap/african_map.shp')

# replacing the data with different names
africa_map.replace("Côte d'Ivoire", "Cote d'Ivoire", inplace= True)
africa_map.replace("Democratic Republic of the Congo", "Congo, Dem. Rep.", inplace = True)
africa_map.replace("Republic of Congo", "Congo, Rep.", inplace = True)
africa_map.replace("Cape Verde", "Cabo Verde", inplace = True)
africa_map.replace("Egypt", "Egypt, Arab Rep.", inplace = True)
africa_map.replace("Gambia", "Gambia, The", inplace = True)
africa_map.replace("Swaziland", "Eswatini", inplace = True)

# merging the data with africa map
merge = africa_map.join(data, on = "NAME_0" , how = 'right')

#itereate each column of year to add to title
# expanding the table
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.expand_frame_repr', False)
print(merge.head())

# plot
merge.plot(column= 'year',
           cmap= 'Reds',
           legend = True,
           scheme = 'user_defined',
           classification_kwds = {'bins' :[-10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
                                           110, 120, 130, 140, 150, 160, 170, 180, 190, 200,
                                           210, 220, 230, 240, 250, 260, 270, 280, 290, 300,
                                           310, 320, 330, 340, 350, 360, 370, 380, 390, 400,
                                           410, 420, 430, 440, 450, 460, 470, 480, 490, 500,
                                           510, 520, 530, 540, 550, 560, 570, 580, 590, 600]
                                  }
           )

#plt.show()

# adding a title to the map
ax.set_title ('Inflation in Countries at', fontdict =
{'fontsize':20},pad = 12.5)

# removing the axis
ax.set_axis_off()

# move legend
ax.get_legend().set_bbox_to_anchor= ((0.18, 0.6))


# data cleaning- checking data for similar entries
# for index, row in data.iterrows():
#    if index not in africa_map['NAME_0'].to_list():
#        print(index + ' is not in the list' )
#   else:
#      pass

# printing results
# print(africa_map)
# print(africa_map)
# print(data)
