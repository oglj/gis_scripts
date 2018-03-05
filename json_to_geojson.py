# Python 2.7
#---Libraries---################################################################

import json

#---Arguments---################################################################

# Declare file paths for input JSON file and output geoJSON file
# input JSON must consist of a dictionary of length = 1 with key "features" 

inputFilePath = r"C:\input\filepath.json"
outputFilePath = r"C:\output\filepath.geojson"

# Declare the names of the values associated with latitude and longitude

latKey = "latitude"
lngKey = "longitude"

# Declare the feature type

# So far only optimized this for point features.  Haven't handled polylines,
# polygons, nor multitype features yet.

featureType = "Point"

#---Script---###################################################################

jsonFile = open(inputFilePath)
geojsonFile = open(outputFilePath, 'w')

jsonData = json.loads(jsonFile.read())

geojson = {
	"type": "FeatureCollection",
	"features" : [
	{
		"type": "Feature",
		"geometry" : {
			"type": featureType,
			"coordinates": [d[lngKey], d[latKey]],
			},
		"properties" : d,
	} for d in jsonData["features"]]
}

json.dump(geojson, geojsonFile)

jsonFile.close()
geojsonFile.close()
