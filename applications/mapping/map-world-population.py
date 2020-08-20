import folium
map = folium.Map(location=[37, -122], zoom_start=10, tiles='Stamen Terrain')
fg = folium.FeatureGroup(name='My Map')
datum = open('world.json', 'r', encoding='utf-8-sig').read()


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


fg.add_child(folium.GeoJson(data=datum, style_function=lambda x: {'fillColor': popu(x['properties']['POP2005'])}))


map.add_child(fg)
map.save('Map-world.html')
