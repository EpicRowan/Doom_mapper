import pandas as pd 
import googlemaps

"""Tall Buildings need their addresses translated into lat/long coordinates with geocoding"""

tb = pd.read_csv("seed_data/Tall_Building_Inventory_clean.csv")

gmaps_key = googlemaps.Client(key="AIzaSyDeNiHduiEBvQI2CnzC1dis32FDktKV4eA")

tb["LAT"] = None
tb["LON"] = None

for i in range(0, len(tb)):
	geocode_result = gmaps_key.geocode(tb.iat[i,0])
	try:
		lat = geocode_result[0]["geometry"]["location"]["lat"]
		lon = geocode_result[0]["geometry"]["location"]["lon"]
		tb.iat[i, tb.columns.get_loc("LAT")] = lat
		tb.iat[i, tb.columns.get_loc("LON")] = lon
	except:
		lat = None
		lon = None
