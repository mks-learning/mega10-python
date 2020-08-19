# adding a statement here so that I can clone
import folium
map = folium.Map(location=[37.4124, -122.1111], zoom_start=20, tiles='Stamen Terrain')
fg = folium.FeatureGroup(name='My Map')

for i in [[37.4124, -122.1109], [37.4434, -122.1312], [37.8895, -122.1045]]:
    fg.add_child(folium.Marker(location=i, popup="Home", icon=folium.Icon(color="green")))

map.add_child(fg)
map.save('Map1.html')
