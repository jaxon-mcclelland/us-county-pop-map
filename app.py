import folium
import os 
import pandas as pd

# county pop data: https://data.census.gov/cedsci/table?q=population&t=Populations%20and%20People&g=0100000US.050000&y=2019&tid=ACSDT5Y2019.B01003&hidePreview=false

usCounties = os.path.join('data', 'counties.json')
pop = os.path.join('data', 'county_pop.csv')
pops = pd.read_csv(pop,encoding = "ISO-8859-1")

#map = folium.Map(location=[38.0498, -84.4585], zoom_start=5, tiles='openstreetmap')
map = folium.Map(location=[38.0498, -84.4585], zoom_start=5)
folium.Choropleth (
    geo_data = usCounties,
    name = 'US State Populations',
    data = pops,
    columns = ['id', 'Estimate!!Total'],
    key_on = 'properties.AFFGEOID',
    fill_color = 'YlOrRd',
    fill_opacity = 0.8,
    line_opacity = 1,
    threshold_scale = [0, 50000, 80000, 300000, 500000, 1000000, 15000000],
    line_color = 'black'
).add_to(map)

map.save('index.html')
