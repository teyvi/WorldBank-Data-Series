from pandas_datareader import wb
import geopandas
import pandas as pd
import matplotlib.pyplot as plt

# download the inflation data
data = wb.download(indicator='FP.CPI.TOTL.ZG',
                   country=('DZ', 'AO', 'BJ', 'BW', 'BF', 'BI', 'CM', 'CV', 'CF', 'TD', 'KM', 'CD', 'CG', 'CI', 'DJ', 'EG', 'GQ', 'ER', 'ET', 'GA', 'GM', 'GH', 'GN', 'GW', 'KE', 'LS', 'LR', 'LY', 'MG', 'MW', 'ML', 'MR', 'MU', 'MA', 'MZ', 'NA', 'NE', 'NG', 'RW', 'ST', 'SN', 'SC', 'SL', 'SO', 'ZA', 'SS', 'SD', 'SZ', 'TZ', 'TG', 'TN', 'UG', 'ZM', 'ZW'),
                   start=2000, end=2020)
data = data.reset_index()
data.columns = ['country', 'year', 'inflation']

world_map = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
africa_map = world_map[world_map['continent'].str.lower() == 'africa']
#africa_map=africa_map.set_index('name')
#join_data= africa_map.join(data, how='outer')
#pd.set_option('display.max_rows', None)

# pivot the data to create a table with countries as rows and years as columns
pivot_data = pd.pivot_table(data, values='inflation', index='country', columns='year')

# plot a line chart for each country
fig, ax = plt.subplots(figsize=(10, 8))
for country in pivot_data.index:
    ax.plot(pivot_data.columns, pivot_data.loc[country], label=country)
ax.legend()
ax.set_xlabel('Year')
ax.set_ylabel('Inflation (%)')
plt.show()
