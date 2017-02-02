import folium
import pandas

# create pandas dataframe
volcano_df = pandas.read_csv("Volcanoes-USA.txt")

# create the base map
map = folium.Map(location=[45.372, -121.679],
                 zoom_start=4,
                 tiles='Stamen Terrain')

# iterate through the data frame and create markers based on the lat/long
for lat, lon, name, elev in zip(volcano_df["LAT"],
                                volcano_df["LON"],
                                volcano_df["NAME"],
                                volcano_df["ELEV"]):
    # map markers
    # make conditionally colored markers based on elevation
    # uses inline if statements -> may not satisfy PEP8
    map.add_child(
        folium.Marker(
            [lat, lon],
            popup=name,
            icon=folium.Icon(
                color='green' if elev in range(0, 1000)
                else 'blue' if elev in range(1000, 3000)
                else 'red'
            )
        )
    )


# save and create map html file
map.save("map1.html")
