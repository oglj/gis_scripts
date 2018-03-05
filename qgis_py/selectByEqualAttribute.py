from qgis.core import *
import processing

# select features from layer 2 if they share an object id with features in layer 1

# change "layer 1" & "Layer 2" to the names of the layers in question

layer1 = processing.getObject("Layer 1")
layer2 = processing.getObject("Layer 2")

layer1Features = layer1.getFeatures()
layer2Features = layer2.getFeatures()

# 'OBJECTID' as default attribute for selection; can be any two attributes

layer1ID = [layer1ID.append(feature['OBJECTID']) for feature in layer1Features]

for feature in layer2Features:
    if feature['OBJECTID'] in layer1ID:
        layer2.select(feature.id())

#To do: Script this as a function with shapefile names and attributes as arguments
