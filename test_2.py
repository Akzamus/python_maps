import folium
import webbrowser

marker_map = folium.Map(
    location=[45.372, -121.6972],
    zoom_start=12,
    tiles="Stamen Terrain"
)

folium.Marker(
    location=[45.3288, -121.6625],
    popup="Mt. Hood Meadows",
    icon=folium.Icon(icon="cloud")
).add_to(marker_map)

folium.Marker(
    location=[45.3311, -121.7113],
    popup="Timberline Lodge",
    icon=folium.Icon(color="green")
).add_to(marker_map)

folium.CircleMarker(
    location=[45.3800, -121.6000],
    radius=100,
    popup="circle",
    color="#3186cc",
    fill=True,
    fill_color="#3186cc"
).add_to(marker_map)

marker_map.save("index.html")
webbrowser.open("index.html")