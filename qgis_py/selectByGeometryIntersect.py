from qgis.core import *
import processing

# change names in getObject() to names of layers for selection and intersection reference, respectively

selectLayer = processing.getObject("Layer 1")
refLayer = processing.getObject("Layer 2")

for a in selectLayer.getFeatures():
    for b in refLayer.getFeatures():
        if a.geometry().intersects(b.geometry()):
            selectLayer.select(a.id())
