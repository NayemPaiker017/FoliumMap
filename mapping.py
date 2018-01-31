import folium
import pandas

data = pandas.read_csv('Volcanoes_USA.txt')
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_produce(color):
    if color < 1000:
        return 'green'
    elif 1000 <= color < 3000:
        return 'orange'
    else:
        return 'red'
