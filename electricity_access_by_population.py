import pandas as pd
from pandas_datareader import wb
import geopandas
import matplotlib.pyplot as plt

electric_access = wb.download(country='all', indicator='EG.ELC.ACCS.ZS', start=2000, end= 2020)
electric_access = electric_access.reset_index(1)
electric_access.columns = ['Year', 'Electricity Access']
print(electric_access)

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 1000)
print(world)

