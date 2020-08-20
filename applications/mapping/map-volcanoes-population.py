import folium
import pandas
import math


map = folium.Map(location=[37, -122], zoom_start=10, tiles='Stamen Terrain')
fgv = folium.FeatureGroup(name='Volcano Map')
data = pandas.read_csv('Volcanoes.csv')
fgp = folium.FeatureGroup(name='Population Map')
datum = open('world.json', 'r', encoding='utf-8-sig').read()
lat = list(data['LAT'])
lon = list(data['LON'])
name = list(data['NAME'])
loc = list(data['LOCATION'])
type = list(data['TYPE'])
elev = list(data['ELEV'])


def popu(pop):
    if pop <= 10000000:
        return 'cadetblue'
    elif pop <= 15000000:
        return 'darkblue'
    elif pop <= 25000000:
        return 'purple'
    elif pop <= 50000000:
        return 'blue'
    elif pop <= 75000000:
        return 'pink'
    elif pop <= 100000000:
        return 'black'
    elif pop <= 250000000:
        return 'green'
    elif pop <= 750000000:
        return 'orange'
    else:
        return 'red'


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


for lt, ln, nm, lc, tp, e in zip(lat, lon, name, loc, type, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], popup=str(nm + '<br>' + lc + '<br>' + tp), radius=math.ceil(e / 100), color=ucolor(tp), fill_color=ucolor(tp), opacity=(e % 10000)))


fgp.add_child(folium.GeoJson(data=datum, style_function=lambda x: {'fillColor': popu(x['properties']['POP2005'])}))


map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save('Map-pop-volc.html')
