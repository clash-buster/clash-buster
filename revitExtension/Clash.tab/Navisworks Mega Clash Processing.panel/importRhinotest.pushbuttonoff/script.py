
import rhino_decider
from Autodesk.Revit import DB
rh_line =  rhino_decider.convert_rvtLine_to_RhinoLine(DB.Line.CreateBound(DB.XYZ(0,0,0),DB.XYZ(100,0,0)))


import Rhino.Geometry as rg

print rg.Extrusion.Create(rg.LineCurve(rh_line), -5, False)
