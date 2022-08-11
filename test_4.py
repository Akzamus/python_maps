import webbrowser
import folium
import json
import pandas as pd

df = pd.read_csv("covid-vaccination-doses-per-capita.csv")
df['Date'] = pd.to_datetime(df['Day'])
df.set_index('Date', inplace=True)
df.drop(['Day'], axis=1, inplace=True)
total_df = df.groupby(['Entity']).sum()

center = [35.762887375145795, 84.08313219586536]
m = folium.Map(location=center,
               zoom_start=2,
               max_bounds=True,
               min_zoom=1,
               min_lat=-84, max_lat=84,
               min_lon=-175, max_lon=187
               )
geo_path = "World_Countries__Generalized_.geojson"

json_data = json.load(open(geo_path), encoding='utf-8')

folium.Choropleth(geo_data=json_data,
                  data=total_df,
                  columns=(total_df.index, 'total_vaccinations_per_hundred'),
                  key_on='properties.COUNTRY',
                  fill_color='RdYlGn',
                  fill_opacity=0.7,
                  line_opacity=0.5
                  ).add_to(m)

folium.LayerControl().add_to(m)
m.save("index.html")
webbrowser.open("index.html")
