import pandas
import folium
from colour import Color
map = folium.Map(location=[37.4124, -122.1111], zoom_start=20, tiles='Stamen Terrain')
fg = folium.FeatureGroup(name='My Map')
data = pandas.read_csv('Volcanoes.csv')
lat = list(data['LAT'])
lon = list(data['LON'])
name = list(data['NAME'])
loc = list(data['LOCATION'])
type = list(data['TYPE'])
w = Color('white')


def ucolor(type):
    if type == 'Caldera':
        return 'cadetblue'
    elif type == 'Cinder cone':
        return 'darkblue'
    elif type == 'Complex volcano':
        return 'purple'
    elif type == 'Fissue vents':
        return 'blue'
    elif type == 'Shield volcano':
        return 'pink'
    elif type == 'Maar':
        return 'black'
    elif type == 'Stratovolcano':
        return 'green'
    elif type == 'Volcanic field':
        return 'orange'
    else:
        return 'red'


for lt, ln, nm, lc, tp in zip(lat, lon, name, loc, type):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(nm + '<br>' + lc + '<br>' + tp), icon=folium.Icon(color=ucolor(tp))))

map.add_child(fg)
map.save('Map-Vol.html')
