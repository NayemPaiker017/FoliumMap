import folium
import pandas

#get the volcano data from text file
data = pandas.read_csv('Volcanoes_USA.txt')
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

#function for color on the map(based on the density)
def color_produce(color):
    if color < 1000:
        return 'green'
    elif 1000 <= color < 3000:
        return 'orange'
    else:
        return 'red'

#setting up the folium map
map = folium.Map(location=[38.58, -99.09], tiles = "Mapbox Bright", zoom_start=6)

# setting up "Volcano" feature group
volcanoes = folium.FeatureGroup("Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    volcanoes.add_child(folium.CircleMarker(location=[lt, ln], radius=5, popup=str(el) + " m",
    color = color_produce(el), fill=True, fill_opacity=0.7))

# setting up "Population" feature group
population = folium.FeatureGroup("Population")
population.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

# add all feature groups in map
map.add_child(volcanoes)
map.add_child(population)
map.add_child(folium.LayerControl())
map.save("Map.html")
