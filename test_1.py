import pandas as pd

df = pd.read_csv("covid-vaccination-doses-per-capita.csv")
df['Date'] = pd.to_datetime(df['Day'])
df.set_index('Date', inplace=True)
df.drop(['Day'], axis=1, inplace=True)
covid_c = df.groupby(['Entity'])
total_df = covid_c.sum()
print(total_df.head())