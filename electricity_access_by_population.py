import pandas as pd
from pandas_datareader import wb
import geopandas
import matplotlib.pyplot as plt

data = wb.download(country='all', indicator='EG.ELC.ACCS.ZS', start=2000, end= 2020)
data = data.reset_index(1)
data.columns = ['Year', 'Electricity Access']

df = pd.read_csv(data)
missing_data = df.isna()
print(missing_data)

map = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
map = map[map['name']!= 'Antarctica']
map = map.set_index('name')

index_change = {
     'United States of America': 'United States',
    'Yemen': 'Yemen, Rep.',
    'Venezuela': 'Venezuela, RB',
    'Syria': 'Syrian Arab Republic',
    'Solomon Is.': 'Solomon Islands',
    'Russia': 'Russian Federation',
    'Iran': 'Iran, Islamic Rep.',
    'Gambia': 'Gambia, The',
    'Kyrgyzstan': 'Kyrgyz Republic',
    'Mauritania': 'Mauritius',
    'Egypt': 'Egypt, Arab Rep.'
}
map = map.rename(index = index_change)
data = map.join(data, how = 'outer')

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
print(data)

data.plot('Electricity Access')
plt.show()


