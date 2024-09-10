import pandas as pd
import matplotlib.pyplot as plt

url = 'https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv'
df = pd.read_csv(url)

columns = ["Mortality rate, infant (per 1,000 live births)","GDP per capita (constant 2010 US$)","Country Name"]
df_columns = df[columns]

df_columns.plot.scatter(x='GDP per capita (constant 2010 US$)',
                y='Mortality rate, infant (per 1,000 live births)',
                title='Infant Mortality Against GDP per Capita')

plt.show()
print("change from computerB")