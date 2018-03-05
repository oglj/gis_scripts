from qgis.core import *
import processing

roadOSM = processing.getObject("ct_roads_OSM_NAD27 [11919]")
bufferFAF = processing.getObject("ct_roadsAADT_FAF_NAD27_200ftBuffer")

for a in roadOSM.getFeatures():
    for b in bufferFAF.getFeatures():
        if a.geometry().intersects(b.geometry()):
            roadOSM.select(a.id())
