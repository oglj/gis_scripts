#---Description---##############################################################
#
# Select features from active layer if they share an attribute value with 
# features in reference layer
#
# To do: Script as function with shapefile names and attributes as arguments
#
#---Imports---##################################################################
from qgis.core import *
import processing

#---Arguments---################################################################

# layer names

activeLayerName = "Layer 1"
refLayerName = "Layer2"

# attribute names

activeAttribute = "OBJECTID"
refAttribute = "OBJECTID"

#---Script---###################################################################

refLayer = processing.getObject(refLayerName)
activeLayer = processing.getObject(activeLayerName)

refFeatures = refLayer.getFeatures()
activeFeatures = activeLayer.getFeatures()

refValues = [feature[refAttribute] for feature in refFeatures]

for feature in activeFeatures:
    if feature[activeAttribute] in refValues:
        activeLayer.select(feature.id())
