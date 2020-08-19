# import pandas
# import math
import folium
from colour import Color
map = folium.Map(location=[37.4124, -122.1111], zoom_start=10, tiles='Stamen Terrain')
fg = folium.FeatureGroup(name='My Map')
data = open('world.json', 'r', encoding='utf-8-sig').read()
lat = list(data['LAT'])
lon = list(data['LON'])
name = list(data['NAME'])
loc = list(data['LOCATION'])
type = list(data['TYPE'])
elev = list(data['ELEV'])
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


# for lt, ln, nm, lc, tp, e in zip(lat, lon, name, loc, type, elev):
#
#     fg.add_child(folium.CircleMarker(location=[lt, ln], popup=str(nm + '<br>' + lc + '<br>' + tp), radius=math.ceil(e / 100), color=ucolor(tp), fill_color=ucolor(tp), opacity=(e % 10000)))

fg.add_child(folium.GeoJson(data=data, style_function=lambda x: {'fillColor': 'purple'}))

map.add_child(fg)
map.save('Map-world.html')
