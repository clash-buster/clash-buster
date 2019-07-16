
from Autodesk.Revit import DB, Creation, UI
from pyrevit import revit
import clash
import rhino_decider
import clr
import sys

doc = revit.doc
uidoc = revit.uidoc
uiapp = __revit__.Application

revitversion = int(uiapp.VersionNumber )

""" Read Decision Maker Results File"""
def readxml():
    outdata = dict()
    outdata["clashid"] = ""
    outdata["elementAId"] = 653435 #beam
    outdata["elementBId"] = 676828 #pipe
    outdata["imagefilename"] = ""
    return outdata
    
class clashdata(object):
    def __init__(self):
        self.xmldata = readxml()
        self.beam = revit.doc.GetElement(DB.ElementId(self.xmldata["elementAId"]))
        self.beamdata = clash.get_beam_data(self.beam)
        self.pipe = revit.doc.GetElement(DB.ElementId(self.xmldata["elementBId"]))
        self.pipedata = clash.get_pipe_data(self.pipe)


def structuralframingopening():
    for ref in beam.GetReferences(DB.FamilyInstanceReferenceType.CenterFrontBack):
        print ref
        radius = 10
        startAngle = 0
        endAngle = 2 * Math.PI     
        curve = Arc.Create(plane, radius, startAngle, endAngle)
        Creation.Document.NewOpening(beam, CurveArray, ref) 

cd = clashdata()

pointsdict = rhino_decider.get_intersection_data(cd.beamdata, cd.pipedata)

v = pointsdict["option_crawl90"]
clash.createnewpipefrompoints(rhino_decider.convert_rhinopoint_to_xyz(v), cd.pipedata)
