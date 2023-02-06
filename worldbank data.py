from pandas_datareader import wb
import geopandas
import pandas as pd
import matplotlib.pyplot as plt
map = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
map = map[map['name'] != 'Antarctica']
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
map = map.rename(index=index_change)
data = wb.download(indicator='FP.CPI.TOTL.ZG', country='all', start=2019, end=2019)
data = data.reset_index(1)
data.columns = ['year', 'inflation']
map = map.join(data, how='outer')
map.plot('inflation', cmap='OrRd', scheme='quantiles', missing_kwds={"color": "lightgrey"}, legend=True, figsize=(14,5))
print(data)
plt.title("Inflation 2019")
plt.show()