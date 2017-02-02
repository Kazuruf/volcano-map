import folium
import pandas

# create pandas dataframe
volcano_df = pandas.read_csv("Volcanoes-USA.txt")
elev_col = volcano_df["ELEV"]
lat_mean = volcano_df["LAT"].mean()
long_mean = volcano_df["LON"].mean()

# elevation data
min_elev = min(elev_col)
max_elev = max(elev_col)
med_elev = (elev_col).median()
low_quant = elev_col.quantile(0.25)
high_quant = elev_col.quantile(0.55)

# create the base map
map = folium.Map(location=[lat_mean, long_mean],
                 zoom_start=4,
                 tiles='Stamen Terrain')


def color_marker(elev):
    if elev in range(int(min_elev), int(low_quant)):
        color = 'green'
    elif elev in range(int(low_quant), int(med_elev)):
        color = 'orange'
    elif elev in range(int(med_elev), int(high_quant)):
        color = 'blue'
    else:
        color = 'red'
    return color


# iterate through the data frame and create markers based on the lat/long
for lat, lon, name, elev in zip(volcano_df["LAT"],
                                volcano_df["LON"],
                                volcano_df["NAME"],
                                volcano_df["ELEV"]):
    # map markers
    # make conditionally colored markers based on elevation
    # uses inline if statements -> may not satisfy PEP8
    marker_label = name + str(elev) + "m"
    map.add_child(
        folium.Marker(
            [lat, lon],
            popup=marker_label,
            icon=folium.Icon(
                color=color_marker(elev)
            )
        )
    )


# save and create map html file
map.save("map1.html")
